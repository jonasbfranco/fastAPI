from fastapi import FastAPI

from fast_car_api.routes import router as car_router

app = FastAPI(
    title="Fast Car API",
    description="Jonas Car API", 
    version="0.1.0",
)

app.include_router(car_router)

@app.get("/")
def read_root():
    return {"status": "ok"}