# -*- mode: Python -*-
services = ["accounts-service", "postgres"]
yaml_files = ["k8s/%s.yaml" % service for service in services]

k8s_yaml(yaml_files)

docker_build("accounts", "accounts-service", dockerfile="accounts-service/Dockerfile")

k8s_resource(workload="accounts-deployment", port_forwards="8000:8000")
