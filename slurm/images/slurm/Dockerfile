FROM ghcr.io/naps-product-sa/openshift-batch:munge-latest as build
ARG SLURM_VERSION=23.02.4

# RUN echo "[9-stream-crb]" > /etc/yum.repos.d/9-stream-crp.repo && \
#     echo "name=9-stream-crb" >> /etc/yum.repos.d/9-stream-crp.repo && \
#     echo "baseurl = https://mirror.stream.centos.org/9-stream/CRB/\$basearch/os/" >> /etc/yum.repos.d/9-stream-crp.repo && \
#     echo "enabled = 1" >> /etc/yum.repos.d/9-stream-crp.repo && \
#     echo "gpgcheck = 0" >> /etc/yum.repos.d/9-stream-crp.repo

# RUN dnf install -y yum-utils

# RUN yum-config-manager --add-repo https://mirror.stream.centos.org/9-stream/BaseOS/\$basearch/os/ && yum-config-manager --add-repo https://mirror.stream.centos.org/9-stream/AppStream/\$basearch/os/

RUN dnf install --enablerepo=crb -y xz gcc openssl-devel bzip2-devel zlib-devel procps-ng bzip2 perl perl-devel git autoconf automake libtool diffutils jansson jansson-devel http-parser-devel

RUN mkdir /tmp/src
WORKDIR /tmp/src

RUN git clone --depth 1 --single-branch -b v1.12.0 https://github.com/benmcollins/libjwt.git libjwt && \
    cd libjwt && \
    autoreconf -v --install && \
    ./configure --prefix=/usr/local && \
    make -j && \
    make install

RUN curl -LO https://download.schedmd.com/slurm/slurm-${SLURM_VERSION}.tar.bz2 && \
    tar xf slurm-${SLURM_VERSION}.tar.bz2 && \
    cd slurm-${SLURM_VERSION} && \
    ./configure \
     --prefix=/usr \
     --sysconfdir=/etc && \
     --with-jwt=/usr/local/ && \
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
