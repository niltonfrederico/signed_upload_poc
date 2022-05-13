# Proof of Concept

This POC covers AWS Signed Upload and its features.

To get it started run:

`cp .env.example .env`

Add your credentials, and then run:

`make up`

And access [localhost](https://localhost:8000) - Check console logs for more info.

-----

The bucket configuration need to be as follow:

1. You need to add CORS to your bucket

![image](https://user-images.githubusercontent.com/9078708/168342283-96adc89d-ea5e-46a0-9359-2a339dd711f1.png)

2. You **DO NOT** need to give any public access 

![image](https://user-images.githubusercontent.com/9078708/168342471-06127241-ea14-492a-9663-093a7c08bde5.png)

3. You [can follow this guide](https://aws.amazon.com/pt/premiumsupport/knowledge-center/s3-allow-certain-file-types/) to block any file type you do not want at bucket level.
