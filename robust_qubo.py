
import numpy as np

def generate_robust_qubo(params, tolerance=0.1, scenarios=100):
    """Генерация QUBO с учётом неопределённостей."""
    n = len(params)
    Q = np.zeros((n, n))
    samples = np.random.normal(loc=params, scale=tolerance*np.abs(params), size=(scenarios, n))
    for sample in samples:
        for i in range(n):
            Q[i][i] += sample[i] ** 2
        for i in range(n):
            for j in range(i+1, n):
                Q[i][j] += sample[i] * sample[j]
                Q[j][i] = Q[i][j]
    Q /= scenarios
    return Q
