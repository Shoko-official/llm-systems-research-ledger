import json
import re
import sys
from pathlib import Path

from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "Makefile",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/research_task.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
    "claims/README.md",
    "citations/README.md",
    "schemas/README.md",
    "schemas/source.json",
    "schemas/claim.json",
    "schemas/citation.json",
    "sources/README.md",
    "tests/README.md",
    "tests/test_schemas.py",
]




REQUIRED_DIRECTORIES = [
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "claims",
    "citations",
    "schemas",
    "scripts",
    "sources",
    "tests",
]

FOUNDATION_MARKERS = {
    "sources/README.md": [
        "# Sources",
        "## Source Record Profile",
        "## Evidence Class",
        "## Future File Naming",
        "Source ID",
        "Evidence class",
    ],
    "claims/README.md": [
        "# Claims",
        "## Claim Record Profile",
        "## Claim Status",
        "## Evidence State",
        "## Future File Naming",
        "Claim ID",
        "TODO:evidence_needed",
    ],
    "citations/README.md": [
        "# Citations",
        "## Handoff Goal",
        "## Claim Eligibility",
        "## Missing Evidence",
        "## Missing Citations",
        "## Ledger and Paper Boundary",
    ],
}

SECRET_PATTERNS = [
    re.compile(pattern)
    for pattern in [
        r"AKIA[0-9A-Z]{16}",
        r"gho_[A-Za-z0-9_]+",
        r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
        r"(?i)\b(password|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}",
    ]
]


def fail(message: str) -> None:
    raise SystemExit(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_text_files() -> list[Path]:
    excluded_parts = {".git", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if excluded_parts.intersection(path.parts):
            continue
        if path.suffix.lower() in {".md", ".yml", ".yaml", ".py", ""}:
            files.append(path)
    return files


def validate_required_paths() -> None:
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    missing_dirs = [path for path in REQUIRED_DIRECTORIES if not (ROOT / path).is_dir()]
    if missing_files or missing_dirs:
        details = []
        if missing_files:
            details.append("missing files: " + ", ".join(missing_files))
        if missing_dirs:
            details.append("missing directories: " + ", ".join(missing_dirs))
        fail("; ".join(details))


def validate_foundation_files() -> None:
    for relative_path, markers in FOUNDATION_MARKERS.items():
        path = ROOT / relative_path
        text = read_text(path)
        missing_markers = [marker for marker in markers if marker not in text]
        if missing_markers:
            fail(
                f"{relative_path} is missing expected marker(s): "
                + ", ".join(missing_markers)
            )


def parse_front_matter(text: str) -> dict | None:
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return None
    yaml_content = match.group(1)
    import yaml
    try:
        return yaml.safe_load(yaml_content)
    except Exception as e:
        raise ValueError(f"YAML parsing error: {e}")


def validate_source_records() -> None:
    source_dir = ROOT / "sources"
    schema_path = ROOT / "schemas" / "source.json"
    if not schema_path.is_file():
        return

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    for path in source_dir.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue

        text = read_text(path)
        try:
            front_matter = parse_front_matter(text)
        except Exception as e:
            fail(f"Invalid YAML front matter in sources/{path.name}: {e}")

        if front_matter is None:
            fail(f"Missing YAML front matter in sources/{path.name}. Source records must start and end with '---'.")

        try:
            validate(instance=front_matter, schema=schema)
        except ValidationError as e:
            fail(f"Validation error in sources/{path.name}: {e.message}")

        source_id = front_matter.get("source_id")
        expected_filename = f"{source_id}.md"
        if path.name != expected_filename:
            fail(f"Filename '{path.name}' does not match source_id '{source_id}'. Expected '{expected_filename}'.")


def get_all_sources() -> dict[str, dict]:
    sources_info = {}
    source_dir = ROOT / "sources"
    schema_path = ROOT / "schemas" / "source.json"
    if not schema_path.is_file():
        return sources_info

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    for path in source_dir.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue

        text = read_text(path)
        try:
            front_matter = parse_front_matter(text)
            if front_matter:
                source_id = front_matter.get("source_id")
                sources_info[source_id] = front_matter
        except Exception:
            # Let validate_source_records report errors
            pass
    return sources_info


def validate_claim_records() -> None:
    claim_dir = ROOT / "claims"
    schema_path = ROOT / "schemas" / "claim.json"
    if not schema_path.is_file():
        return

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    sources_info = get_all_sources()

    for path in claim_dir.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue

        text = read_text(path)
        try:
            front_matter = parse_front_matter(text)
        except Exception as e:
            fail(f"Invalid YAML front matter in claims/{path.name}: {e}")

        if front_matter is None:
            fail(f"Missing YAML front matter in claims/{path.name}. Claim records must start and end with '---'.")

        try:
            validate(instance=front_matter, schema=schema)
        except ValidationError as e:
            fail(f"Validation error in claims/{path.name}: {e.message}")

        claim_id = front_matter.get("claim_id")
        expected_filename = f"{claim_id}.md"
        if path.name != expected_filename:
            fail(f"Filename '{path.name}' does not match claim_id '{claim_id}'. Expected '{expected_filename}'.")

        try:
            verify_claim_business_rules(claim_id, front_matter, sources_info)
        except ValueError as e:
            fail(f"Validation error in claims/{path.name}: {e}")


def verify_claim_business_rules(claim_id: str, front_matter: dict, sources_info: dict) -> None:
    status = front_matter.get("status")
    evidence_state = front_matter.get("evidence_state")
    source_references = front_matter.get("source_references", [])
    primary_source_required = front_matter.get("primary_source_required")
    paper_readiness = front_matter.get("paper_readiness")

    # 1. Do not promote a claim to paper-ready status while its evidence state is TODO:evidence_needed
    if paper_readiness == "ready" and evidence_state == "TODO:evidence_needed":
        raise ValueError(f"Claim {claim_id} cannot be paper-ready ('ready') while evidence state is 'TODO:evidence_needed'.")

    # 2. Use TODO:evidence_needed whenever a claim lacks a usable source (i.e. source_references is empty)
    if not source_references and evidence_state != "TODO:evidence_needed":
        raise ValueError(f"Claim {claim_id} has no source references, so its evidence state must be 'TODO:evidence_needed' (got '{evidence_state}').")

    # 3. If evidence state is supported or partial, source_references must NOT be empty
    if evidence_state in ("supported", "partial") and not source_references:
        raise ValueError(f"Claim {claim_id} has evidence state '{evidence_state}' but no source references.")

    # 4. Use supported only when the claim has enough evidence for its current purpose
    if status == "supported" and evidence_state in ("TODO:evidence_needed", "not_applicable"):
        raise ValueError(f"Claim {claim_id} cannot have status 'supported' with evidence state '{evidence_state}'.")

    # 5. Validate that referenced sources exist
    for ref_id in source_references:
        if ref_id not in sources_info:
            raise ValueError(f"Referenced source '{ref_id}' does not exist.")

    # 6. If primary source required is yes and evidence state is supported, at least one referenced source must be primary
    if primary_source_required == "yes" and evidence_state == "supported":
        has_primary = any(
            sources_info[ref_id].get("evidence_class") == "primary"
            for ref_id in source_references
            if ref_id in sources_info
        )
        if not has_primary:
            raise ValueError(f"Claim {claim_id} requires a primary source, but none of its referenced sources are of class 'primary'.")


def get_all_claims() -> dict[str, dict]:
    claims_info = {}
    claim_dir = ROOT / "claims"
    schema_path = ROOT / "schemas" / "claim.json"
    if not schema_path.is_file():
        return claims_info

    for path in claim_dir.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue

        text = read_text(path)
        try:
            front_matter = parse_front_matter(text)
            if front_matter:
                claim_id = front_matter.get("claim_id")
                claims_info[claim_id] = front_matter
        except Exception:
            pass
    return claims_info


def validate_citation_records() -> None:
    citation_dir = ROOT / "citations"
    schema_path = ROOT / "schemas" / "citation.json"
    if not schema_path.is_file():
        return

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    sources_info = get_all_sources()
    claims_info = get_all_claims()

    for path in citation_dir.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue

        text = read_text(path)
        try:
            front_matter = parse_front_matter(text)
        except Exception as e:
            fail(f"Invalid YAML front matter in citations/{path.name}: {e}")

        if front_matter is None:
            fail(f"Missing YAML front matter in citations/{path.name}. Citation records must start and end with '---'.")

        try:
            validate(instance=front_matter, schema=schema)
        except ValidationError as e:
            fail(f"Validation error in citations/{path.name}: {e.message}")

        citation_id = front_matter.get("citation_id")
        expected_filename = f"{citation_id}.md"
        if path.name != expected_filename:
            fail(f"Filename '{path.name}' does not match citation_id '{citation_id}'. Expected '{expected_filename}'.")

        try:
            verify_citation_business_rules(citation_id, front_matter, sources_info, claims_info)
        except ValueError as e:
            fail(f"Validation error in citations/{path.name}: {e}")


def verify_citation_business_rules(citation_id: str, front_matter: dict, sources_info: dict, claims_info: dict) -> None:
    source_id = front_matter.get("source_id")
    claim_id = front_matter.get("claim_id")
    readiness_state = front_matter.get("readiness_state")
    missing_detail = front_matter.get("missing_citation_detail")

    # 1. Validate source_id exists
    if source_id not in sources_info:
        raise ValueError(f"Referenced source '{source_id}' does not exist.")

    # 2. Validate claim_id exists if not null
    if claim_id is not None and claim_id not in claims_info:
        raise ValueError(f"Referenced claim '{claim_id}' does not exist.")

    # 3. If readiness_state is ready_for_bibliography, missing_citation_detail should be null or "None"
    if readiness_state == "ready_for_bibliography":
        if missing_detail is not None and str(missing_detail).strip().lower() != "none" and str(missing_detail).strip() != "":
            raise ValueError(f"Citation {citation_id} cannot be 'ready_for_bibliography' with missing detail: '{missing_detail}'.")


def run_validate() -> None:
    validate_required_paths()
    validate_foundation_files()
    validate_source_records()
    validate_claim_records()
    validate_citation_records()





def lint_text() -> None:
    for path in iter_text_files():
        text = read_text(path)
        relative = path.relative_to(ROOT)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret in {relative}: {pattern.pattern}")


def run_lint() -> None:
    lint_text()


def run_unit_tests() -> None:
    import unittest
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        fail("Unit tests failed.")


def run_test() -> None:
    run_validate()
    run_lint()
    run_unit_tests()



def main(argv: list[str]) -> int:
    if len(argv) == 1:
        command = "test"
    elif len(argv) == 2 and argv[1] in {"validate", "lint", "test"}:
        command = argv[1]
    else:
        print("usage: validate_repo.py {validate|lint|test}", file=sys.stderr)
        return 2

    if command == "validate":
        run_validate()
    elif command == "lint":
        run_lint()
    else:
        run_test()

    print(f"{command} ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
