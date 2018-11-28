IMAGE := angelus169/nagios-yaml

help:
	@echo "---------------------------------------------------------------"
	@echo "Author: Borys Babii <angelus169@gmail.com>"
	@echo "Version: 0.0.2"
	@echo "License: Apache license 2.0"
	@echo "---------------------------------------------------------------"
	@echo "	Usage:"
	@echo "		make <target>"
	@echo "	Targets:"
	@echo "		run       	run the application"
	@echo "		install   	install application dependencies"
	@echo "		image		build docker image"
	@echo "		push-image	push docker image"
	@echo "		pull-image	pull docker image"

run:
	python converter.py

install:
	pip install -r requirements.txt

image:
	docker build -t $(IMAGE) .

push-image:
	docker push $(IMAGE)

pull-image:
	docker pull ${IMAGE}

PHONY: help run install image push-image pull-image
