FROM=1
LESS_THAN=51

# gittea configs

HOST='http://localhost:3000'
USER_NAME='gittea'
PASSWORD='gittea'
TOKEN='ec54b83ae911ecbc61c6c3e06aa3515c2f845884'
HEADER = {
    'Authorization': f'token {TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/json" 
}

# gocd with git path plugin

GOCD_HOST= 'http://192.168.56.11:8153/'
GOCD_TOKEN= 'aa6600af97f73ecf59f92e9c3de0a43daa1d4959'
GOCD_HEADER = {
    'Authorization':  f'bearer {GOCD_TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT="http://10.0.2.2:3000"

# gocd with build in material plugin

GOCD_HOST_1= 'http://192.168.57.11:8153/'
GOCD_TOKEN_1= '929a45db39c48d57ddb644092aa54f923824a2c4'
GOCD_HEADER_1 = {
    'Authorization':  f'bearer {GOCD_TOKEN_1}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT_1="http://10.0.2.2:3000"