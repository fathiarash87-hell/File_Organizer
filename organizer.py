import argparse
from pathlib import Path
import shutil


categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Videos": [".mp4", ".mkv"],
}


def get_category(suffix):
    for category, extensions in categories.items():
        if suffix.lower() in extensions:
            return category
    return "Others"


def unique_path(path):
    counter = 1
    new_path = path
    while new_path.exists():
        new_path = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        counter += 1
    return new_path

def organize(folder, dry_run=False):
    folder = Path(folder)
    if not folder.is_dir():
        print("پوشه پیدا نشد", folder)
        return

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            target_folder = folder / category
            target = unique_path(target_folder / item.name)

            if dry_run:
                print("[تست]", item.name, "->", category)
            else:
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(target))
                print(item.name, "->", category)

def main():
    parser = argparse.ArgumentParser(description="مرتب‌کننده خودکار فایل‌ها")
    parser.add_argument("folder", help="مسیر پوشه‌ای که باید مرتب بشه")
    parser.add_argument("--dry-run", action="store_true",
                        help="فقط نشون بده چی می‌شه، بدون جابه‌جایی")
    args = parser.parse_args()
    organize(args.folder, args.dry_run)


if __name__ == "__main__":
    main()