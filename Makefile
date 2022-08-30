clean-gocd-setup-1:
	echo "cleaning old certs..."
	rm -rf ./gocd-1/roles/gocd_agent/gocd.example.com.crt
	rm -rf ./gocd-1/roles/gocd_agent/gocd.example.com.key
	rm -rf ./gocd-1/roles/gocd_server/gocd.example.com.crt
	rm -rf ./gocd-1/roles/gocd_server/gocd.example.com.key
	rm -rf ./gocd-1/roles/gocd_agent/files/id_rsa
	rm -rf ./gocd-1/deploy_keys/id_rsa.pub


init-setup-gocd-1: clean-gocd-setup-1
	sh ./gocd-1/cnf/generate_csr.sh
	sh ./gocd-1/deploy_keys/generate_key.sh
	mv id_rsa ./gocd-1/roles/gocd_agent/files/
	mv id_rsa.pub ./gocd-1/deploy_keys/

start-gocd-1:
	cd gocd-1 && vagrant up --provision && cd -

stop-gocd-1:
	cd gocd-1 && vagrant destroy -f && cd - 

gocd-status-1:
	cd gocd-1 && vagrant status && cd - 


clean-gocd-setup:
	echo "cleaning old certs..."
	rm -rf ./gocd/roles/gocd_agent/gocd.example.com.crt
	rm -rf ./gocd/roles/gocd_agent/gocd.example.com.key
	rm -rf ./gocd/roles/gocd_server/gocd.example.com.crt
	rm -rf ./gocd/roles/gocd_server/gocd.example.com.key
	rm -rf ./gocd/roles/gocd_agent/files/id_rsa
	rm -rf ./gocd/deploy_keys/id_rsa.pub


init-setup-gocd: clean-gocd-setup
	sh ./gocd/cnf/generate_csr.sh
	sh ./gocd/deploy_keys/generate_key.sh
	mv id_rsa ./gocd/roles/gocd_agent/files/
	mv id_rsa.pub ./gocd/deploy_keys/

start-gocd:
	cd gocd && vagrant up --provision && cd -

stop-gocd:
	cd gocd && vagrant destroy -f && cd - 

gocd-status:
	cd gocd && vagrant status && cd - 

start-gittea:
	docker-compose -f ./gittea/docker-compose.yml up -d --remove-orphans
stop-gittea:
	docker-compose -f ./gittea/docker-compose.yml down --remove-orphans

start-prom:
	docker-compose -f ./prometheus/docker-compose.yml up -d --remove-orphans
stop-prom:
	docker-compose -f ./prometheus/docker-compose.yml down --remove-orphans

generate-gocd-encrypt-git-pass:
	curl 'http://192.168.56.11:8153/go/api/admin/encrypt' -u 'goadmin:goadmin' -H 'Accept: application/vnd.go.cd.v1+json' -H 'Content-Type: application/json' -X POST -d '{ "value": "gittea" }'