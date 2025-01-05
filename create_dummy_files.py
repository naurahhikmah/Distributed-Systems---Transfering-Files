# create_dummy_files.py
import os

def create_dummy_file(file_name, size_kb):
    with open(file_name, 'wb') as f:
        f.write(os.urandom(size_kb * 1024))
    print(f'Created {file_name} of size {size_kb} KB')

if __name__ == '__main__':
    sizes_kb = [10, 100, 1024, 5120]  # 10 KB, 100 KB, 1 MB, 5 MB
    for size in sizes_kb:
        file_name = f'file_{size}KB.bin'
        create_dummy_file(file_name, size)
