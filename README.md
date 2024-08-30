# openshift-batch

Testing batch capabilities of OpenShift

## Slurm on OpenShift

see [slurm/README.md](slurm/README.md)

## Simple NFS Storage

Just create a simple NFS server for shared storage this uses the upstream: https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner/tree/nfs-server-provisioner-1.8.0

```
$ oc apply -k simple-nfs/
```

## Todo

- AWS FSx Lustre support in demo
- Move users to external ldap maybe with https://github.com/glauth/glauth
- Implement UID/GID enforcement per namespace
- More advanced view of how jobs are scheduled and placed on the cluster
- Add and schedule workloads to specialized hardware like GPU or IB

