[root@slurm-0 /]# cat /var/spool/slurm/jwks.json

[root@slurm-0 /]# cat /etc/cgroup.conf
CgroupPlugin=cgroup/v1

[root@slurm-0 /]# jobs
[1]   Running                 munged -F &
[6]   Running                 SLURM_JWT=daemon slurmrestd -a rest_auth/jwt -u nobody -s openapi/v0.0.37 localhost:8080 -vvv &
[7]-  Running                 slurmctld -D vvv &
[8]+  Running                 slurmd -DZ --conf /etc/slurm.conf -vvv &

$ oc create token default | pbcopy

curl -H "X-SLURM-USER-NAME: system:serviceaccount:default:default" \
     -H "X-SLURM-USER-TOKEN: TOKEN" \
     localhost:8080/slurm

scontrol token lifespan=31536000 username=jason
