FROM quay.io/centos/centos:stream9 as build
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

FROM scratch as tmp

COPY --from=build /etc/munge /etc/munge
COPY --from=build /var/lib/munge /var/lib/munge
COPY --from=build /var/log/munge /var/log/munge
COPY --from=build /run/munge /run/munge
COPY --from=build /usr/lib/*munge* /usr/lib/
COPY --from=build /usr/lib/pkgconfig/munge.pc /usr/lib/pkgconfig
COPY --from=build /usr/include/*munge* /usr/include/
COPY --from=build /usr/share/man/man1/*munge* /usr/share/man/man1/
COPY --from=build /usr/share/man/man3/*munge* /usr/share/man/man3/
COPY --from=build /usr/share/man/man7/*munge* /usr/share/man/man7/
COPY --from=build /usr/share/man/man8/*munge* /usr/share/man/man8/
COPY --from=build /usr/bin/*munge* /usr/bin/
COPY --from=build /usr/sbin/*munge* /usr/sbin/

FROM quay.io/centos/centos:stream9

# single layer for copy
COPY --from=tmp / /

RUN ldconfig && \
    useradd -r -u 500 munge && \
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
