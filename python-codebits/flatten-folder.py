"""
flatten-folder.py

Run this script from the top-level folder that contains your topic folders (a, b, c, d, e, ...).
For each immediate subfolder (topic), it recursively finds every file nested inside and moves
them all up to that topic's root. Empty subdirectories are then removed.

Usage:
    python flatten-folder.py

Optional flags:
    --dry-run       Preview what would happen without moving anything
    --yes           Skip the confirmation prompt and run immediately
"""

import os
import sys
import shutil
import argparse
from pathlib import Path


def get_safe_destination(dest_dir: Path, filename: str) -> Path:
    """
    If a file with this name already exists at the destination, append a counter
    to avoid overwriting it. E.g. photo.jpg -> photo_2.jpg -> photo_3.jpg
    """
    dest = dest_dir / filename
    if not dest.exists():
        return dest

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 2
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        dest = dest_dir / new_name
        if not dest.exists():
            return dest
        counter += 1


def flatten_topic(topic_dir: Path, dry_run: bool) -> tuple[int, int]:
    """
    Move all files in subdirectories of topic_dir up to topic_dir itself.
    Returns (files_moved, dirs_removed).
    """
    files_moved = 0
    dirs_removed = 0

    # Collect all files that are NOT already at the top level of topic_dir
    files_to_move = [
        p for p in topic_dir.rglob("*")
        if p.is_file() and p.parent != topic_dir
    ]

    for src in files_to_move:
        dest = get_safe_destination(topic_dir, src.name)
        if dry_run:
            print(f"  [DRY RUN] Would move: {src.relative_to(topic_dir.parent)} -> {dest.relative_to(topic_dir.parent)}")
        else:
            shutil.move(str(src), str(dest))
            print(f"  Moved: {src.relative_to(topic_dir.parent)} -> {dest.name}")
        files_moved += 1

    if not dry_run:
        # Remove all now-empty subdirectories (bottom-up so parents clear after children)
        for subdir in sorted(topic_dir.rglob("*"), reverse=True):
            if subdir.is_dir():
                try:
                    subdir.rmdir()  # only succeeds if empty
                    print(f"  Removed empty dir: {subdir.relative_to(topic_dir.parent)}")
                    dirs_removed += 1
                except OSError:
                    print(f"  WARNING: Could not remove (not empty?): {subdir.relative_to(topic_dir.parent)}")

    return files_moved, dirs_removed


def main():
    parser = argparse.ArgumentParser(description="Flatten topic subfolders into their top-level directory.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    cwd = Path.cwd()
    topic_dirs = sorted([d for d in cwd.iterdir() if d.is_dir()])

    if not topic_dirs:
        print("No subfolders found in the current directory. Nothing to do.")
        sys.exit(0)

    print(f"Working directory : {cwd}")
    print(f"Topic folders found: {[d.name for d in topic_dirs]}")
    print()

    if args.dry_run:
        print("=== DRY RUN MODE — no files will be moved ===\n")
    elif not args.yes:
        confirm = input("This will move files and delete subdirectories. Continue? [y/N] ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            sys.exit(0)

    total_files = 0
    total_dirs = 0

    for topic in topic_dirs:
        print(f"\n[{topic.name}]")
        files, dirs = flatten_topic(topic, dry_run=args.dry_run)
        if files == 0:
            print("  Nothing to move — already flat.")
        total_files += files
        total_dirs += dirs

    print()
    if args.dry_run:
        print(f"Dry run complete. Would move {total_files} file(s).")
    else:
        print(f"Done. Moved {total_files} file(s), removed {total_dirs} empty director(ies).")


if __name__ == "__main__":
    main()
