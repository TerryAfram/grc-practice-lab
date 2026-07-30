from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/metrics")
def get_metrics():
    return {
        "controls": 142,
        "threats": "10,248",
        "latency": "14ms",
        "benchmark": "ISO / NIST - Passed"
    }
