from fastapi import FastAPI
from api.routes.clinicas_route import router as clinicas_router
app = FastAPI()

app.include_router(clinicas_router, prefix="/clinicas", tags=["Clinicas"])

@app.get("/")
def home():
    return {"message": "Welcome to the Clinicas API"}
