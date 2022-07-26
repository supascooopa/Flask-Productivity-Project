import boto3
import os


def file_getter(bucket_key):
    """ gets a specified file from s3 bucket """
    # --- credentials for s3 connection --- #
    s3 = boto3.resource(
                        service_name="s3",
                        region_name="us-west-1",
                        aws_access_key_id=os.environ.get("ACCESS_KEY"),
                        aws_secret_access_key=os.environ.get("SECRET_KEY")
                        )
    # --- accessing desired bucket --- #
    bucket = s3.Bucket("blue-cell-folder")
    # --- GETTING FILE FROM S3 ---#
    obj = bucket.Object(bucket_key).get()
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
    obj = s3.Bucket("blue-cell-folder")
    obj.upload_file(file, bucket_key)


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
