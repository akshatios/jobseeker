from fastapi import FastAPI
from core.routers import include_routers

app = FastAPI(title="Job Portal API", version="1.0.0")

include_routers(app)

@app.get("/")
def root():
    return {"message": "Job Portal API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)