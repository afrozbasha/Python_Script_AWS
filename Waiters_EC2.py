import boto3
import time

aws_con=boto3.session.Session(profile_name="ec2_dev")
ec2_con_re=aws_con.resource(service_name="ec2", region_name="ap-south-1")
ec2_con_cli=aws_con.client(service_name="ec2", region_name="ap-south-1")

my_int_ob=ec2_con_re.Instance("i-0d66e048db4419e18")

# print("Starting given instance ...")
# my_int_ob.start()
# print("Now instance is running")

print("Starting given instance ...")
my_int_ob.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0d66e048db4419e18'])
print("Now instance is running")
