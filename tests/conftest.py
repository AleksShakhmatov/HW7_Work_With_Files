import os
import pytest
import shutil
import zipfile
from script_os import FILES_DIR, FOLDER_DIR


@pytest.fixture(scope="session", autouse=True)
def files_archive():
    if not os.path.exists(FOLDER_DIR):
        os.mkdir(FOLDER_DIR)
    with zipfile.ZipFile(os.path.join(FOLDER_DIR, "archive.zip"), 'w') as zf:
        for file in os.listdir(FILES_DIR):
            zf.write(os.path.join(FILES_DIR, file), file)
    yield
    shutil.rmtree(FOLDER_DIR)