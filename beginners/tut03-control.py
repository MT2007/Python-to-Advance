#!/usr/bin/env python3

import sys  # used for the sys.exit function

int_var = 9
if int_var < 8:
    sys.exit("int_var must be greater than 8")
else:
    print("int_var is greater than 8")
