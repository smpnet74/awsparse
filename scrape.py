from lxml import html
import requests

page = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json', verify=False)
tree = html.fromstring(page.content)

#zlib1g-dev libxml2