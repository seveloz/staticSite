from textnode import TextNode, TextType
import os
import shutil
from generator import generate_pages_recursive
from copy_static import copy_static_files  # asegúrate de tener esta función

def copy_static_files(source_dir="static", dest_dir="public"):
    # Eliminar el directorio de destino si ya existe
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Removed existing directory: {dest_dir}")

    # Crear el nuevo directorio de destino
    os.makedirs(dest_dir)
    print(f"Created directory: {dest_dir}")

    # Función recursiva para copiar archivos
    def recursive_copy(src, dst):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)

            if os.path.isdir(src_path):
                os.makedirs(dst_path)
                print(f"Created directory: {dst_path}")
                recursive_copy(src_path, dst_path)
            else:
                shutil.copy(src_path, dst_path)
                print(f"Copied file: {src_path} -> {dst_path}")

    recursive_copy(source_dir, dest_dir)

def main():
    print("Copying static files...")
    copy_static_files()
    print("Static files copied successfully!")
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()


