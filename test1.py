import urllib.request
url = 'https://hcmuni.fpt.vn'

try:
    urllib.request.urlopen(url)
except ValueError:
    print('False')
