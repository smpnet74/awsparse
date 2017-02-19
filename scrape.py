from lxml import html
import requests
import json

lookforwhat = "us-west-1"
page = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
tree = html.fromstring(page.content)
parsed_json = json.loads(page.text)
for each in parsed_json['prefixes']:
    if each['region'] == lookforwhat:
        print (each['ip_prefix'])