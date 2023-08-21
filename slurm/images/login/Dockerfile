FROM quay.io/containerssh/agent AS agent

FROM ghcr.io/naps-product-sa/slurm:latest

COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent

