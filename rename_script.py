import os
import re

directory = input('Enter filepath: ')

for filename in os.listdir(directory):
    old_name = re.findall(r'[A-Z][a-z]+|[A-Z]\d+', filename)
    extension = re.findall(r'\.\w+', filename)
    new_name = '_'.join(old_name).lower()
    if old_name and extension:
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name + extension[0])
        os.rename(old_path, new_path)
    elif old_name:
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name.lower())
        os.rename(old_path, new_path)
    else:
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, filename.lower())
        os.rename(old_path, new_path)
