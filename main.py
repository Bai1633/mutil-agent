from fastapi import FastAPI
from core.orchestrator import Orchestrator

app = FastAPI()
orc = Orchestrator()

@app.get("/")
def root():
    return {"msg": "Multi-Agent System Running"}

@app.post("/run")
def run(req: str):
    return orc.run(req)
