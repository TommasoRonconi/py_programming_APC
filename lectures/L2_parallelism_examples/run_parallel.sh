#! /bin/bash

for i in 1 2 4 8 16
do
    python example_multip.py $i >> perf_measure.txt
done

