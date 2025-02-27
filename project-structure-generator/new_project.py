import os
import importlib.util

def create_project_structure(project_name, project_type="default"):
    base_path = os.path.join(os.getcwd(), project_name)
    
    try:
        structure_module = importlib.import_module(f"structures.{project_type}")
        folders = structure_module.get_structure()
    except ModuleNotFoundError:
        print(f"Invalid project type! Using 'default' instead.")
        structure_module = importlib.import_module("structures.default")
        folders = structure_module.get_structure()
    
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    print(f"Project '{project_name}' of type '{project_type}' created successfully at {base_path}")

def main():
    project_name = input("Insert project name: ")
    if not project_name:
        print("Project name is required!")
        return
    
    structure_dir = os.path.join(os.getcwd(), "structures")
    structure_files = [f.replace(".py", "") for f in os.listdir(structure_dir) if f.endswith(".py")]
    
    print(f"Insert project type [{', '.join(structure_files)}]:")
    project_type = input()
    
    if project_type not in structure_files:
        print(f"Invalid project type! Using 'default' instead.")
        project_type = "default"
    
    create_project_structure(project_name, project_type)

if __name__ == "__main__":
    main()
