FROM ghcr.io/slinkyproject/slurmd:24.11.1-rockylinux9

RUN <<EOR
set -xeuo pipefail
dnf -q makecache --refresh
dnf -q -y install vim git python3
dnf clean all
EOR
