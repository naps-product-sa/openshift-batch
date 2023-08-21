# Slurm

# Install

## Apply manifests

```
oc apply -k manifests/
```

## Create munge secret key

```
oc -n slurm-system create secret generic munge-key --from-file=munge.key=<(dd status=none if=/dev/urandom bs=1 count=128)
```

## Build images

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

# containerssh

TODO: replace authconfig python with OPA example: https://github.com/ContainerSSH/examples/tree/main/opa/containerssh

```
oc apply -k manifests/containerssh
```
