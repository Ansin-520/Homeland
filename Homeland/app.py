from fastapi import FastAPI

app = FastAPI(title="Homeland", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Welcome to Homeland"}


@app.get("/health")
def health():
    return {"status": "ok"}
