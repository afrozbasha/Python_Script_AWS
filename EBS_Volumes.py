import boto3

aws_mag_con = boto3.session.Session(profile_name="ec2_dev")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="ap-south-1")


"""  EBS Volumes """
# for each_volume in ec2_con_re.volumes.all():
#     print(each_volume.id, each_volume.state)

filter_ebs_unused = {"Name": "status", "Values": ["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[filter_ebs_unused]):
    print(each_volume.id, each_volume.state)


ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="ap-south-1")
for each_volume in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_volume and each_volume['State']=='available':
        print('Deleting', each_volume['VolumeId'])
        ec2_con_cli.delete_volume(VolumeId=each_volume['VolumeId'])
print("Delete all unused and untagged volumes.")