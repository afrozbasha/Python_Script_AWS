import boto3

aws_mag_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="ap-south-1")
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name="ap-south-1")

all_instances_ids = []
for each_in in ec2_con_re.instances.all():
    all_instances_ids.append(each_in.id)

""" Starting all instances """
# waiter = ec2_con_cli.get_waiter('instance_running')
# print("Starting all instances ...")
# ec2_con_re.instances.start()
# waiter.wait(InstanceIds=all_instances_ids)
# print("your all instances are up and running")


""" Starting AWS instances """
ser_ids = []
f1 = {"Name": "tag:Name", "Values": ['AWS']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    for each_in in each_item['Instances']:
        ser_ids.append(each_in['InstanceId'])
print(ser_ids)

print("Starting instances with ids of : ",ser_ids)
waiter=ec2_con_cli.get_waiter('instance_running')
ec2_con_cli.start_instances(InstanceIds=ser_ids)
waiter.wait(InstanceIds=ser_ids)
print("Your AWS instances are up and running...")