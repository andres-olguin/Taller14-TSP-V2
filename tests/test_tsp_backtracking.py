import unittest

from src.tsp_backtracking import solve_tsp


class BacktrackingTests(unittest.TestCase):
    def test_known_four_city_instance(self):
        matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        result = solve_tsp(matrix)
        self.assertEqual(result["cost"], 80)
        self.assertEqual(result["route"][0], 0)
        self.assertEqual(result["route"][-1], 0)
        self.assertEqual(set(result["route"][:-1]), set(range(4)))

    def test_two_cities(self):
        self.assertEqual(solve_tsp([[0, 3], [7, 0]])["cost"], 10)

    def test_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            solve_tsp([[0, -1], [2, 0]])

    def test_rejects_nonsquare(self):
        with self.assertRaises(ValueError):
            solve_tsp([[0, 1], [1]])

    def test_rejects_large_instance(self):
        with self.assertRaises(ValueError):
            solve_tsp([[0] * 11 for _ in range(11)])


if __name__ == "__main__":
    unittest.main()
