import os

dirs = [
    "data\\raw",
    "data\\processed",
    "notebooks",
    "saved_models",
    "src"

]
for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    "src\\__init.py"
]

for file in files:
    with open(file,"w") as f:
        pass
