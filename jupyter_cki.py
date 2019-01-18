#!/usr/bin/env python
#
# Jupyter Custom Kernel Installer (jupyter_cki)
# Copyright (C) 2019 aramcap (https://github.com/aramcap/jupyter_cki)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Not modify this software! It's can be produce corruption!
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

import sys
from subprocess import call
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove, chmod

# Call command
def command(py_path, kernel_name):
    return call([py_path+"/bin/python", "-m", "ipykernel", "install", "--name", kernel_name, "--prefix", py_path])

# Secure replace line in file
def replace(file_path, pattern, subst):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    remove(file_path)
    move(abs_path, file_path)
    return True

def help():
    return "\nJupyter Custom Kernel Installer - Copyright (GNU GPL v3) 2019 https://github.com/aramcap/jupyter_cki\n\n\
    How run: python jupyter_cki.py <PY_PATH> <KERNEL_NAME> <KERNEL_EXECUTOR>\n\
        PY_PATH: Python path that Jupyter uses\n\
        KERNEL_NAME: Kernel name for Jupyter\n\
        KERNEL_EXECUTOR: Python path for Python binary in environment\n\
\n\
Example: python jupyter_cki.py /opt/conda/envs/tools python36 /opt/conda/envs/python36\n"

if __name__ == "__main__":
    if len(sys.argv) == 4:
        PY_PATH = sys.argv[1]
        KERNEL_NAME = sys.argv[2]
        KERNEL_EXECUTOR = sys.argv[3]

        command(PY_PATH, KERNEL_NAME)
        replace(PY_PATH+"/share/jupyter/kernels/"+KERNEL_NAME+"/kernel.json", PY_PATH, KERNEL_EXECUTOR)
        chmod(PY_PATH+"/share/jupyter/kernels/"+KERNEL_NAME+"/kernel.json", 644)
    else:
        print(help())
        exit(1)