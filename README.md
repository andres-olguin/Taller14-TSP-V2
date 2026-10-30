# Taller 14 - El Vendedor Viajero (Versión Optimizada)

**Integrantes:** Andrés Olguín, Maximiliano Valdés, Enrique Chamy.
**Versión:** 2.0 (Optimización mediante Backtracking)

### Descripción
A diferencia de la versión base (fuerza bruta), esta iteración utiliza un algoritmo de **Backtracking con Poda**. Esto permite descartar ramas de búsqueda que ya superan el costo mínimo encontrado, mejorando drásticamente el rendimiento en comparación con el cálculo factorial puro.

### 1. ¿En qué consiste?
Buscamos la ruta más corta visitando cada ciudad una sola vez y regresando al inicio, pero aplicando una estrategia de búsqueda más inteligente.

### 2. Problema de decisión
¿Existe una ruta con costo total $C \leq K$?

### 3. Clase
NP-Completo.

### 4. Aplicaciones
* Optimización de rutas de logística urbana.
* Planificación de mantenimiento de redes de sensores.
* Secuenciación de tareas en líneas de montaje.


## Demostración web (frontend propio)

Se incorporó una [interfaz experimental en docs/index.html](docs/index.html) que puede utilizarse como fuente de GitHub Pages. **No se ha confirmado aún la activación ni la URL pública de GitHub Pages.**

Para publicarla, configurar GitHub Pages con rama main y carpeta /docs, verificar el sitio y agregar su URL comprobada a la sección About del repositorio. La interfaz es una adaptación o visualización didáctica; consultar sus límites en la propia página.

[Estudio de evolución y requisitos de seguridad](docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md).
