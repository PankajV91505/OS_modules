import os
import shutil
import argparse

def organize_files(source_folder, dry_run=False):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1][1:].lower()
            if not ext:
                continue

            target_dir = os.path.join(source_folder, ext)
            target_path = os.path.join(target_dir, file)

            if dry_run:
                print(f"[Dry Run] Would move: {file_path} → {target_path}")
            else:
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, target_path)
                print(f"Moved: {file_path} → {target_path}")

def main():
    parser = argparse.ArgumentParser(description="Organize files by extension")
    parser.add_argument('--source', type=str, required=True, help="Source folder to organize")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without moving files")
    args = parser.parse_args()

    organize_files(args.source, args.dry_run)

if __name__ == "__main__":
    main()
