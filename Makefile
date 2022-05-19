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
	cd gocd && vagrant up && cd -

stop-gocd:
	cd gocd && vagrant destroy -f && cd - 

start-gittea:
	docker-compose -f ./gittea/docker-compose.yml up -d --remove-orphans
stop-gittea:
	docker-compose -f ./gittea/docker-compose.yml down --remove-orphans

start-prom:
	docker-compose -f ./prometheus/docker-compose.yml up -d --remove-orphans
stop-prom:
	docker-compose -f ./prometheus/docker-compose.yml down --remove-orphans

start-grafana:
	docker-compose -f ./grafana/docker-compose.yml up -d --remove-orphans
stop-grafana:
	docker-compose -f ./grafana/docker-compose.yml down --remove-orphans