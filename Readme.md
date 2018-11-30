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

Enable scheduling of pods onto the k8s master node:

```bash
kubectl taint nodes --all node-role.kubernetes.io/master-
```

GCloud commands

Install the SDK on a worker node:

```bash
sudo raspi-config # on rpi3-k8s-{1,2}: 5 Interfacing Options #/ I2C / Enable
sudo raspi-config # on rpi3-k8s-4: 5 Interfacing Options #/ SPI / Enable
curl https://sdk.cloud.google.com | bash
gcloud init
gcloud auth configure-docker
kubectl label nodes rpi3-k8s-1 hardware=ledshim
kubectl label nodes rpi3-k8s-2 hardware=ledshim
kubectl label nodes rpi3-k8s-4 hardware=inky
kubectl label nodes rpi3-k8s-0 hardware=tof
kubectl label nodes rpi3-k8s-3 hardware=buttons
```

### pulse.yaml

Kubernetes yaml for running the docker container on a specific pod.


### Dockerfile.cloudrun

This is a simple NodeJS Express server within an x86 container for running on Cloud Run

### Dockerfile.golang

This is a simple GoLang web server within an x86 container

