FROM ghcr.io/naps-product-sa/openshift-batch:munge-latest as build
ARG SLURM_VERSION=23.02.4

RUN dnf install -y xz gcc openssl-devel bzip2-devel zlib-devel procps-ng bzip2 perl perl-devel git autoconf

RUN mkdir /tmp/src
WORKDIR /tmp/src

RUN git clone --depth 1 --single-branch -b v1.12.0 https://github.com/benmcollins/libjwt.git libjwt && \
    cd libjwt && \
    autoreconf --force --install && \
    ./configure --prefix=/usr/local && \
    make -j && \
    make install

RUN curl -LO https://download.schedmd.com/slurm/slurm-${SLURM_VERSION}.tar.bz2 && \
    tar xf slurm-${SLURM_VERSION}.tar.bz2 && \
    cd slurm-${SLURM_VERSION} && \
    ./configure \
     --prefix=/usr \
     --sysconfdir=/etc && \
     -- with-jwt=/usr/local/ && \
    make && \
    make install

FROM ghcr.io/naps-product-sa/openshift-batch:munge-latest

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
