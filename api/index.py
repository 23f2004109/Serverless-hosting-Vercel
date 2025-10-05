from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from typing import List, Dict, Any
import json

app = FastAPI()

# Enable CORS for POST requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/api/latency")
async def analyze_latency(request: Dict[str, Any]):
    regions = request.get("regions", [])
    threshold_ms = request.get("threshold_ms", 180)
    
    # Load your telemetry data (you need to upload this)
    # For now, using sample structure
    df = pd.read_csv("telemetry_bundle.csv") 
    
    result = {}
    
    for region in regions:
        if region in sample_data:
            latencies = sample_data[region]["latencies"]
            uptime = sample_data[region]["uptime"]
            
            result[region] = {
                "avg_latency": np.mean(latencies),
                "p95_latency": np.percentile(latencies, 95),
                "avg_uptime": np.mean(uptime),
                "breaches": sum(1 for lat in latencies if lat > threshold_ms)
            }
    
    return result
