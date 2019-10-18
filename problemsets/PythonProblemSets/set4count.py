#!/usr/bin/env python3

import sys
min_argv = int( min(sys.argv[1:]))
max_argv = int( max(sys.argv[1:])) # this will prevent user errors

myrange = [print(ran) for ran in range(min_argv, max_argv)]
myrange


