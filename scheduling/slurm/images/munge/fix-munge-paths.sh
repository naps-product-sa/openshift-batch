#!/bin/bash

cp -v /var/secrets/munge.key /etc/munge/munge.key
chown -v -R munge:munge /etc/munge
chmod -v 700 /etc/munge
chmod -v 400 /etc/munge/munge.key

chown -v munge:munge /run/munge
chmod -v 755 /run/munge

exit 0
