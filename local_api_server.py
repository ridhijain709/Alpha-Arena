import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mochatrade Alpha Arena Local API",
    description="Local metrics API engine for Power BI / frontend dashboard integration",
    version="1.0.0"
)

# Enable CORS for local dashboards / browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/metrics")
def get_metrics():
    return {
        "status": "success",
        "campaign": "Mochatrade Alpha Arena",
        "metrics": {
            "reengagement_rate": 42.5,
            "viral_k_factor": 1.45,
            "blended_cac_inr": 240,
            "active_referral_refills": 384,
            "day1_deposit_conversion": 18.2
        }
    }

if __name__ == "__main__":
    uvicorn.run("local_api_server:app", host="127.0.0.1", port=8000, reload=True)
