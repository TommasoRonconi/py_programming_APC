##############################################################
# Initialization:


# Always first <-------------------------------------- IMPORTANT
from mpi4py import MPI

# Load libraries
import numpy as np
import time

# define internal functions
def func ( v1, v2 ) :
    time.sleep(5.e-3)
    return v1 * np.exp( v2 )

# Initialize a communication world
comm = MPI.COMM_WORLD

# Count how many processes in the world
size = comm.Get_size()

# Give each process a name
rank = comm.Get_rank()

if rank == 0 :
    
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

else :

    # prepare container on other ranks
    NN = None


# BROADCAST size from root to others (1 to N communication)
NN = comm.bcast( NN, root = 0 )

# Compute local amount of data
Nloc = int( NN / size )

# check the load is balanced
if NN % Nloc != 0 :
    raise RuntimeError( 'load unbalance' )

# prepare storage on other processes
if rank != 0 :
    aa = np.empty( NN, dtype='d' )
    bb = np.empty( NN, dtype='d' )

# BROADCAST arrays from root to others (1 to N communication)
aa = comm.bcast( aa, root=0 )
bb = comm.bcast( bb, root=0 )

# initialize output
cloc = np.empty( Nloc, dtype='d' )

##############################################################
# Start operations:

# Compute starting point for each rank
start_loc = rank * Nloc

# Loop on the domain
for ii in range( start_loc, start_loc+Nloc ) :
    # note the indexing:
    cloc[ ii-start_loc ] = func( aa[ ii ], bb[ ii ] ) 

# prepare output array
cc = None
if rank == 0 :
    cc = np.empty( [size, Nloc], dtype='d' )

# GATHER information from all processes
comm.Gather( cloc, cc, root=0 )

if rank == 0 :
    cc = cc.ravel()

##############################################################
# Finalize program:

if rank == 0 :
    
    # Check everything went fine:
    if np.isnan( cc ).any() or not np.isfinite( cc ).all() :
        raise Exception(
            'Something went wrong.'
        )
    
    # Store outputs
    np.save( 'outputarray_mpi.npy', cc )

# end.
##############################################################
