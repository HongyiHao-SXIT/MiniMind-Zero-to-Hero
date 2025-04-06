#!/usr/bin/env python3
import os
from pathlib import Path

def create_llm_project(root_dir="llm-project"):
    """Generate the LLM project directory structure"""
    structure = {
        "configs": {
            "model": ["base.yaml", "7b.yaml"],
            "train": ["cpu.yaml", "multi_gpu.yaml"]
        },
        "data": {
            "raw": None,
            "processed": None,
            "dataloader.py": None,
            "tokenizer": ["vocab.json", "merges.txt"]
        },
        "docs": ["ARCHITECTURE.md", "PRETRAIN.md"],
        "scripts": {
            "deploy": None,
            "monitor": None,
            "data_preprocess.sh": None
        },
        "src": {
            "modeling": ["attention.py", "blocks.py", "__init__.py"],
            "training": ["trainer.py", "optim", "scheduler.py"],
            "utils": ["logging.py", "metrics.py"],
            "inference": ["api.py", "quantize.py"]
        },
        "tests": {
            "unit": None,
            "integration": None
        },
        "requirements.txt": None,
        "LICENSE": None,
        "README.md": None
    }

    def create_path(base, path_dict):
        for name, content in path_dict.items():
            full_path = base / name
            if content is None:  # File or empty dir
                if "." in str(name):  # Likely a file
                    full_path.touch()
                    print(f"Created file: {full_path}")
                else:
                    full_path.mkdir(parents=True, exist_ok=True)
                    print(f"Created directory: {full_path}")
            elif isinstance(content, list):  # Directory with files
                full_path.mkdir(parents=True, exist_ok=True)
                print(f"Created directory: {full_path}")
                for item in content:
                    item_path = full_path / item
                    if "." in item:  # File
                        item_path.touch()
                        print(f"  Created file: {item_path}")
                    else:  # Subdirectory
                        item_path.mkdir()
                        print(f"  Created subdirectory: {item_path}")
            elif isinstance(content, dict):  # Nested directory
                full_path.mkdir(parents=True, exist_ok=True)
                print(f"Created directory: {full_path}")
                create_path(full_path, content)

    project_root = Path(root_dir)
    print(f"\nCreating LLM project structure at: {project_root.absolute()}\n")
    create_path(project_root, structure)
    print("\nProject structure created successfully!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Generate LLM project structure')
    parser.add_argument('--dir', default='llm-project', help='Project root directory')
    args = parser.parse_args()
    
    create_llm_project(args.dir)