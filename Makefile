
all: dep build_qpu_server

PROTOC := $(shell which protoc)
UNAME := $(shell uname)
DOCKERREPONAME := dvasilas/proteus
TAG := $(shell git log -1 --pretty=%H | cut -c1-8)
IMG := ${DOCKERREPONAME}:${TAG}

$(PROTOC_CMD):
ifeq ($(UNAME), Darwin)
	https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-osx-x86_64.zip
	unzip /tmp/protoc.zip -d "$(HOME)/protoc"
endif
ifeq ($(UNAME), Linux)
	curl -L https://github.com/google/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip -o /tmp/protoc.zip
	unzip /tmp/protoc.zip -d "$(HOME)/protoc"
endif

dep:
	dep ensure

proto: $(PROTOC_CMD)
	go get ./vendor/github.com/golang/protobuf/protoc-gen-go
	protoc --go_out=plugins=grpc:$(GOPATH)/src/ ./src/protos/utils/utils.proto
	protoc --proto_path=./src/protos/utils --proto_path=./src/protos/qpu --go_out=plugins=grpc:$(GOPATH)/src ./src/protos/qpu/qpu.proto
	protoc --proto_path=./src/protos/utils --proto_path=./src/protos/qpu --proto_path=./src/protos/s3 --go_out=plugins=grpc:$(GOPATH)/src ./src/protos/s3/s3.proto
	protoc --proto_path=./src/protos/utils --proto_path=./src/protos/antidote --go_out=plugins=grpc:$(GOPATH)/src ./src/protos/antidote/log_propagation.proto
	protoc --proto_path=./src/protos/qpu --proto_path=./src/protos/utils --go_out=plugins=grpc:$(GOPATH)/src/ ./src/protos/qpu/qpu.proto
	protoc --proto_path=./src/protos/qpu --proto_path=./src/protos/s3client --go_out=plugins=grpc:$(GOPATH)/src/ ./src/protos/s3client/s3client.proto
	protoc --proto_path=./src/protos/qpu --proto_path=./src/protos/monitoring --go_out=plugins=grpc:$(GOPATH)/src/ ./src/protos/monitoring/monitoring.proto
	python3 -m grpc_tools.protoc -I./src/protos/s3client --python_out=./benchmarks/s3/ --grpc_python_out=./benchmarks/s3/ ./src/protos/s3client/s3client.proto

build_qpu_server:
	go build -o bin/qpu_server -v ./src/qpu/server/server.go

# Cross compilation
build_qpu_server_linux:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o bin/qpu_server_linux -v ./qpu/server/server.go

serve_ds:
	./bin/ds_server

serve_scan_qpu:
	$(PWD)/bin/qpu_server -qpu=scanQPU

serve_index_qpu:
	$(PWD)/bin/qpu_server -qpu=indexQPU

test:
	go test -v ./...

clean:
	rm ./protos/utils/utils.pb.go ./protos/datastore/datastore.pb.go ./protos/s3/s3.pb.go ./protos/qpu/qpu.pb.go
	rm -rf ./bin

docker_build:
	echo ${TAG}
	echo ${IMG}
	docker build -t proteus:local .
	docker tag proteus:local ${IMG}

docker_push:
	docker push ${IMG}

.PHONY: build_qpu_server build_qpu_server test clean local docker_build docker_push
