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
