DOCKER_NAME = awslib
ALIAS_FILE = ~/.alias_config
PROFILE_FILE = ~/.bash_profiles

build:
	docker build -t $(DOCKER_NAME) .

setup_docker: build
	printf 'alias awslib="docker run --rm --' >> $(ALIAS_FILE)
	printf 'env-file <(env | grep AWS) -' >> $(ALIAS_FILE)
	printf 'v ~/.aws:/aws/.aws -' >> $(ALIAS_FILE)
	printf 'v `pwd`:/aws/local -' >> $(ALIAS_FILE)
	printf 'v /:/aws/absolute -' >> $(ALIAS_FILE)
	printf 'e IAM_ROLE=$$AWS_DEFAULT_ROLE ' >> $(ALIAS_FILE)
	printf "$(DOCKER_NAME)\"\n" >> $(ALIAS_FILE)

setup_host: requirements.txt $(ALIAS_FILE)
	pip3 install --user -r requirements.txt
	printf "alias awslib=\"`pwd`/awslib\"\n" >> $(ALIAS_FILE)

link_alias:
	printf "source ~/.alias_config\n" >> $(PROFILE_FILE)

.PHONY: build setup_host link_alias
