import logging
import boto3
import requests
from flask import Flask, render_template
from app.routes.main import main_routes
from config import basedir
from app.object_wrapper import ObjectWrapper

@main_routes.route('/')
def index():
    instance_id = get_ec2_instance_id_from_within()
    return render_template('index.html', instance_id=instance_id)

@main_routes.route('/healthcheck')
def health():
    return 'Ok'

@main_routes.route('/s3')
def s3():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket("tofu-multi-env-storage-app-development")

    listed_files = ObjectWrapper.list(bucket, "Screenshot")
    return f"Their keys are: {', '.join(l.key for l in listed_files)}"

def get_ec2_instance_id_from_within():
    """Retrieves the EC2 instance ID from within the instance."""
    try:
        # For IMDSv2, first get a token
        token_url = "http://169.254.169.254/latest/api/token"
        token_headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        token_response = requests.put(token_url, headers=token_headers)
        token_response.raise_for_status() # Raise an exception for bad status codes
        token = token_response.text

        # Then use the token to get the instance ID
        instance_id_url = "http://169.254.169.254/latest/meta-data/instance-id"
        instance_id_headers = {"X-aws-ec2-metadata-token": token}
        instance_id_response = requests.get(instance_id_url, headers=instance_id_headers)
        instance_id_response.raise_for_status()
        return instance_id_response.text
    except requests.exceptions.RequestException as e:
        print(f"Error getting EC2 instance ID: {e}")
        return None