HOST='http://localhost:3000'
USER_NAME='admin123'
PASSWORD='admin@123'
TOKEN='cc6a3a8733fd412673a58f15cf75f605ced86cef'
GOCD_TOKEN= 'c46943e4a64c8864adfd35616cf79e21aa2ebabb'


# https://try.gitea.io/

# HOST='https://try.gitea.io'
# USER_NAME='ishnmu'
# PASSWORD=''
# TOKEN='79fd165ae59ea0bea56c7d22c0aef7a6be303428'


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

GOCD_HOST= 'http://192.168.199.11:8153/'