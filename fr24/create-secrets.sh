#!/bin/sh -ex

# File format is FR24_KEY={secret key}
kubectl create secret generic fr24-secrets --from-env-file=fr24-k8s-secrets
