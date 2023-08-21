FROM quay.io/containerssh/agent AS agent

FROM ghcr.io/naps-product-sa/openshift-batch:slurm-latest

COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent

