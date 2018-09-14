# Search for an IP on your Route53 zones
To use this script, define an environment variable *AWS_ACCESS_KEY* with your `aws_access_key_id` and *AWS_SECRET_KEY* with your `aws_secret_access_key`.

Then run the script passing the IP your looking for as first argument:

```BASH
  python route53.py 192.168.0.100
```

The script will loop over all available zones in AWS Route53 and print the records when match with your IP.