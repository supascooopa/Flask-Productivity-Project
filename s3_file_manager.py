import boto3
import os
from io import BytesIO


def file_getter(bucket_key):
    """ gets a specified file from s3 bucket """
    # --- credentials for s3 connection --- #
    s3 = boto3.resource(
                        service_name="s3",
                        region_name="us-west-1",
                        aws_access_key_id=os.environ.get("ACCESS_KEY"),
                        aws_secret_access_key=os.environ.get("SECRET_KEY"),
    )

    # --- accessing desired bucket --- #
    bucket = s3.Bucket("blue-cell-folder")
    key = bucket_key

    # --- UPLOADING TO A SPECIFIC DIRECTORY IN S3 -- #
    # file_path = os.path.abspath("../Flask-Productivity-Project/static/browser_automation/XL/sample_excel_sheet-2.xlsx")
    # bucket.upload_file(Filename=file_path, Key="browser_automation/excel_sample/excel_sample.xlsx")
    # --- GETTING FILE FROM S3 ---#
    obj = bucket.Object(key).get()
    return obj['Body'].read()


def file_uploader(file, bucket_key):

    # --- credentials for s3 connection --- #
    s3 = boto3.resource(
                        service_name="s3",
                        region_name="us-west-1",
                        aws_access_key_id=os.environ.get("ACCESS_KEY"),
                        aws_secret_access_key=os.environ.get("SECRET_KEY"),
    )
    # --- UPLOADING TO A SPECIFIC DIRECTORY IN S3 -- #
    obj = s3.Object("blue-cell-folder", bucket_key)
    obj.put(Body=file)


def file_downloader(bucket_key):
    # --- credentials for s3 connection --- #
    s3 = boto3.resource(
                        service_name="s3",
                        region_name="us-west-1",
                        aws_access_key_id=os.environ.get("ACCESS_KEY"),
                        aws_secret_access_key=os.environ.get("SECRET_KEY"),
    )
    bucket = s3.Bucket("blue-cell-folder")
    key = bucket_key
    return bucket.Object(key).get()



