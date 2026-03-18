import json

path = r'c:\Users\Luís Felipe\Documents\GitHub\computer-vision\LeNet5_Architecture.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

count = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        new_source = []
        replaced = False
        for line in source:
            if 'model_loaded' in line:
                new_line = line.replace('model_loaded', 'model')
                new_source.append(new_line)
                replaced = True
            else:
                new_source.append(line)
        if replaced:
            cell['source'] = new_source
            count += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"Notebook updated. Replaced 'model_loaded' in {count} cells.")
