from pathlib import Path
import shutil


def sync(home: Path) -> None:
    source = Path(__file__).resolve().parent
    codex = home / ".codex"
    codex.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / "AGENTS.md", codex / "AGENTS.md")
    shutil.copytree(
        source / "skills",
        home / ".agents" / "skills",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("tmp", "*.zh.md"),
    )
    shutil.copytree(source / "tmp", source.parent / "tmp", dirs_exist_ok=True)
    print(f"Updated {codex / 'AGENTS.md'}")
    print(f"Updated {home / '.agents' / 'skills'}")
    print(f"Updated {source.parent / 'tmp'}")


if __name__ == "__main__":
    sync(Path.home())
