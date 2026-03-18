import json

path = r'c:\Users\Luís Felipe\Documents\GitHub\computer-vision\LeNet5_Architecture.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Cell 2 (index 2) is the first code cell (Topic 1)
# We add import os and device definition here
source_c2 = nb['cells'][2]['source']
if 'import os' not in "".join(source_c2):
    source_c2.insert(0, "import os\n")
if 'device =' not in "".join(source_c2):
    # Find first empty line or after imports
    for i, line in enumerate(source_c2):
        if line.startswith('class LeNet5'):
            source_c2.insert(i, "\n")
            source_c2.insert(i, "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n")
            break

# Cell index 14 (Topic 8 code cell) - Ensure 'device' and 'os' are available
# and handle potential missing test_dataset better or just ensure it works.
source_c14 = nb['cells'][14]['source']
# Check if device is initialized in this cell or assume global
# Actually, the previously fixed Topic 4 has its own initialization too.
# Let's add it here to be safe if they skip cells.
new_source_c14 = []
new_source_c14.append("import os\n")
new_source_c14.append("device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n")
new_source_c14.extend(source_c14)
nb['cells'][14]['source'] = new_source_c14

# Also, move the 'import torch', etc. list if needed, but they are there.

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully.")
