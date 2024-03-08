import os
from glob import glob
import time

from Cryptodome.Cipher import AES

key = b"cfsv1JVnGqZwAbsS1LWRnVemMpqZ7iep"

def decrypt(filename):
    with open(filename, "rb") as f:
        data = f.read()
    iv = data[:16]
    data = data[16:]
    return AES.new(key, AES.MODE_CFB, segment_size=8, IV=iv).decrypt(data)

def find_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def get_subpath(full_path):
    subpath1 = full_path.split("pituitary\\")[1]
    subpath2 = "\\".join(subpath1.split("\\")[1:])
    return subpath2

def main():
    data_root = "c:\\Users\\david\\Exjobb\\data\\pituitary\\accel"
    source_paths = glob(f"{data_root}/**/*.csv", recursive=True)
    source_subpaths = [get_subpath(path) for path in source_paths]
    target_root = "c:\\Users\\david\\Exjobb\\data\\pituitary\\accel_decrypted"

    target_paths = glob(f"{target_root}\\**\\*.csv", recursive=True)
    target_subpaths = [get_subpath(path) for path in target_paths]
    missing_subpaths = set(source_subpaths) - set(target_subpaths)
    for i, missing_subpath in enumerate(missing_subpaths):
        if i % 100 == 1:
            print(f"{i} / {len(missing_subpaths)}")
        source_path = os.path.join(data_root, missing_subpath)
        d = decrypt(source_path)
        target_path = os.path.join(target_root, missing_subpath)
        os.makedirs("\\".join(target_path.split("\\")[:-1]), exist_ok=True)
        with open(target_path, "wb+") as f:
            f.write(d)

if __name__ == '__main__':
    main()
