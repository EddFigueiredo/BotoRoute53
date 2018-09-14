import boto3
import json
import os
import sys

client = boto3.client(
  'route53',
  aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
  aws_secret_access_key = os.environ["AWS_SECRET_KEY"]
)

response = client.list_hosted_zones()

def searchResourceRecords(ResourceRecordSets, valueToSearch):
  for record in ResourceRecordSets:
    if 'ResourceRecords' in record:
      for value in record['ResourceRecords']:
        if value['Value'] == valueToSearch:
          print(record['Name'])

for zone in response['HostedZones']:
  print('Searching zone: ' + zone['Name'])
  zone_id = zone['Id'].replace('/hostedzone/', '')
  records = client.list_resource_record_sets(HostedZoneId=zone_id,MaxItems='100')
  while True:
    if not records['IsTruncated']:
      searchResourceRecords(records['ResourceRecordSets'], sys.argv[1])
      break

    searchResourceRecords(records['ResourceRecordSets'], sys.argv[1])
    records = client.list_resource_record_sets(HostedZoneId=zone_id,MaxItems='100',StartRecordName=records['NextRecordName'])



