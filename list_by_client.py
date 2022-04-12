import	boto3

aws_mag_con=boto3.session.Session(profile_name="root")
iam_con_cli=aws_mag_con.client(service_name="iam", region_name="ap-south-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="ap-south-1")
s3_con_cli=aws_mag_con.client(service_name="s3", region_name="ap-south-1")

"""Listing iam users with client object"""
# response = iam_con_cli.list_users()
# for each_item in response['Users']:
# 	print(each_item['UserName'])
#

"""Listing ec2 Instances with client object"""
# response=ec2_con_cli.describe_instances()
# for each_item in response['Reservations']:
#     for each_instance in each_item['Instances']:
#         print(each_instance)
# #print(response)


"""Listing s3 Buckets with client object"""
# response = s3_con_cli.list_buckets()
# for each_item in response['Buckets']:
#     print(each_item['Name'])

"""Listing s3 Bucket objects with client object"""
# response = s3_con_cli.list_objects_v2(Bucket='afroz-s3')
# for obj in response['Contents']:
#     print(obj['Key'])
