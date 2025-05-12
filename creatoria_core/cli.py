
import sys
import numpy as np
from .robust_qubo import generate_robust_qubo
from .pareto_solver import fast_non_dominated_sort

def main():
    print("Creatoria CLI запущен")
    if len(sys.argv) < 2:
        print("Использование: creatoria_cli run")
        return

    if sys.argv[1] == "run":
        print("Создание QUBO...")
        params = [1.0, 0.8, 1.2]
        Q = generate_robust_qubo(params)
        print("QUBO матрица:")
        print(Q)

        print("\nОценка решений (псевдосимуляция)...")
        population = np.random.rand(10, 3)
        fronts = fast_non_dominated_sort(population)
        print("Pareto фронты:")
        for i, front in enumerate(fronts):
            print(f"Фронт {i+1}: {front}")
