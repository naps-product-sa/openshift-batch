# MUNGE

## Build Image

```
oc create ns slurm-system
oc project slurm-system

oc new-build --name munge --binary
oc start-build munge --from-dir=. --follow --no-cache
```

## munged Usage

```
Usage: munged [OPTIONS]

  -h, --help                Display this help message
  -L, --license             Display license information
  -V, --version             Display version information

  -f, --force               Force daemon to run if possible
  -F, --foreground          Run daemon in the foreground (do not fork)
  -M, --mlockall            Lock all pages in memory
  -s, --stop                Stop daemon bound to socket
  -S, --socket=PATH         Specify local socket [/run/munge/munge.socket.2]
  -v, --verbose             Be verbose

  --benchmark               Disable timers to reduce noise while benchmarking
  --group-check-mtime=BOOL  Specify whether to check "/etc/group" mtime [1]
  --group-update-time=SECS  Specify seconds between group info updates [3600]
  --key-file=PATH           Specify key file [/etc/munge/munge.key]
  --log-file=PATH           Specify log file [/var/log/munge/munged.log]
  --max-ttl=SECS            Specify maximum time-to-live (in seconds) [3600]
  --num-threads=INT         Specify number of threads to spawn [2]
  --origin=ADDR             Specify origin address via hostname/IPaddr/interface
  --pid-file=PATH           Specify PID file [/run/munge/munged.pid]
  --seed-file=PATH          Specify PRNG seed file [/var/lib/munge/munged.seed]
  --syslog                  Redirect log messages to syslog
  --trusted-group=GID       Specify trusted group/GID for directory checks
```
