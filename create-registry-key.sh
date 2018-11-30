#!/bin/bash -ex

# https://medium.com/@michaelmorrissey/using-cross-project-gcr-images-in-gke-1ddc36de3d42
# https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-secret-in-the-cluster-that-holds-your-authorization-token

kubectl create secret docker-registry gcrsecret --docker-username=_json_key --docker-password="$(cat rpi3-k8s-gcr.key)" --docker-server=https://gcr.io --docker-email=blah@example.com
