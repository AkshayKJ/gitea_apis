HOST='http://localhost:3000'
USER_NAME='gittea'
PASSWORD='gittea'
TOKEN='ec54b83ae911ecbc61c6c3e06aa3515c2f845884'
GOCD_TOKEN= '2b4ea4d3e8c6ca0f442c83404a486db66c0da9c1'
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

GIT_HOST_FROM_VAGRANT="http://10.0.2.2:3000"

FROM=0
LESS_THAN=1