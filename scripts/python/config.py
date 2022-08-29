FROM=1
LESS_THAN=5

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

# gocd default

GOCD_HOST= 'http://192.168.56.11:8153/'
GOCD_TOKEN= 'ea735fdf1586bc2e3a9d70b847cbde513585bb52'
GOCD_HEADER = {
    'Authorization':  f'bearer {GOCD_TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT="http://10.0.2.2:3000"

# gocd 1

GOCD_HOST_1= 'http://192.168.57.11:8153/'
GOCD_TOKEN_1= '3272d54fbb212b001373d916d4000e370decaa6f'
GOCD_HEADER_1 = {
    'Authorization':  f'bearer {GOCD_TOKEN_1}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT_1="http://10.0.2.2:3000"