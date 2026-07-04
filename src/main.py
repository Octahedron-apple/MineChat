import ctypes
import os
src_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.abspath(os.path.join(src_dir, "..", "libcubiomes.so"))
print(f"Loading shared library from: {lib_path}")
try:
    cubiomes = ctypes.CDLL(lib_path)
    print("Successfully loaded libcubiomes.so")
except OSError as e:
    print(f"Error loading library: {e}")
    print("Make sure you ran the gcc compilation command in the root folder first.")
    exit(1)
