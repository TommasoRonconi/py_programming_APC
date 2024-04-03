##############################################################
# Initialization:

# Load libraries
import numpy as np
import time

# Load argument variables here?
# [ ... ]

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

# Loop on the domain
cc = func( aa, bb ) # <--- exploiting vectorization and shared memory parallelism of NumPy

##############################################################
# Finalize program:

# Check everything went fine:
if np.isnan( cc ).any() or not np.isfinite( cc ).all() :
    raise Exception(
        'Something went wrong.'
        )
    
# Store outputs
np.save( 'outputarray_vector.npy', cc )

# end.
##############################################################
