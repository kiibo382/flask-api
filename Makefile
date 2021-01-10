.PHONY: build-local
build-local:
	docker-compose build

.PHONY: run-local
run-local:
	docker-compose up -d

.PHONY: cleanup
cleanup:
	docker-compose down