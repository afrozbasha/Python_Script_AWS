import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
iam_con_res=aws_mag_con.resource(service_name="iam", region_name="ap-south-1")
ec2_con_res=aws_mag_con.resource(service_name="ec2", region_name="ap-south-1")
s3_con_res=aws_mag_con.resource(service_name="s3", region_name="ap-south-1")

##get account id or number
sts_con_cli=aws_mag_con.client(service_name="sts", region_name="ap-south-1")
response=sts_con_cli.get_caller_identity()
print(response.get('Account'))

# for each_item in iam_con_res.users.all():
#     print(each_item.user_name)

# for each_item in iam_con_res.users.limit(1):
#     print(each_item.user_name)


# for each_item in s3_con_res.buckets.all():
#     print(each_item.name)


# for each_item in s3_con_res.buckets.limit(2):
#     print(each_item.name)


# for each_item in ec2_con_res.classic_addresses.all():
#     print(each_item)

# classic_address_iterator = ec2_con_res.classic_addresses.all()
# for each_item in classic_address_iterator:
#     print(each_item)

