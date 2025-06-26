import os
from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 title found in markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    result = template.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(entry_path) and entry.endswith(".md"):
            html_filename = entry.replace(".md", ".html")
            final_dest_path = os.path.join(dest_dir_path, html_filename)
            generate_page(entry_path, template_path, final_dest_path)

        elif os.path.isdir(entry_path):
            # Asegúrate de que la carpeta destino exista
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            # Llama recursivamente
            generate_pages_recursive(entry_path, template_path, dest_path)
