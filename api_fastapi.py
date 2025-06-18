# api_fastapi.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from creatoria_core.robust_qubo import generate_robust_qubo

app = FastAPI()

class QuboParams(BaseModel):
    params: list
    tolerance: float = 0.1
    scenarios: int = 100

@app.post("/run_qubo")
def run_qubo(input: QuboParams):
    arr = np.array(input.params)
    Q = generate_robust_qubo(arr, tolerance=input.tolerance, scenarios=input.scenarios)
    return {"qubo": Q.tolist()}