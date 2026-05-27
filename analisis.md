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

\min \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} d_{ij} x_{ij}

---

### Nombres para tus archivos en GitHub
Para que tu repositorio sea profesional y ordenado (tal como lo pide un alumno de 4to año), usa estos nombres estrictos:

1.  **`README.md`**: El archivo principal que explica el proyecto.
2.  **`analisis.md`**: El archivo donde pusimos el pseudocódigo, la complejidad y el LaTeX.
3.  **`vendedor_viajero_opt.py`**: El código fuente en Python.
4.  **`requirements.txt`**: El archivo que indica que no necesitas librerías externas.
5.  **`LICENSE`**: El archivo estándar que se crea al elegir una licencia (MIT).

**¿Por qué usar ````math` en lugar de `$$`?**
A veces, dependiendo de la configuración del repositorio, `$$` puede ser interpretado como texto plano si no está bien configurado. Usar el bloque ````math` es el estándar más robusto en GitHub para asegurar que el LaTeX se renderice correctamente en cualquier computadora.

¡Dale con ese nombre y estructura y el repositorio quedará impecable! ¿Vamos con la versión 3 o prefieres revisar algo más?
