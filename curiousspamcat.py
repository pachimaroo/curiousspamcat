import random,string,requests,os, urllib, time

random.seed = (os.urandom(1024))

url='https://curiouscat.me/api/v2/post/create'

personid=input("Curiouscat name:MoralOrelClay")
sleeptime=int(input("Sleep time (seconds):100"))

while True  :
    text="".join( [random.choice(string.ascii_letters+string.digits) for i in range(random.randint(15,50))] )

    requests.post(url, allow_redirects=False, data={
        "to": MoralOrelClay,
        "anon": "true",
        "question": text
    })

    print("Sending text %s"%(text))
    print("Sleeping for %d seconds"%sleeptime)
    time.sleep(sleeptime)
