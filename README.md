# 🌳 Estructura de Datos - Implementación en Python

Bienvenido a mi repositorio de **Estructuras de Datos** implementadas desde cero en Python.  
Este proyecto tiene como objetivo aprender y practicar las principales estructuras de datos, comenzando con **árboles binarios** y avanzando hacia **grafos**, todo con un enfoque claro, modular y orientado a objetos.

🎯 Ideal para estudiantes de ciencias de la computación, programadores que refuerzan conceptos o quienes preparan entrevistas técnicas.

---

## 📦 Estructuras Implementadas

| Estructura | Estado | Detalles |
|-----------|--------|---------|
| 🌲 Árboles Binarios | ✅ Completado | Inserción, búsqueda, recorridos (inorden, preorden, postorden) |
| 🔄 Listas Enlazadas | ⏳ En progreso | Próximamente |
| 📦 Pilas y Colas | ⏳ En progreso | Próximamente |
| 🌐 Grafos | 🚧 Próximo | DFS, BFS, Dijkstra, etc. |

---

## 🛠️ Tecnologías y Herramientas

- **Python 3** 🐍
- **Git & GitHub** 🌐
- **Zed Editor** ✨
- **Entorno virtual (venv)** 🔒

---

## 🧪 Ejemplo de Uso

```python
from arboles.arbol import Arbol

arbol = Arbol()
valores = [10, 5, 15, 3, 7, 12, 18]

for v in valores:
    arbol.insertar(v)

print("Inorden:", arbol.recorrer_inorden())  # [3, 5, 7, 10, 12, 15, 18]
print("¿Existe 7?", arbol.buscar(7))         # True

estructura_de_datos/
├── main.py                 # Ejecuta todas las pruebas
├── arboles/
│   ├── __init__.py
│   ├── nodo.py             # Clase Nodo con getters y setters
│   └── arbol.py            # Clase Arbol (ABB)
├── venv/                   # Entorno virtual
├── README.md
└── .gitignore              # Archivos ignorados
