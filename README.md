# TSP Backtracking Lab — Vendedor viajero con poda

**Laboratorio académico de algoritmos** sobre el *Travelling Salesperson Problem* (TSP). Esta versión amplía la búsqueda exacta de rutas mediante **backtracking con poda por costo parcial**, conservando la comparación conceptual con [`tsp-bruteforce-lab`](https://github.com/andres-olguin/tsp-bruteforce-lab).

**Autores del trabajo académico original:** Andrés Olguín, Maximiliano Valdés y Enrique Chamy.

> **Estado:** algoritmo educativo exacto para instancias pequeñas, con pruebas automáticas. No es un optimizador de rutas productivo ni garantiza mejor tiempo que fuerza bruta para todos los casos.

## Qué hace

Dada una matriz cuadrada con distancias **finitas y no negativas**, busca un ciclo que parte de la ciudad `0`, visita una vez cada otra ciudad y vuelve al origen. Recorre rutas recursivamente y descarta ramas cuya suma parcial ya iguala o supera el mejor costo encontrado.

**Limitación:** la poda actual utiliza solamente el mejor costo parcial; **no incluye un bound inferior sofisticado**. En el peor caso sigue explorando un número **factorial O(n!)** de alternativas.

## Inicio rápido

Requiere Python 3.10+ y solamente biblioteca estándar.

```bash
python -m src.tsp_backtracking
python -m unittest discover -s tests -v
```

La primera instrucción resuelve una instancia de cuatro ciudades con costo óptimo conocido `80`. El ejemplo imprime el ciclo encontrado, el costo, los nodos de búsqueda visitados y las ramas podadas.

## Uso desde código

```python
from src.tsp_backtracking import solve_tsp

distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
resultado = solve_tsp(distancias)
print(resultado["route"], resultado["cost"])
```

El límite inicial es **10 ciudades** para evitar ejecuciones accidentales excesivamente costosas.

## Estructura

| Archivo | Responsabilidad |
|---|---|
| [`src/tsp_backtracking.py`](src/tsp_backtracking.py) | Solver exacto con poda y métricas de exploración |
| [`tests/test_tsp_backtracking.py`](tests/test_tsp_backtracking.py) | Casos conocidos, límites y errores de entrada |
| [`analisis.md`](analisis.md) | Fundamentos, pseudocódigo y complejidad |
| [`docs/index.html`](docs/index.html) | Demo visual didáctica independiente |
| [`.github/workflows/python-tests.yml`](.github/workflows/python-tests.yml) | Pruebas automáticas CI |

La demostración HTML no garantiza usar el mismo motor Python; comparar su comportamiento antes de publicar equivalencias.

## Evolución y evaluación

1. Comparar resultados con el solver exacto de fuerza bruta usando las mismas matrices.
2. Introducir límites inferiores válidos más fuertes y contar nodos por estrategia.
3. Repetir benchmarks con semillas y tamaños documentados, evitando presentar rapidez simulada como medida.
4. Incorporar heurísticas como alternativas no necesariamente óptimas para instancias mayores.
5. Documentar casos adversos donde la poda simple no logra una mejora relevante.

[Estudio de evolución](docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md) · [Escalabilidad](docs/ARCHITECTURE_SCALABILITY_2026-11-04.md).

**Créditos y titularidad:** material académico con coautoría. Preservar historia y permisos antes de reutilización comercial.
