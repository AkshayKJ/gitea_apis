HOST='http://localhost:3000'
USER_NAME='gittea'
PASSWORD='gittea'
TOKEN='ec54b83ae911ecbc61c6c3e06aa3515c2f845884'
GOCD_TOKEN= 'aa6600af97f73ecf59f92e9c3de0a43daa1d4959'
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

FROM=1
LESS_THAN=50