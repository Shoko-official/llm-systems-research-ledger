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
    "sources/README.md",
    "tests/README.md",
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


def run_validate() -> None:
    validate_required_paths()
    validate_foundation_files()
    validate_source_records()



def lint_text() -> None:
    for path in iter_text_files():
        text = read_text(path)
        relative = path.relative_to(ROOT)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret in {relative}: {pattern.pattern}")


def run_lint() -> None:
    lint_text()



def run_test() -> None:
    run_validate()
    run_lint()


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
