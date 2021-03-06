# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
#   Importlib
import importlib.util
#   Pathlib
from pathlib import Path

# PyMake Imports
#   Projects
from pymake.projects import ProjectData
#   Toolchains: Clang
from pymake.toolchains.clang import ClangToolchainC
from pymake.toolchains.clang import ClangToolchainCXX
#   Toolchains: GCC
from pymake.toolchains.gcc import GccToolchainC
from pymake.toolchains.gcc import GccToolchainCXX


# =============================================================================
# >> REGISTER TOOLCHAINS
# =============================================================================
# Register Clang family toolchains
ClangToolchainC.register()
ClangToolchainCXX.register()

# Register GCC family toolchains
GccToolchainC.register()
GccToolchainCXX.register()


def main():
    # Load the make.py module, if it exists
    make_py = Path("make.py")

    if make_py.exists():
        spec = importlib.util.spec_from_file_location("make", str(make_py))
        make = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(make)

    # Get project data from the YAML file inside the current working directory
    data = ProjectData.read("pymake.yml")

    # Build the target sequentially
    # data.build()

    # Build the target in parallel
    data.build_parallel()
