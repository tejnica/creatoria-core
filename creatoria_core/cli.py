
import sys
import numpy as np
from creatoria_core.robust_qubo import generate_robust_qubo
from creatoria_core.pareto_solver import fast_non_dominated_sort

def main():
    print("Creatoria CLI started")
    if len(sys.argv) < 2:
        print("Usage: creatoria_cli run")
        return

    if sys.argv[1] == "run":
        print("Generating QUBO matrix...")
        params = [1.0, 0.8, 1.2]
        Q = generate_robust_qubo(params)
        print("QUBO matrix:")
        print(Q)

        print("\nEvaluating solutions (simulation placeholder)...")
        population = np.random.rand(10, 3)
        fronts = fast_non_dominated_sort(population)

        print("Pareto fronts:")
        for i, front in enumerate(fronts):
            print(f"Front {i+1}: {front}")

if __name__ == "__main__":
    main()
