#! /bin/sh -ex

gcloud config set run/region us-central1
gcloud alpha run deploy --image gcr.io/sonorous-crane-219712/cloudbuild-arm32:cloudrun
