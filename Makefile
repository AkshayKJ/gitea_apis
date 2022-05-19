init-setup-gocd:
	sh ./gocd/cnf/generate_csr.sh
	sh ./gocd/deploy_keys/generate_key.sh
	mv id_rsa ./gocd/roles/gocd_agent/files/
	mv id_rsa.pub ./gocd/deploy_keys/

start-gocd:
	cd gocd && vagrant up && cd -

start-gittea:
	docker-compose -f ./gittea/docker-compose.yml up -d --remove-orphans
stop-gittea:
	docker-compose -f ./gittea/docker-compose.yml down --remove-orphans