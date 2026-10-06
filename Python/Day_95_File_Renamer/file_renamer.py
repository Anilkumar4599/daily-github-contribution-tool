from pathlib import Path


def rename_files(folder_name):
    """
    Rename all files in a folder using a consistent naming pattern.
    """

    folder = Path(folder_name)

    if not folder.exists():
        print(f"Error: Folder does not exist: {folder}")
        return

    if not folder.is_dir():
        print(f"Error: Path is not a folder: {folder}")
        return

    files = sorted(
        [file for file in folder.iterdir() if file.is_file()]
    )

    if not files:
        print("No files found.")
        return

    print("=== FILE RENAMING AUTOMATION ===")

    for number, file in enumerate(files, start=1):

        new_name = f"Renamed_File_{number:03d}{file.suffix}"
        new_path = folder / new_name

        if new_path.exists():
            print(f"Skipped: {new_name} already exists.")
            continue

        file.rename(new_path)

        print(f"{file.name} -> {new_name}")


if __name__ == "__main__":
    rename_files("test_files")