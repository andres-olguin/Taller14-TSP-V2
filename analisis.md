# Análisis técnico — Backtracking y poda para TSP

**Objetivo:** encontrar el ciclo de menor costo que sale de la ciudad 0, visita las demás exactamente una vez y vuelve al inicio.

## Pseudocódigo

```text
mejor_costo = infinito
mejor_ruta = ninguna
explorar(ruta=[0], visitadas={0}, costo=0):
    si costo >= mejor_costo:  // solo para pesos no negativos
        podar
        retornar
    si número_visitadas = n:
        costo_ciclo = costo + distancia[última][0]
        si costo_ciclo < mejor_costo:
            actualizar mejor_costo y mejor_ruta
        retornar
    para cada ciudad no visitada:
        explorar(ruta + ciudad, visitadas + ciudad, costo + distancia[última][ciudad])
```

## Complejidad

- **Peor caso temporal:** O(n!) recorridos parciales, con factores adicionales por construcción de rutas y conjuntos.
- **Profundidad de recursión:** O(n). La implementación de referencia crea rutas/conjuntos parciales nuevos, por lo que su memoria total en una rama supera un esquema in-place; no afirmar O(n) de memoria total sin esa salvedad.
- **Poda:** puede reducir sustancialmente las ramas cuando se identifica temprano una ruta de bajo costo, pero **no cambia el peor caso factorial**.
- **Correctitud:** requiere distancias finitas y no negativas para justificar la poda por costo parcial.

## Verificación

```bash
python -m src.tsp_backtracking
python -m unittest discover -s tests -v
```

Para estudiar eficiencia real, fijar dataset, algoritmo de referencia y entorno; reportar tiempo, memoria, nodos explorados y nodos podados por repetición. Comparar con [tsp-bruteforce-lab](https://github.com/andres-olguin/tsp-bruteforce-lab).

**Autoría académica:** Andrés Olguín, Maximiliano Valdés y Enrique Chamy.
