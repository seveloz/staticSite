# src/copy_static.py
import os
import shutil

def copy_static_files(src_path="static", dest_path="public"):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    def copy_recursive(src, dest):
        if not os.path.exists(dest):
            os.makedirs(dest)
        for item in os.listdir(src):
            s_item = os.path.join(src, item)
            d_item = os.path.join(dest, item)
            if os.path.isdir(s_item):
                copy_recursive(s_item, d_item)
            else:
                shutil.copy(s_item, d_item)
                print(f"Copied: {d_item}")

    copy_recursive(src_path, dest_path)

