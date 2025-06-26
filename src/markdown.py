def markdown_to_blocks(markdown):
    # 1. Divide por doble salto de línea
    raw_blocks = markdown.split("\n\n")

    # 2. Limpia espacios alrededor y filtra bloques vacíos
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]

    return blocks
