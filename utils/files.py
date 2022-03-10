from hashlib import md5


def md5sum(filename, size=65536):
    try:
        hash_content = md5()
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(size), b""):
                hash_content.update(block)
        return hash_content.hexdigest()
    except FileNotFoundError:
        return None
