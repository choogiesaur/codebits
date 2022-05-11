import os
import hashlib
from collections import defaultdict

def hash_for_file(file, BUFFER=65536):
    md5 = hashlib.md5()
    with open(file, "rb") as f:
        while True:
            buf = f.read(BUFFER)
            if not buf:
                break
            md5.update(buf)
    return md5.hexdigest()

def compare_two_folders(folder_a, folder_b):
    dict_a = defaultdict(str)
    dict_b = defaultdict(str)
    intersection = set()

    for root, dirs, files in os.walk(folder_a, topdown=False):
        for file in files:
            dict_a[file] = hash_for_file(os.path.join(root,file))

    for root, dirs, files in os.walk(folder_b, topdown=False):
        for file in files:
            dict_b[file] = hash_for_file(os.path.join(root,file))

    # Expose unique files (stuff not in the intersection of both sets)
    print(f"Scanning {folder_a}:")
    for item in dict_a:
        if item not in dict_b:
            print(f"{item} is not found in {folder_b}")
        else:
            intersection.add(item)
            
    print(f"Scanning {folder_b}:")
    for item in dict_b:
        if item not in dict_a:
            print(f"{item} is not found in {folder_a}")
        else:
            intersection.add(item)
    
    print(f"\nComparing hashes of common files in {folder_a}, {folder_b}")
    for item in intersection:
        print(f"{item}\n  {dict_a[item]}\n  {dict_b[item]}")

compare_two_folders('fsattar-1.0.9', 'fsattar-1.0.10')
