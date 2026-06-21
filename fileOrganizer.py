import shutil
import sys
from pathlib import Path

def organize_directory(directory_path: str):
    clean_path = directory_path.strip('\"\'')
    base_dir = Path(clean_path).resolve()

    if not base_dir.is_dir():
        return

    script_name = Path(sys.argv[0]).name

    for item in base_dir.iterdir():
        if item.is_file() and item.name != script_name:
            ext = item.suffix.lower().replace('.', '')
            folder_name = ext if ext else "unknown"

            target_dir = base_dir / folder_name
            target_dir.mkdir(exist_ok=True)

            try:
                shutil.move(str(item), str(target_dir / item.name))
            except Exception:
                pass

if __name__ == "__main__":
    target_folder = input("Enter folder path (or press Enter for current folder): ")
    if not target_folder.strip():
        target_folder = "."
    organize_directory(target_folder)
