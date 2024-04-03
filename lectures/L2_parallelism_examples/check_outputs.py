##############################################################
# Check arrays are the same

# Load libraries
import numpy as np
import sys

# Load argument variables
if len(sys.argv) < 3 :
    raise RuntimeError(
        'Necessary 2 arguments: files with 1st and 2nd array'
    )

a1 = np.load( sys.argv[1] )
a2 = np.load( sys.argv[2] )

if np.any(a1 != a2) :
    raise RuntimeError( 'arrays are different' )
else :
    print( 'all good.' )

##############################################################
