import boto3
from environs import Env
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Environment Variables
env = Env()
env.read_env()
S3_BUCKET = env.str("S3_BUCKET")


s3_client = boto3.client("s3")

# App
app = FastAPI(title="Signed Upload POC")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Schemas
class Obj(BaseModel):
    object_name: str


# Endpoints
@app.post("/generate-signed-url")
def generate_upload_signed_url(obj: Obj):
    url = s3_client.generate_presigned_post(
        Bucket=S3_BUCKET,
        Key=obj.object_name,
        ExpiresIn=3600,
    )

    return {"upload_url": url}
