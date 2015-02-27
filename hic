#!/usr/bin/env python
from sys import argv, stdout

from mylang.hello import hic

for fname in argv[1:]:
    hic(open(fname).read())
