# Slurm

## Build Image

(image builds on munge image)

```
oc new-build --name slurm --binary
oc start-build slurm --from-dir=. --follow --no-cache
```

## Usage

```
Usage: slurmd [OPTIONS]
   -b                         Report node reboot now.
   -c                         Force cleanup of slurmd shared memory.
   -C                         Print node configuration information and exit.
   --conf                     Dynamic node configuration, works with -Z.
   --conf-server host[:port]  Get configs from slurmctld at `host[:port]`.
   -d stepd                   Pathname to the slurmstepd program.
   -D                         Run daemon in foreground.
   -f config                  Read configuration from the specified file.
   -F[feature]                Start as Dynamic Future node w/optional Feature.
   -G                         Print node's GRES configuration and exit.
   -h                         Print this help message.
   -L logfile                 Log messages to the file `logfile'.
   -M                         Use mlock() to lock slurmd pages into memory.
   -n value                   Run the daemon at the specified nice value.
   -N node                    Run the daemon for specified nodename.
   -s                         Change working directory to SlurmdLogFile/SlurmdSpoolDir.
   -v                         Verbose mode. Multiple -v's increase verbosity.
   -V                         Print version information and exit.
   -Z                         Start as Dynamic Normal node.
```

```
Usage: slurmctld [OPTIONS]
  -c      	Do not recover state from last checkpoint.
  -D      	Run daemon in foreground, with logging copied to stdout.
  -f file 	Use specified file for slurmctld configuration.
  -h      	Print this help message.
  -i      	Ignore errors found while reading in state files on startup.
  -L logfile 	Log messages to the specified file.
  -n value 	Run the daemon at the specified nice value.
  -R      	Recover full state from last checkpoint.
  -s      	Change working directory to SlurmctldLogFile/StateSaveLocation.
  -v      	Verbose mode. Multiple -v's increase verbosity.
  -V      	Print version information and exit.
```
