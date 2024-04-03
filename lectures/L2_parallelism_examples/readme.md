# Lecture 2

In this lecture we have inspected different files containing different levels of parallelism implementations of the same problem.

* [example_naive.py](example_naive.py) contains a simple program that applies an operation to a list of objects. It cannot be parallelised but
  gives a broken down example of the main parts of a program (i.e. initialization, execution, finalization)

* [example_serial.py](example_serial.py) is the starting point of the lecture. A more complex and realistic version of the naive example,
  it defines the problem at hand.
  Having followed Lecture 1, the student should be able to understand which part of the problem could take advantage of parallelism.

* [example_multip.py](example_multip.py) applies python ``multiprocessing`` to parallelise the problem with SHARED MEMORY PARALLELISM.

* [example_mpi4py.py](example_mpi4py.py) applies MPI for parallelisation (i.e. DISTRIBUTED MEMORY PARALLELISM).
  It cannot be run in the usual way but requires a call to mpi but needs instead:
  ``mpiexec -n [SOME NUMBER] python example_mpi4py.py``

* [example_vector.py](example_vector.py) this last version of the program uses NumPy's broadcasting (which exploits both shared memory parallelism
  and vectorisation). This was not shown at lecture since the NumPy library is presented in L3_S1 but it is here for completeness.
  The student should be aware though that NumPy's array broadcasting cannot always solve the problem.

Each of the above scripts generates an output file in ``NPY`` format.

Additional files present here:

* [inputarray.npy](inputarray.npy) input array for the execution of the examples above.

* [check_outputs.npy](check_outputs.npy) script to check that the outputs of the above exercises are correct.

* [run_parallel.sh](run_parallel.sh) is a script I have written at lecture to collect the execution time of the scripts (useful for plotting the scaling)
