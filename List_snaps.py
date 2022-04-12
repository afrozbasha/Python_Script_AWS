import boto3

from list_by_resource import sts_con_cli

"""  List all Available Snapshots """
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name="ap-south-1")
response=sts_con_cli.get_caller_identity()
my_own_id=response.get('Account')
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    print(each_snap)

""" List snapshots based on size """
f_size={"Name" : "volume-size", "Values" : ['8']}

for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id], Filters=[f_size]):
    print(each_snap)