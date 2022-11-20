import os
import subprocess
import argparse

# Set max size to 1MB
MAX_SIZE = 1000000

def resize_dir(dpath):
    print(f'Compressing image files in {dpath} to be under {MAX_SIZE} bytes...')
    fnames = os.listdir(dpath)
    for fname in fnames:
        fpath = os.path.join(dpath, fname)
        fsize = int(os.path.getsize(fpath))
        presize = fsize
        while fsize > 1000000:
            bashCommand = f"convert, -resize, 50%, {fpath}, {fpath}"
            process = subprocess.Popen(bashCommand.split(', '), stdout=subprocess.PIPE)
            _, _ = process.communicate()
            fsize = int(os.path.getsize(fpath))
        cursize = fsize
        size_info = fsize if presize==cursize else f"{presize} -> {cursize}"
        print(fpath, size_info, '✓')



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('dpath')
    args = parser.parse_args()
    resize_dir(args.dpath)