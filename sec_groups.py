#!/usr/bin/env python2.7

import boto.ec2
import argparse

def findSecGroup(sg_id): #obtaining an object with security group details by sec group id
    return conn.get_all_security_groups(group_ids=[sg_id])[0]

#Parsing command line args. Usage example: python2.7 ./sec_groups.py sg-45b9a12c eu-central-1
parser = argparse.ArgumentParser(description="Validate security rules of instances which belong to given security group")
parser.add_argument('sec_group_id', help='Security group id')
parser.add_argument('region_name', help='Region name')
args = parser.parse_args()
sec_group_id = args.sec_group_id
region_name = args.region_name

conn = boto.ec2.connect_to_region(region_name);

GivenSecGroup=findSecGroup(sec_group_id)
print("Given security group id:\t" + GivenSecGroup.id + "\t Given security group name:\t" + GivenSecGroup.name+"\nRules:")
print(GivenSecGroup.rules)
print("-------------------------------------------\n")

for I in GivenSecGroup.instances():
    print(I)
    for SecGroup in I.groups:
        SecGroup=findSecGroup(SecGroup.id)
        print("Security group id:\t" + SecGroup.id + "\t Security group name:\t" + SecGroup.name+"\nRules:")
        print(SecGroup.rules)
    print("-------------------------------------------\n")
