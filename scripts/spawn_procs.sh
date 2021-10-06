#!/bin/sh

# source.sh doit etre sourced avant de lancer ce prog
pids=""

for i in $(seq 0 25); do
    sleep 1d &
    pids="$pids $!"
done

wait $pids

echo "Good Job killing those sleepy jobs"