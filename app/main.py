from fastapi import FastAPI

app = FastAPI(
    title="Valerianich",
    description="Private messenger for two",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Valerianich is running!"}
