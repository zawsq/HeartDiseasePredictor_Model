from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/practice")
def predict():
    return 'rawrerfou'



if __name__ == "__main__":
    uvicorn.run(
        "deployment.Api.app:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True
    )










