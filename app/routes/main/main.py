import logging
import boto3
from flask import Flask, render_template
from app.routes.main import main_routes
from config import basedir
from app.object_wrapper import ObjectWrapper

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/healthcheck')
def health():
    return 'Ok'

@main_routes.route('/s3')
def s3():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket("three-tier-storage-app-development")

    listed_files = ObjectWrapper.list(bucket, "Screenshot")
    return f"Their keys are: {', '.join(l.key for l in listed_files)}"
