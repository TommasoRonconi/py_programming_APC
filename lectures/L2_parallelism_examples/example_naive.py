##############################################################
# Initialization:

# define variables
aa = 42
size = 100
bb = []

##############################################################
# Start operations:

# Loop on the domain
for ii in range( size ) :
    bb += [ ii**aa ]

##############################################################
# Finalize program:

with open( 'output.txt', 'w' ) as f :
    for b in bb : f.write( f'{b}\n' )

# end.
##############################################################
