#!/usr/bin/env bash
set -e

echo "Compiling C wrapper..."
# We need to compile test_wrapper.c into a shared object, linking with libcubiomes.so or its object files.
# The project has `Makefile` and `libcubiomes.so` in root. We can just link against the existing libcubiomes.so.
gcc -shared -fPIC -o tests/libcubiomes_wrapper.so tests/test_wrapper.c -L. -lcubiomes -Wl,-rpath=$(pwd)

echo "Running pytest..."
python3 -m pytest tests/test_cubiomes.py -v
