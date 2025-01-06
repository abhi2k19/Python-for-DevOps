#--------Dictionary---------

ec2_instances = {
           'name': ["demo_01", "demo_02"],
           'type': ["t2.micro", "t2.small"],
           'state': ["running", "stopped"],
           'region': ["us-east-1", "us-east-2"]
           }

s3_buckets = [
          {
           'name': "bucket_01", 
           'type':"standard",
           'region':"us-east-1"
           },
          {
           'name': "bucket_01",
           'type':"standard",
           'region': "us-east-2"
           }
]


print(ec2_instances['name'][0])
print(s3_buckets[0]['region'])
print(s3_buckets[1]['region'])