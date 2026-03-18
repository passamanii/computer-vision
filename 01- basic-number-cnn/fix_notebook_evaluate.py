import json

path = r'c:\Users\Luís Felipe\Documents\GitHub\computer-vision\LeNet5_Architecture.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find Topic 8 code cell
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_md = "".join(cell['source'])
        if '### 8. Carregamento' in source_md:
            idx = nb['cells'].index(cell)
            for j in range(idx + 1, len(nb['cells'])):
                if nb['cells'][j]['cell_type'] == 'code':
                    source = nb['cells'][j]['source']
                    new_source = []
                    for line in source:
                        # Replace model_loaded with model
                        new_line = line.replace('model_loaded', 'model')
                        new_source.append(new_line)
                    nb['cells'][j]['source'] = new_source
                    print(f"Updated Topic 8 (index {j}) to use 'model' instead of 'model_loaded'")
                    break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully.")
