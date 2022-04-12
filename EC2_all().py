import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name="ap-south-1")

f1={"Name": "instance-state-name", "Values" : ['running', 'stopped']}
f2={"Name": "instance-type", "Values" : ['t2.micro']}

# for each in ec2_con_re.instances.all():
#     print(each)

for each in ec2_con_re.instances.filter(Filters=[f1, f2]):
    print(each)