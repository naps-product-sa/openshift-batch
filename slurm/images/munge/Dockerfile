FROM registry.access.redhat.com/ubi9:latest as build
ARG MUNGE_VERSION=0.5.15

RUN dnf install -y xz gcc openssl-devel bzip2-devel zlib-devel procps-ng

RUN mkdir /tmp/src
WORKDIR /tmp/src

RUN curl -LO https://github.com/dun/munge/releases/download/munge-${MUNGE_VERSION}/munge-${MUNGE_VERSION}.tar.xz && \
    tar xJf munge-${MUNGE_VERSION}.tar.xz && \
    cd munge-${MUNGE_VERSION} && \
    ./configure \
     --prefix=/usr \
     --sysconfdir=/etc \
     --localstatedir=/var \
     --runstatedir=/run && \
    make && \
    make install

FROM registry.access.redhat.com/ubi9:latest

COPY --from=build /usr /usr
COPY --from=build /etc /etc
COPY --from=build /var /var

RUN ldconfig && \
    useradd -r -u 500 munge && \
    mkdir -v /run/munge && \
    chown -v munge:munge /run/munge && \
    chown -v munge:munge /etc/munge

RUN useradd user1 && \
    useradd user2 && \
    useradd user3 && \
    useradd user4

RUN mkdir /scripts
ADD fix-munge-paths.sh /scripts
RUN chmod +x /scripts/*.sh

WORKDIR /
CMD ['/sbin/munged', '-F']
