import json

path = r'c:\Users\Luís Felipe\Documents\GitHub\computer-vision\LeNet5_Architecture.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Better: Find cells by markdown headers
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_md = "".join(cell['source'])
        if '### 8. Carregamento' in source_md:
            # The next code cell is what we want
            idx = nb['cells'].index(cell)
            for j in range(idx + 1, len(nb['cells'])):
                if nb['cells'][j]['cell_type'] == 'code':
                    code_cell = nb['cells'][j]
                    source = code_cell['source']
                    if 'import os' not in "".join(source):
                        new_source = [
                            "import os\n",
                            "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n"
                        ] + source
                        code_cell['source'] = new_source
                        print(f"Updated Topic 8 code cell (index {j})")
                    break
        elif '### 1. Definição' in source_md:
            idx = nb['cells'].index(cell)
            for j in range(idx + 1, len(nb['cells'])):
                if nb['cells'][j]['cell_type'] == 'code':
                    source = nb['cells'][j]['source']
                    if 'import os' not in "".join(source):
                        source.insert(0, "import os\n")
                    if 'device =' not in "".join(source):
                        for k, line in enumerate(source):
                            if line.startswith('class LeNet5'):
                                source.insert(k, "\n")
                                source.insert(k, "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n")
                                break
                    print(f"Updated Topic 1 code cell (index {j})")
                    break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully.")
