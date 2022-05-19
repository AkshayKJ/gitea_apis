HOST='http://localhost:3000'
USER_NAME='gittea'
PASSWORD='gittea'
TOKEN='ec54b83ae911ecbc61c6c3e06aa3515c2f845884'
GOCD_TOKEN= 'c46943e4a64c8864adfd35616cf79e21aa2ebabb'
GOCD_HOST= 'http://192.168.56.11:8153/'

HEADER = {
    'Authorization': f'token {TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/json" 
}
GOCD_HEADER = {
    'Authorization':  f'bearer {GOCD_TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}