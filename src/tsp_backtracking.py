"""TSP exacto con backtracking y poda por costo parcial para matrices pequeñas."""
import math


def solve_tsp(matrix, max_cities=10):
    """Busca un ciclo Hamiltoniano mínimo, con origen fijo en el nodo 0.

    No es un algoritmo polinomial: en el peor caso explora O(n!) rutas.
    La poda costo>=mejor es válida solo por pesos no negativos.
    """
    n = len(matrix)
    if not 2 <= n <= max_cities:
        raise ValueError(f"Se requieren 2..{max_cities} ciudades.")
    if any(len(row) != n for row in matrix):
        raise ValueError("La matriz debe ser cuadrada.")
    for row in matrix:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError("Las distancias deben ser numéricas, finitas y no negativas.")

    best_cost = math.inf
    best_route = None
    visited_nodes = 0
    pruned_branches = 0

    def search(path, seen, cost):
        nonlocal best_cost, best_route, visited_nodes, pruned_branches
        visited_nodes += 1
        if cost >= best_cost:
            pruned_branches += 1
            return
        if len(path) == n:
            total = cost + matrix[path[-1]][0]
            if total < best_cost:
                best_cost = total
                best_route = [*path, 0]
            return
        for next_city in range(1, n):
            if next_city not in seen:
                search([*path, next_city], seen | {next_city}, cost + matrix[path[-1]][next_city])

    search([0], {0}, 0)
    return {"route": best_route, "cost": best_cost,
            "visited_nodes": visited_nodes, "pruned_branches": pruned_branches}


if __name__ == "__main__":
    sample = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(solve_tsp(sample))
