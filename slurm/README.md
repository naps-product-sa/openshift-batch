# Slurm

> [!IMPORTANT]
> This is one way of doing Slurm on OpenShift but a better way is now to use [Slinky](https://slurm.schedmd.com/slinky.html)
> from SchedMD. These manifests are left for historical reasons and are no longer being updated.

## Install

### Create image builds and build images

```
oc adm new-project slurm-system
```

```
oc new-build -n slurm-system --name munge --binary
oc new-build -n slurm-system --name slurm --binary
oc new-build -n slurm-system --name login --binary
```

#### Option 1: Set up local ImageStreams to pull through from upstream

```
oc tag --source=docker ghcr.io/naps-product-sa/openshift-batch/munge:latest slurm-system/munge:latest --reference-policy=local
oc tag --source=docker ghcr.io/naps-product-sa/openshift-batch/slurm:latest slurm-system/slurm:latest --reference-policy=local
oc tag --source=docker ghcr.io/naps-product-sa/openshift-batch/login:latest slurm-system/login:latest --reference-policy=local
```

#### Option 2: Build the images yourself

```
oc start-build -n slurm-system munge --from-dir=images/munge --follow --no-cache
oc start-build -n slurm-system slurm --from-dir=images/slurm --follow --no-cache
oc start-build -n slurm-system login --from-dir=images/login --follow --no-cache
```

### Create munge secret key

```
oc -n slurm-system create secret generic munge-key --from-file=munge.key=<(dd status=none if=/dev/urandom bs=1 count=128)
```

### Apply manifests

```
oc apply -k manifests/
```


## Slurm job

```
#!/bin/bash
#SBATCH --nodes=1                # node count
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)

sleep 10
```

### Scale compute

```
$ oc scale -n slurm-system statefulset/compute --replicas=3
```

```
#!/bin/bash
#SBATCH --nodes=3                # node count
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)

sleep 10
```

## containerssh

```
oc new-project containerssh
```

Set your user ssh public key into the authentication app (hardcoded)

```
sed -i -e "s#ssh-rsa.*#$(cat ~/.ssh/id_rsa.pub)#" manifests/containerssh/authconfig/app.py
```

TODO: Automate or script this part
Generate host key and create a secret for it

```
openssl rsa -in mykey.pem -pubout > mykey.pub
oc create secret generic -n containerssh  containerssh-hostkey --from-file=host.key=mykey.pem
```
```
$ oc apply -k manifests/containerssh
$ openssl genrsa | kubectl create secret generic -n containerssh containerssh-hostkey --from-file=host.key=/dev/stdin
```

## Checks

Check thats pods in projects `slurm-system` and `containerssh` are up and running:

```
oc get pods -n containerssh
oc get pods -n slurm-system
```

You are ready for the demo and you can return to [the main demo README](../README.md)

### Login

```
$ oc get svc -n containerssh containerssh
NAME           TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)          AGE
containerssh   LoadBalancer   172.30.147.21   a9cf4fabd2d9b49659d8af106ea30536-1220395463.us-east-2.elb.amazonaws.com   2222:30036/TCP   47m

$ ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -p 2222 jason@a9cf4fabd2d9b49659d8af106ea30536-1220395463.us-east-2.elb.amazonaws.com
bash-5.1$
```
