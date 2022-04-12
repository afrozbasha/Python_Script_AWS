import boto3

aws_mag_con=boto3.session.Session(profile_name="s3_dev")
s3_cons=aws_mag_con.resource('s3')

for each_bucket in s3_cons.buckets.all():
    print(each_bucket)