import json
from typing import List, Dict, Any, cast



path = r'c:\Users\Luís Felipe\Documents\GitHub\computer-vision\LeNet5_Architecture.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Explicitly check that 'nb' is a dictionary and hint the type
if not isinstance(nb, dict):
    raise ValueError("The notebook file is not a valid JSON dictionary.")
nb_dict: Dict[str, Any] = nb

# Use .get() and cast to avoid [] indexing errors on ambiguously typed variables
cells_list = cast(List[Any], nb_dict.get('cells', []))

if not isinstance(cells_list, list):
    raise ValueError("The 'cells' field in the notebook is not a list.")

for idx, cell in enumerate(cells_list):

    if not isinstance(cell, dict):
        continue
        
    source_list = cell.get('source', [])
    # Safely join source lines even if they aren't a list
    source_text = "".join(source_list) if isinstance(source_list, list) else str(source_list)
    
    if cell.get('cell_type') == 'markdown' and '### 8. Carregamento' in source_text:
        # Avoid indexing/slicing entirely to satisfy the type checker's hallucinations
        all_cells_iter = iter(cells_list)
        # Advance the iterator to the position after the current cell
        for _ in range(idx + 1):
            next(all_cells_iter, None)
            
        # Search for the next code cell
        for j, target_cell in enumerate(all_cells_iter, start=idx + 1):
            if isinstance(target_cell, dict) and target_cell.get('cell_type') == 'code':
                new_source = [


                    "import os\n",
                    "import torch\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "\n",
                    "# Garantir que o dispositivo está definido\n",
                    "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n",
                    "\n",
                    "model_path = 'models/lenet5_mnist.pth'\n",
                    "if os.path.exists(model_path):\n",
                    "    # Instanciar a classe e carregar os pesos\n",
                    "    model = LeNet5()\n",
                    "    model.load_state_dict(torch.load(model_path, map_location=device))\n",
                    "    model.to(device)\n",
                    "    model.eval()\n",
                    "    \n",
                    "    print(f\"Modelo carregado com sucesso de {model_path}!\")\n",
                    "    \n",
                    "    # Teste de inferência\n",
                    "    if 'test_dataset' in globals():\n",
                    "        random_idx = np.random.randint(len(test_dataset))\n",
                    "        image, label = test_dataset[random_idx]\n",
                    "        \n",
                    "        with torch.no_grad():\n",
                    "            output = model(image.unsqueeze(0).to(device))\n",
                    "            _, predicted = torch.max(output, 1)\n",
                    "            \n",
                    "        plt.imshow(image.squeeze().numpy(), cmap='gray')\n",
                    "        plt.title(f\"Teste de Carregamento\\nReal: {label} | Predito: {predicted.item()}\")\n",
                    "        plt.axis('off')\n",
                    "        plt.show()\n",
                    "    else:\n",
                    "        print(\"test_dataset não encontrado. Por favor, execute a célula do Tópico 3.\")\n",
                    "else:\n",
                    "    print(f\"Arquivo {model_path} não encontrado.\")\n"
                ]
                # Use update() to avoid square bracket assignment syntax
                target_cell.update({'source': new_source})
                print(f"Topic 8 cell (index {j}) rewritten successfully.")
                break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
