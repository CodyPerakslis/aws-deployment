DOCKER_NAME = aws_lib

build:
	docker build -t $(DOCKER_NAME) .

setup: build
	printf 'alias aws_lib="docker run --rm --env-file <(env | grep AWS) -v ~/.aws:/lib/.aws:ro -v `pwd`:/lib/local ' >> ~/.alias_config
	echo "$(DOCKER_NAME)\"" >> ~/.alias_config

link_alias:
	echo "source ~/.alias_config" >> ~/.bash_profile

.PHONY: build
