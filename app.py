from fastapi import FastAPI

app = FastAPI(title="Signed Upload POC")


@app.get("/generate-signed-url")
def generate_signed_url():
    ...


@app.get("/upload")
def upload():
    ...
