FROM ghcr.io/slinkyproject/slurmd:24.11.1-rockylinux9

RUN <<EOR
# Install hpc dev env
set -xeuo pipefail
dnf -q makecache --refresh
# https://spack.readthedocs.io/en/latest/getting_started.html
dnf -y group install "Development Tools"
dnf -q -y install gcc-gfortran redhat-lsb-core python3 unzip
dnf clean all
EOR
