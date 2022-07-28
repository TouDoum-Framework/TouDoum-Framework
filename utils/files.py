from hashlib import md5


def md5sum(filename, size=65536):
    """
    Calculate the md5sum of a file
    :param filename: file to calculate md5sum
    :param size: default is 65536
    :return str: md5sum of the file
    """
    try:
        hash_content = md5()
        with open(filename, "rb") as stream:
            for block in iter(lambda: stream.read(size), b""):
                hash_content.update(block)
        return hash_content.hexdigest()
    except FileNotFoundError:
        return None
