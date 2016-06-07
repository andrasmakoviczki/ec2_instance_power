import json
import collections
import boto3
ec2 = boto3.resource('ec2','eu-west-1')

def ec2Status(instanceid):
    instance = ec2.Instance('i-a51cac29')
    return instance.state['Name']


def ec2Info(instanceid):
    instance = ec2.Instance(instanceid)
    instanceInfo = collections.OrderedDict()
    instanceInfo['GroupName'] = instance.tags[0]['Key']
    instanceInfo['InstanceName'] = instance.tags[0]['Value']
    instanceInfo['Type'] = instance.instance_type
    instanceInfo['Status'] = instance.state['Name']
    instanceInfo['Private DNS'] = instance.private_dns_name
    instanceInfo['Public DNS'] = instance.public_dns_name
    instanceInfo['Private IP'] = instance.private_ip_address
    instanceInfo['Public IP'] = instance.public_ip_address
    return instanceInfo


def ec2PowerOn(instanceid):
    instance = ec2.instances.filter(InstanceIds=[instanceid]).start()
    return instance


def ec2PowerOff(instanceid):
    instance = ec2.instances.filter(InstanceIds=[instanceid]).stop()
    return instance

def checkId(instanceId):
    path = os.path.join(os.path.dirname(__file__), '../private/instances.txt')
    with open(path) as f:
       content = f.read().splitlines()

    for i in content:
        if i == instanceId:
            return True

    print "not find"
    return False