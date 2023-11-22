#Autor: Sharon Michelle Olvera Ibarra
#Descripción: El módulo os
#Fecha: 20/11/2023

import os

def find(path, target_dir):
    
    abs_path = os.path.abspath(path)
    
    def search_directory(current_path):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            if os.path.isdir(item_path):
                if item == target_dir:
                    print(os.path.abspath(item_path))
                search_directory(item_path)

    search_directory(abs_path)
find("./tree", "python")
