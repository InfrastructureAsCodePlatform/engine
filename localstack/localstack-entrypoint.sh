#!bin/bash

readonly LOCALSTACK_S3_URL=http://localstack:4566

aws configure set aws_access_key_id AWS_EXAMPLE
aws configure set aws_secret_access_key AWS_EXAMPLE
echo "[default]" > ~/.aws/config
echo "region = us-east-1" >> ~/.aws/config
echo "output = json" >> ~/.aws/config

aws s3 mb s3://harakiri-bucket --endpoint-url $LOCALSTACK_S3_URL
s3api put-bucket-acl --bucket harakiri-bucket --acl public-read
