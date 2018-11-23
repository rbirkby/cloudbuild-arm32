### Dockerfile

This is a simple NodeJS Express server within an ARM container

### Instructions

Cloud Build commands

```bash
$ gcloud builds submit
$ gcloud builds list --ongoing
$ gcloud builds log <build id> --stream
```

Cloud Run commands

```bash
$ gcloud alpha run deploy --image gcr.io/<project>/<image>:<tag>
$ gcloud alpha run list
```

In the log output for a deploy or a build, you should see "Service ... revision ... has been deploy and is serving traffic at <endpoint>



### Dockerfile.cloudrun

This is a simple NodeJS Express server within an x86 container for running on Cloud Run

### Dockerfile.golang

This is a simple GoLang web server within an x86 container

