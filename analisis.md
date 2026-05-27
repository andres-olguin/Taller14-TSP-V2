
```markdown
# Análisis Técnico: Backtracking y Poda

### Pseudocódigo

```text
Funcion Resolver(ciudad_actual, contador, costo_actual):
    Si contador == n y existe camino al inicio:
        Actualizar distancia_minima si costo_actual < distancia_minima
        Retornar
    
    Para cada ciudad vecina:
        Si no visitada y costo_actual + distancia < distancia_minima:
            Marcar visitada
            Resolver(siguiente, contador + 1, costo_actual + distancia)
            Desmarcar visitada

```

### Análisis de Complejidad

* **Complejidad Temporal:** O(n^2 * 2^n) debido a la poda de ramas innecesarias.
* **Complejidad Espacial:** O(n) para la pila de recursión.

### Representación Matemática del Costo

$$ min \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} d_{ij} x_{ij} $$

Donde d_{ij} representa la distancia entre la ciudad i y la ciudad j, y x_{ij} es una variable binaria que indica si se recorre el arco entre ellas.

```

