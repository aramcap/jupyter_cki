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

import os, sys, argparse
from subprocess import call
from tempfile import mkstemp
from shutil import move

# Call command
def command(env_path, kernel_name):
    return call([env_path+"/bin/python", "-m", "ipykernel", "install", "--name", kernel_name, "--prefix", env_path])

# Secure replace line in file
def replace(file_path, pattern, subst):
    fh, abs_path = mkstemp()
    with os.fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    os.remove(file_path)
    move(abs_path, file_path)
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Jupyter Custom Kernel Installer - Copyright (GNU GPL v3) 2019 https://github.com/aramcap/jupyter_cki')
    subparsers = parser.add_subparsers(help='Subcommands', dest="command")
    parser_python = subparsers.add_parser('python', help='Install Python kernel')
    parser_python.add_argument('--jupyter', action='store', help='Jupyter environment path')
    parser_python.add_argument('--kernel', action='store', help='Python kernel environment path')
    parser_python.add_argument('--kernel_name', action='store', help='Kernel name')
    parser_ir = subparsers.add_parser('ir', help='Install IR kernel')
    parser_ir.add_argument('--jupyter', action='store', help='Jupyter environment path')
    parser_ir.add_argument('--kernel', action='store', help='IR kernel environment path')
    args = parser.parse_args()

    if args.command == "python":
        if args.jupyter == None or args.kernel == None or args.kernel_name == None:
            parser_python.print_help()
            sys.exit(2)
        
        ENV_PATH = args.jupyter
        KERNEL_PATH = args.kernel
        KERNEL_NAME = args.kernel_name

        command(ENV_PATH, KERNEL_NAME)
        replace(ENV_PATH+"/share/jupyter/kernels/"+KERNEL_NAME+"/kernel.json", ENV_PATH, KERNEL_PATH)
        os.chmod(ENV_PATH+"/share/jupyter/kernels/"+KERNEL_NAME+"/kernel.json", 644)
    elif args.command == "ir":
        if args.jupyter == None or args.kernel == None:
            parser_ir.print_help()
            sys.exit(2)
        
        ENV_PATH = args.jupyter
        KERNEL_PATH = args.kernel

        replace(ENV_PATH+"/share/jupyter/kernels/ir/kernel.json", '["R"', '["'+os.path.join(KERNEL_PATH,"bin/R")+'"')
        os.chmod(ENV_PATH+"/share/jupyter/kernels/ir/kernel.json", 644)
    else:
        parser.print_help()
        sys.exit(2)
