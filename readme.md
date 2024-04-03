# (Python) Programming in APC

This repository contains material for the PhD course in Python programming focused on problems that the astrophysicist and cosmologist could encounter in their carreer.

The course is structured in an hybrid form,

* **Lecture 1** is a classic frontal lecture introducing concept of parallel programming, architecture awareness and cluster usage.
  The lecture has been held at the blackboard with the support of the slides collected in [lectures/L1_parallelcomputing+clusters.pdf](lectures/L1_parallelcomputing+clusters.pdf).

* **Lecture 2** is an hands-on, the students have been shown different ways of applying parallelism to speed up the execution of a simple python program. The different examples shown during class are collected in the directory [lectures/L2_parallelism_examples](lectures/L2_parallelism_examples)
  REQUIREMENTS: a working installation of MPI and ``mpi4py``

* **Lecture 3** introduces NumPy, array-programming and catalogues. The lecture was presented with the 2 Jupyter Notebooks:
  - [lectures/L3_S1_NumPy.ipynb](lectures/L3_S1_NumPy.ipynb) 
  - [lectures/L3_S2_catalogue_inspection.ipynb](lectures/L3_S2_catalogue_inspection.ipynb)
  Students were asked to solve simple problems on-the-fly, following previous explanation of the tools to be used. These solutions have been added to the notebooks.
  REQUIREMENTS: ``numpy``, ``scipy``, ``matplotlib``, ``astropy``

* **Lecture 4** was once again an hands on in which we solved together the problem of fitting a parameterised model to some data, obtained in L3_S2.
  In particular, we want to fit a Schechter function to some data extracted from a catalogue.
  In [L4_S1_fitting.ipynb](L4_S1_fitting.ipynb) we use a naive grid method, the function ``scipy.optimize.minimize`` and the ``emcee`` library to fit the curve.
  REQUIREMENTS: Lecture 3 requirements + ``emcee`` + having run the [lectures/L3_S2_catalogue_inspection.ipynb](lectures/L3_S2_catalogue_inspection.ipynb) notebook (in which the dataset studied is produced)

Some of the above notebooks use datasets stored in the [datasets](datasets) directory.