# Slurm

## Install

### Apply manifests

```
oc apply -k manifests/
```

### Create munge secret key

```
oc -n slurm-system create secret generic munge-key --from-file=munge.key=<(dd status=none if=/dev/urandom bs=1 count=128)
```

### Build images

```
oc new-build --name munge --binary
oc new-build --name slurm --binary
oc new-build --name login --binary
```

```
oc start-build munge --from-dir=images/munge --follow --no-cache
oc start-build slurm --from-dir=images/slurm --follow --no-cache
oc start-build login --from-dir=images/login --follow --no-cache
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

TODO: replace authconfig python with OPA example: https://github.com/ContainerSSH/examples/tree/main/opa/containerssh

```
$ oc apply -k manifests/containerssh
$ openssl genrsa | kubectl create secret generic -n containerssh containerssh-hostkey --from-file=host.key=/dev/stdin
```

### Login

```
$ oc get svc -n containerssh containerssh
NAME           TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)          AGE
containerssh   LoadBalancer   172.30.147.21   a9cf4fabd2d9b49659d8af106ea30536-1220395463.us-east-2.elb.amazonaws.com   2222:30036/TCP   47m

$ ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -p 2222 jason@a9cf4fabd2d9b49659d8af106ea30536-1220395463.us-east-2.elb.amazonaws.com
bash-5.1$
```
