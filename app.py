import boto3
from environs import Env
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Signed Upload POC")

# Environment Variables
env = Env()
env.read_env()
S3_BUCKET = env.str("S3_BUCKET")


s3_client = boto3.client("s3")

# Schemas
class Obj(BaseModel):
    object_name: str


# Endpoints
@app.post("/generate-signed-url")
def generate_upload_signed_url(obj: Obj):
    url = s3_client.generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": S3_BUCKET, "Key": obj.object_name},
        ExpiresIn=3600,
    )

    return {"upload_url": url}
