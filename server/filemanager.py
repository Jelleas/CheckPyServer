import dropbox
import os

UPLOAD_FOLDER = os.path.abspath("uploads")

with open("credentials.txt") as f:
    _dbx = dropbox.Dropbox(f.readline().strip())

class get:
    def __init__(self, dropboxPath):
        dest = _filePath(dropboxPath)
        destDir = os.path.dirname(dest)
        if not os.path.exists(destDir):
            os.makedirs(destDir)

        if not os.path.exists(dest):
            _dbx.files_download_to_file(dest, dropboxPath)

        self._fileLocation = dest

    def __enter__(self):
        f = open(self._fileLocation, "r")
        return f

    def __exit__ (self, exc_type, exc_value, traceback):
        f.close()
        os.remove(self._fileLocation)


class getCached:
    def __init__(self, dropboxPath):
        self._fileLocation = _cachePath(dropboxPath)

    def __enter__(self):
        f = open(self._fileLocation, "r")
        return f

    def __exit__ (self, exc_type, exc_value, traceback):
        f.close()

def isCached(dropboxPath):
    return os.path.exists(_cachePath(dropboxPath))

def cache(json, dropboxPath):
    with open(_cachePath(dropboxPath), "w") as f:
        f.write(json)

def _filePath(dropboxPath):
    dropboxDir = os.path.dirname(dropboxPath[1:] if dropboxPath.startswith("/") else dropboxPath)
    destDir =  os.path.join(UPLOAD_FOLDER, dropboxDir)
    return os.path.join(destDir, os.path.basename(dropboxPath))

def _cachePath(dropboxPath):
    return _filePath(dropboxPath).replace(".py", ".json")
