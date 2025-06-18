import numpy as np
from creatoria_core.robust_qubo import generate_robust_qubo

def test_qubo():
    params = np.array([1.0, 2.0, 3.0])
    Q = generate_robust_qubo(params, tolerance=0.2, scenarios=100)
    print("✅ QUBO matrix generated:\n", Q)  # 👈 ЭТО и добавляет вывод

if __name__ == "__main__":
    test_qubo()
