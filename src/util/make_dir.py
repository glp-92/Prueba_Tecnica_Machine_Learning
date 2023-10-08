import os

def make_dir(path_to_dir: str):
    if path_to_dir[-1] != "/": path_to_dir += "/"
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)
    return path_to_dir