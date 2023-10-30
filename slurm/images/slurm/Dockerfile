FROM ghcr.io/naps-product-sa/openshift-batch/munge:latest as build
ARG SLURM_VERSION=23.02.4

RUN dnf install --enablerepo=crb -y xz gcc procps-ng bzip2 perl git autoconf automake libtool diffutils jansson \
    openssl-devel bzip2-devel zlib-devel jansson-devel http-parser-devel json-c-devel perl-devel

RUN mkdir /tmp/src
WORKDIR /tmp/src

RUN git clone --depth 1 --single-branch -b v1.12.0 https://github.com/benmcollins/libjwt.git libjwt && \
    cd libjwt && \
    autoreconf -v --install && \
    ./configure --prefix=/usr && \
    make -j && \
    make install

RUN curl -LO https://download.schedmd.com/slurm/slurm-${SLURM_VERSION}.tar.bz2 && \
    tar xf slurm-${SLURM_VERSION}.tar.bz2 && \
    cd slurm-${SLURM_VERSION} && \
    ./configure \
     --prefix=/usr \
     --sysconfdir=/etc \
     --with-jwt=/usr && \
    make && \
    make install

FROM scratch as tmp

# libjwt
COPY --from=build /usr/include/jwt* /usr/include/
COPY --from=build /usr/lib64/libjwt* /usr/lib/
COPY --from=build /usr/lib64/pkgconfig/libjwt* /usr/lib64/pkgconfig/
COPY --from=build /usr/bin/jwt* /usr/bin/

#slurm
COPY --from=build /usr/lib64/*slurm* /usr/lib64/
COPY --from=build /usr/lib64/slurm/ /usr/lib64/slurm/
COPY --from=build /usr/bin/s* /usr/bin/
COPY --from=build /usr/sbin/slurm* /usr/sbin/
COPY --from=build /usr/share/man/ /usr/share/man/

FROM ghcr.io/naps-product-sa/openshift-batch/munge:latest

COPY --from=tmp / /

RUN dnf install -y procps-ng bind-utils hostname iproute jansson http-parser

RUN ldconfig && ldconfig -n /usr/lib64/slurm && \
    useradd -r -u 501 slurm && \
    mkdir /var/spool/slurmctld && \
    chown slurm:slurm /var/spool/slurmctld && \
    mkdir /var/spool/slurmd && \
    chown slurm:slurm /var/spool/slurmd    

WORKDIR /
CMD ['/sbin/slurmd', '-D']
