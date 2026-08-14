import json
import boto3
import pymysql

SECRET_NAME = "myapp/rds/credentials"
AWS_REGION = "us-east-1"

RDS_HOST = "database-1.ckb8usqysdhc.us-east-1.rds.amazonaws.com"
RDS_PORT = 3306


def get_secret():

    client = boto3.client(
        "secretsmanager",
        region_name=AWS_REGION
    )

    response = client.get_secret_value(
        SecretId=SECRET_NAME
    )

    return json.loads(response["SecretString"])


secret = get_secret()

connection = pymysql.connect(
    host=RDS_HOST,
    port=RDS_PORT,
    user=secret["username"],
    password=secret["password"]
)

print("Connected to RDS successfully!")

connection.close()
