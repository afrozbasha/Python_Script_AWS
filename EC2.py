import boto3
from pprint import pprint

aws_mag_con=boto3.session.Session(profile_name="ec2_dev")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="ap-south-1")

response=ec2_con_cli.describe_instances()['Reservations']

""" Describe EC2 Instances """
for each_item in response:
    for each in each_item['Instances']:
        print(" ImageId: {}\n InstanceId: {}\n InstanceType: {}\n Instance Lanch Time is: {}\n Instance State: {}\n"
              .format(each['ImageId'], each['InstanceId'], each['InstanceType'], each['LaunchTime'].strftime("%y-%m-%d"), each['State']['Name']))




""" Describe EC2 Instances """
response = ec2_con_cli.describe_volumes()['Volumes']
for each_item in response:
    print(" VolumeId is: {}\n AvailabilityZone: {}\n VolumeType: {}\n"
          .format(each_item['VolumeId'], each_item['AvailabilityZone'], each_item['VolumeType']))
