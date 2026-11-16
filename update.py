from pathlib import Path
import shutil
import subprocess


def sync(home: Path) -> None:
    source = Path(__file__).resolve().parent
    subprocess.run(["git", "-C", str(source), "pull", "--ff-only"], check=True)
    instructions = (home / ".codex" / "AGENTS.md", home / ".dsh" / "AGENTS.md")
    for target in instructions:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / "AGENTS.md", target)
    shutil.copytree(
        source / "skills",
        home / ".agents" / "skills",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("tmp", "*.zh.md"),
    )
    shutil.copytree(source / "tmp", source.parent / "tmp", dirs_exist_ok=True)
    print(f"Updated {home / '.codex' / 'AGENTS.md'}")
    print(f"Updated {home / '.dsh' / 'AGENTS.md'}")
    print(f"Updated {home / '.agents' / 'skills'}")
    print(f"Updated {source.parent / 'tmp'}")


if __name__ == "__main__":
    sync(Path.home())
