import yaml
import numpy as np
from creatoria_core.robust_qubo import generate_robust_qubo

# Загрузка параметров из YAML
with open("task.yaml", "r") as f:
    data = yaml.safe_load(f)

# Пример: task.parameters.vector = [1.0, 2.5, 0.7]
params = data["task"]["parameters"]["vector"]
Q = generate_robust_qubo(np.array(params), tolerance=0.1, scenarios=100)

print("✅ Матрица Q:")
print(Q)