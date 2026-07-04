import ctypes
import os
src_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.abspath(os.path.join(src_dir, "..", "libcubiomes.so"))
print(f"Loading shared library from: {lib_path}")
def auto_compile():
    """Runs 'make' in the root directory automatically to ensure libcubiomes.so is built."""
    print("Checking/building libcubiomes.so via Makefile...")
    try:
        subprocess.run(
            ["make"], 
            cwd=root_dir, 
            check=True, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print(f"Compilation error while building cubiomes:\n{e.stderr.decode()}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'make' command not found. Ensure you are running inside 'nix-shell'.", file=sys.stderr)
        sys.exit(1)
auto_compile()
try:
    cubiomes = ctypes.CDLL(lib_path)
    print("Successfully loaded libcubiomes.so")
except OSError as e:
    print(f"Error loading library: {e}")
    print("Make sure you ran the gcc compilation command in the root folder first.")
    exit(1)
