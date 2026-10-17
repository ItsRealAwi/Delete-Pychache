import os as Os
import shutil as Shutil
from pathlib import Path as Path


def DeletePycacheDirectories() -> int:
    ObexDirectory = Path(__file__).resolve().parent
    DeletedCount = 0

    for CurrentDirectory, DirectoryNames, _ in Os.walk(ObexDirectory, topdown=True, followlinks=False):
        for DirectoryName in DirectoryNames[:]:
            if DirectoryName != "__pycache__":
                continue

            PycacheDirectory = Path(CurrentDirectory) / DirectoryName
            if PycacheDirectory.is_symlink() or (
                hasattr(PycacheDirectory, "is_junction") and PycacheDirectory.is_junction()
            ):
                continue

            Shutil.rmtree(PycacheDirectory)
            DirectoryNames.remove(DirectoryName)
            DeletedCount += 1

    return DeletedCount


if __name__ == "__main__":
    DeletedCount = DeletePycacheDirectories()
    print(f"Removed {DeletedCount} __pycache__ director{'y' if DeletedCount == 1 else 'ies'} from {Path(__file__).resolve().parent}")
