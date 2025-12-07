import re
import zipfile
import tarfile
from pathlib import Path

import requests


def download_and_extract_gdrive_hw3():
    """
    Завантажує архів з Google Drive (goit-rdb-hw-03) і розпаковує його
    в папку ./downloads поруч із цим файлом.

    Повертає:
        (шлях до архіву, шлях до папки з розпакованим вмістом)
    """

    # Оригінальне посилання з Google Drive
    url = "https://drive.google.com/file/d/1B45tkzH3lIrf2CmQIB2VB0AJRB9Ly7c2/view?usp=drive_link"

    # Папка, куди все складати (downloads поруч із mai.py)
    base_dir = Path(__file__).parent
    extract_dir = base_dir / "downloads"
    extract_dir.mkdir(parents=True, exist_ok=True)

    # Витягуємо file_id з URL
    m = re.search(r"/d/([^/]+)/", url)
    if not m:
        raise ValueError("Не вдалося витягнути file_id з URL")

    file_id = m.group(1)
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # Шлях до завантаженого файлу
    archive_path = extract_dir / f"{file_id}.bin"

    # Завантаження файлу
    print("Завантажую файл з Google Drive...")
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(archive_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    print(f"Файл завантажено: {archive_path.resolve()}")

    # Спроба розпакувати
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, "r") as zf:
            zf.extractall(extract_dir)
        print(f"ZIP-архів розпаковано в: {extract_dir.resolve()}")
    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, "r:*") as tf:
            tf.extractall(extract_dir)
        print(f"TAR-архів розпаковано в: {extract_dir.resolve()}")
    else:
        print("Попередження: файл не схожий на ZIP або TAR-архів. Нічого не розпаковано.")

    return str(archive_path), str(extract_dir)


if __name__ == "__main__":
    archive, folder = download_and_extract_gdrive_hw3()
    print("Готово.")
    print("Архів:", archive)
    print("Розпаковано (якщо це був архів) у:", folder)