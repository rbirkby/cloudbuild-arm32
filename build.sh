#!/bin/bash -ex

# Manual trigger when GitHub integration isn't working
# Assumes use of cloudbuild.yaml (since gcloud v223)
# NOTE: This will autogenerate a .gcloudignore from the .gitignore file
gcloud builds submit

