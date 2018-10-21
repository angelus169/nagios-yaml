IMAGE := angelus169/nagios-yaml

image:
	docker build -t $(IMAGE) .

push-image:
	docker push $(IMAGE)

PHONY: image push-image
