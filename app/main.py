from fastapi import FastAPI

app = FastAPI(title="Sigma API")

@app.get("/")
def read_root():
    return "Sigma API"