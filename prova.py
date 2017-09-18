import sys, slepc4py
slepc4py.init(sys.argv)

from petsc4py import PETSc
from slepc4py import SLEPc
import numpy

opts = PETSc.Options()
n = opts.getInt('n', 30)

A = PETSc.Mat().create()
A.setSizes([n, n])
A.setFromOptions()
A.setUp()

rstart, rend = A.getOwnershipRange()

# first row
if rstart == 0:
