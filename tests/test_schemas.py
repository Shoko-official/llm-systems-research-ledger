import json
import sys
import unittest
from pathlib import Path
from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_repo import parse_front_matter, verify_claim_business_rules, verify_citation_business_rules

class TestSchemaValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.source_schema_path = ROOT / "schemas" / "source.json"
        self.claim_schema_path = ROOT / "schemas" / "claim.json"
        self.citation_schema_path = ROOT / "schemas" / "citation.json"

        with open(self.source_schema_path, "r", encoding="utf-8") as f:
            self.source_schema = json.load(f)

        with open(self.claim_schema_path, "r", encoding="utf-8") as f:
            self.claim_schema = json.load(f)

        with open(self.citation_schema_path, "r", encoding="utf-8") as f:
            self.citation_schema = json.load(f)

    def test_parse_front_matter_valid(self) -> None:
        text = """---
source_id: source-test-2026
title: Test Source Title
authors: Jane Doe
year: 2026
source_type: paper
evidence_class: primary
venue: Arxiv
locator: https://arxiv.org
review_notes: Some note.
---
Some content here
"""
        data = parse_front_matter(text)
        self.assertIsNotNone(data)
        self.assertEqual(data["source_id"], "source-test-2026")
        self.assertEqual(data["year"], 2026)

    def test_parse_front_matter_invalid(self) -> None:
        text = "No front matter here"
        data = parse_front_matter(text)
        self.assertIsNone(data)


    def test_valid_source_schema(self) -> None:
        valid_source = {
            "source_id": "source-attention-is-all-you-need-2017",
            "title": "Attention Is All You Need",
            "authors": "Ashish Vaswani, et al.",
            "year": 2017,
            "source_type": "paper",
            "evidence_class": "primary",
            "venue": "NeurIPS",
            "locator": "arXiv:1706.03762",
            "review_notes": "First Transformer paper."
        }
        validate(instance=valid_source, schema=self.source_schema)

    def test_invalid_source_schema_missing_fields(self) -> None:
        invalid_source = {
            "source_id": "source-invalid-2026",
            "title": "Missing fields"
        }
        with self.assertRaises(ValidationError):
            validate(instance=invalid_source, schema=self.source_schema)

    def test_invalid_source_schema_bad_enum(self) -> None:
        invalid_source = {
            "source_id": "source-invalid-2026",
            "title": "Bad Enum",
            "authors": "Jane Doe",
            "year": 2026,
            "source_type": "invalid_type",
            "evidence_class": "primary",
            "venue": "Arxiv",
            "locator": "https://arxiv.org",
            "review_notes": "Note"
        }
        with self.assertRaises(ValidationError):
            validate(instance=invalid_source, schema=self.source_schema)

    def test_valid_claim_schema(self) -> None:
        valid_claim = {
            "claim_id": "claim-test-claim",
            "claim_text": "This is a test claim.",
            "status": "draft",
            "evidence_state": "TODO:evidence_needed",
            "source_references": [],
            "primary_source_required": "no",
            "review_notes": "Initial draft.",
            "paper_readiness": "not_ready"
        }
        validate(instance=valid_claim, schema=self.claim_schema)

    def test_invalid_claim_schema_missing_fields(self) -> None:
        invalid_claim = {
            "claim_id": "claim-invalid",
            "claim_text": "Missing status etc."
        }
        with self.assertRaises(ValidationError):
            validate(instance=invalid_claim, schema=self.claim_schema)

    def test_valid_citation_schema(self) -> None:
        valid_citation = {
            "citation_id": "citation-test-attention-2017",
            "source_id": "source-attention-is-all-you-need-2017",
            "claim_id": "claim-test-claim",
            "paper_section_target": "sections/introduction.md",
            "readiness_state": "ready_for_bibliography",
            "missing_citation_detail": None
        }
        validate(instance=valid_citation, schema=self.citation_schema)

    def test_invalid_citation_schema_missing_fields(self) -> None:
        invalid_citation = {
            "citation_id": "citation-invalid",
            "source_id": "source-invalid-2026"
        }
        with self.assertRaises(ValidationError):
            validate(instance=invalid_citation, schema=self.citation_schema)


class TestClaimBusinessRules(unittest.TestCase):
    def setUp(self) -> None:
        self.sources_info = {
            "source-primary-2017": {
                "source_id": "source-primary-2017",
                "evidence_class": "primary"
            },
            "source-secondary-2018": {
                "source_id": "source-secondary-2018",
                "evidence_class": "secondary"
            }
        }

    def test_ready_but_evidence_needed_fails(self) -> None:
        claim = {
            "claim_id": "claim-1",
            "evidence_state": "TODO:evidence_needed",
            "paper_readiness": "ready",
            "source_references": []
        }
        with self.assertRaises(ValueError) as ctx:
            verify_claim_business_rules("claim-1", claim, self.sources_info)
        self.assertIn("cannot be paper-ready", str(ctx.exception))

    def test_empty_sources_without_evidence_needed_fails(self) -> None:
        claim = {
            "claim_id": "claim-2",
            "evidence_state": "supported",
            "paper_readiness": "not_ready",
            "source_references": []
        }
        with self.assertRaises(ValueError) as ctx:
            verify_claim_business_rules("claim-2", claim, self.sources_info)
        self.assertIn("must be 'TODO:evidence_needed'", str(ctx.exception))

    def test_evidence_supported_but_empty_sources_fails(self) -> None:
        claim = {
            "claim_id": "claim-3",
            "evidence_state": "supported",
            "paper_readiness": "not_ready",
            "source_references": []
        }
        with self.assertRaises(ValueError):
            verify_claim_business_rules("claim-3", claim, self.sources_info)

    def test_status_supported_but_evidence_needed_fails(self) -> None:
        claim = {
            "claim_id": "claim-4",
            "status": "supported",
            "evidence_state": "TODO:evidence_needed",
            "source_references": []
        }
        with self.assertRaises(ValueError) as ctx:
            verify_claim_business_rules("claim-4", claim, self.sources_info)
        self.assertIn("cannot have status 'supported'", str(ctx.exception))

    def test_missing_referenced_source_fails(self) -> None:
        claim = {
            "claim_id": "claim-5",
            "evidence_state": "supported",
            "source_references": ["source-nonexistent-2026"]
        }
        with self.assertRaises(ValueError) as ctx:
            verify_claim_business_rules("claim-5", claim, self.sources_info)
        self.assertIn("does not exist", str(ctx.exception))

    def test_primary_required_but_none_primary_fails(self) -> None:
        claim = {
            "claim_id": "claim-6",
            "evidence_state": "supported",
            "source_references": ["source-secondary-2018"],
            "primary_source_required": "yes"
        }
        with self.assertRaises(ValueError) as ctx:
            verify_claim_business_rules("claim-6", claim, self.sources_info)
        self.assertIn("requires a primary source", str(ctx.exception))

    def test_primary_required_and_has_primary_passes(self) -> None:
        claim = {
            "claim_id": "claim-7",
            "status": "supported",
            "evidence_state": "supported",
            "source_references": ["source-primary-2017", "source-secondary-2018"],
            "primary_source_required": "yes",
            "paper_readiness": "ready"
        }
        # Should not raise any ValueError
        verify_claim_business_rules("claim-7", claim, self.sources_info)


class TestCitationBusinessRules(unittest.TestCase):
    def setUp(self) -> None:
        self.sources_info = {
            "source-primary-2017": {
                "source_id": "source-primary-2017",
                "evidence_class": "primary"
            }
        }
        self.claims_info = {
            "claim-valid": {
                "claim_id": "claim-valid"
            }
        }

    def test_valid_citation_business_rules(self) -> None:
        citation = {
            "citation_id": "citation-valid",
            "source_id": "source-primary-2017",
            "claim_id": "claim-valid",
            "readiness_state": "ready_for_bibliography",
            "missing_citation_detail": None
        }
        # Should not raise any ValueError
        verify_citation_business_rules("citation-valid", citation, self.sources_info, self.claims_info)

    def test_nonexistent_source_fails(self) -> None:
        citation = {
            "citation_id": "citation-invalid",
            "source_id": "source-nonexistent-2026",
            "claim_id": "claim-valid",
            "readiness_state": "ready_for_bibliography",
            "missing_citation_detail": None
        }
        with self.assertRaises(ValueError) as ctx:
            verify_citation_business_rules("citation-invalid", citation, self.sources_info, self.claims_info)
        self.assertIn("does not exist", str(ctx.exception))

    def test_nonexistent_claim_fails(self) -> None:
        citation = {
            "citation_id": "citation-invalid",
            "source_id": "source-primary-2017",
            "claim_id": "claim-nonexistent",
            "readiness_state": "ready_for_bibliography",
            "missing_citation_detail": None
        }
        with self.assertRaises(ValueError) as ctx:
            verify_citation_business_rules("citation-invalid", citation, self.sources_info, self.claims_info)
        self.assertIn("does not exist", str(ctx.exception))

    def test_ready_with_missing_detail_fails(self) -> None:
        citation = {
            "citation_id": "citation-invalid",
            "source_id": "source-primary-2017",
            "claim_id": "claim-valid",
            "readiness_state": "ready_for_bibliography",
            "missing_citation_detail": "page number locator needed"
        }
        with self.assertRaises(ValueError) as ctx:
            verify_citation_business_rules("citation-invalid", citation, self.sources_info, self.claims_info)
        self.assertIn("cannot be 'ready_for_bibliography' with missing detail", str(ctx.exception))
