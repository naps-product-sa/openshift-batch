#!/bin/bash
# https://www.mpinat.mpg.de/grubmueller/bench
# http://www.mdtutorials.com/gmx/lysozyme/10_analysis2.html
# https://manual.gromacs.org/documentation/2016/user-guide/file-formats.html
# https://manual.gromacs.org/documentation/2019/how-to/visualize.html#software

curl -Lo benchMEM.zip https://www.mpinat.mpg.de/benchMEM
unzip benchMEM.zip
. GMXRC.bash
mpirun -np 1 gmx_mpi mdrun -s benchMEM.tpr -nsteps 10000 -resethway
