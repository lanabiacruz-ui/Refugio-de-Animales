import json
import os

def cargar(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r", enconding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    