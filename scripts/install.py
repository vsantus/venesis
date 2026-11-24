import argparse
import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {"berners": "Front-end engineering", "turing": "Back-end engineering", "uncle-bob": "QA and software quality", "codd": "Data engineering", "rams": "UX/UI and creative direction"}

def render(name, target):
    paths = ["core/principles.md", "core/collaboration.md", f"agents/{name}/identity.md", f"agents/{name}/instructions.md"]
    if name == "rams":
        paths.append("skills/rams-creative.md")
    body = "\n\n".join((ROOT / p).read_text(encoding="utf-8") for p in paths)
    if target == "opencode":
        return f"---\ndescription: {AGENTS[name]}\nmode: subagent\n---\n\n{body}\n"
    payload = {"name": name, "description": AGENTS[name], "developer_instructions": body}
    text = "".join(f"{k} = {json.dumps(v, ensure_ascii=False)}\n" for k, v in payload.items())
    assert tomllib.loads(text) == payload
    return text

def main():
    p = argparse.ArgumentParser()
    p.add_argument("project", type=Path)
    p.add_argument("--target", choices=["codex", "opencode", "all"], default="codex")
    p.add_argument("--agents", nargs="+", choices=list(AGENTS), default=list(AGENTS))
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()
    project = args.project.resolve()
    if not project.is_dir():
        p.error("Project must exist")
    outputs = {}
    for target in (["codex", "opencode"] if args.target == "all" else [args.target]):
        folder = project / ("." + target) / "agents"
        if not folder.resolve().is_relative_to(project):
            p.error("Target outside project")
        for name in args.agents:
            path = folder / (name + (".toml" if target == "codex" else ".md"))
            if path.is_symlink() or (path.exists() and not args.force):
                p.error(f"Refusing overwrite: {path}")
            outputs[path] = render(name, target)
    for path, body in outputs.items():
        if not args.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
        print(path)

if __name__ == "__main__":
    main()
