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

# gocd default

GOCD_HOST= 'http://192.168.56.11:8153/'
GOCD_TOKEN= 'c304b8b373edf3dd3c287fedda44e13cb15757f3'
GOCD_HEADER = {
    'Authorization':  f'bearer {GOCD_TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT="http://10.0.2.2:3000"

# gocd 1

GOCD_HOST_1= 'http://192.168.57.11:8153/'
GOCD_TOKEN_1= '2db0715dfbb438baa5f5687c16fae3b248e6f772'
GOCD_HEADER_1 = {
    'Authorization':  f'bearer {GOCD_TOKEN_1}',
    "Content-Type" : "application/json",
    "accept": "application/vnd.go.cd.v4+json" 
}
GIT_HOST_FROM_VAGRANT_1="http://10.0.2.2:3000"