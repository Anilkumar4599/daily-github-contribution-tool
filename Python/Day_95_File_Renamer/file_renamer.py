from pathlib import Path


def get_next_number(folder):
    """Find the next available Renamed_File number."""

    existing_numbers = []

    for file in folder.iterdir():
        if file.is_file() and file.name.startswith("Renamed_File_"):
            try:
                number_part = file.stem.replace("Renamed_File_", "")
                existing_numbers.append(int(number_part))
            except ValueError:
                continue

    if not existing_numbers:
        return 1

    return max(existing_numbers) + 1


def rename_files(folder_name):
    """
    Rename files using a consistent naming pattern.
    Already renamed files are skipped.
    """

    folder = Path(folder_name)

    if not folder.exists():
        print(f"Error: Folder does not exist: {folder}")
        return

    if not folder.is_dir():
        print(f"Error: Path is not a folder: {folder}")
        return

    files = sorted(
        [
            file
            for file in folder.iterdir()
            if file.is_file() and not file.name.startswith("Renamed_File_")
        ]
    )

    if not files:
        print("No files available for renaming.")
        return

    print("=== FILE RENAMING AUTOMATION ===")

    next_number = get_next_number(folder)

    for file in files:

        new_name = f"Renamed_File_{next_number:03d}{file.suffix}"
        new_path = folder / new_name

        file.rename(new_path)

        print(f"{file.name} -> {new_name}")

        next_number += 1


if __name__ == "__main__":
    rename_files("test_files")