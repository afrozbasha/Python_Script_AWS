import boto3

session = boto3.Session(
    aws_access_key_id='AKIA3QD7QS3TPY5IL376',
    aws_secret_access_key='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'
)

s3 = session.resource('s3')
my_bucket = s3.Bucket('afroz-s3')
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
