##############################################################
# Initialization:

# Load libraries
import numpy as np
import time
import os
import sys

########## <-------------------------------------- Specific/
import multiprocessing as mp
########## <-------------------------------------- /Specific

# Load argument variables here?
if len(sys.argv) != 2 :
    raise RuntimeError( 'I want the number of processes' )
Nproc = int(sys.argv[1])

# define internal functions
def func ( v1, v2 ) :
    time.sleep(5.e-3)
    return v1 * np.exp( v2 )

# load inputs
aa = np.load( 'inputarray.npy' )
NN = aa.size

# define variables
bb = np.linspace( 0, 100, NN )

# check initializations 
if aa.size != bb.size :
    raise Exception(
        f'Input arrays should have same size = {aa.size}'
    )

# initialize output
cc = np.empty( NN )

##############################################################
# Start operations:

########## <-------------------------------------- Specific/

# define a function unpacking the arguments
def func_mp ( arg ) :
    return func( *arg )

t1 = time.time()
# context manager for pool of processes
# with mp.Pool(os.cpu_count()) as p :
with mp.Pool(Nproc) as p :
    cc = p.map( func_mp, zip(aa, bb) )
t2 = time.time()
print( t2-t1 )
########## <-------------------------------------- /Specific

##############################################################
# Finalize program:

# Check everything went fine:
if np.isnan( cc ).any() or not np.isfinite( cc ).all() :
    raise Exception(
        'Something went wrong.'
        )
    
# Store outputs
np.save( 'outputarray_mp.npy', cc )

# end.
##############################################################
