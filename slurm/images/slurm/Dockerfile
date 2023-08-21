FROM ghcr.io/naps-product-sa/munge:latest as build
ARG SLURM_VERSION=23.02.4

RUN dnf install -y xz gcc openssl-devel bzip2-devel zlib-devel procps-ng bzip2 perl perl-devel

RUN mkdir /tmp/src
WORKDIR /tmp/src

RUN curl -LO https://download.schedmd.com/slurm/slurm-${SLRUM_VERSION}.tar.bz2 && \
    tar xf slurm-${SLRUM_VERSION}.tar.bz2 && \
    cd slurm-${SLRUM_VERSION} && \
    ./configure \
     --prefix=/usr \
     --sysconfdir=/etc && \
    make && \
    make install

FROM ghcr.io/naps-product-sa/munge:latest

RUN dnf install -y bind-utils hostname iproute

COPY --from=build /usr /usr
COPY --from=build /etc /etc
COPY --from=build /var /var

RUN ldconfig && \
    useradd -r -u 501 slurm && \
    mkdir /var/spool/slurmctld && \
    chown slurm:slurm /var/spool/slurmctld

WORKDIR /
CMD ['/sbin/slurmd', '-D']
