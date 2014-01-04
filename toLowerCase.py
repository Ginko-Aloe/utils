#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert stdin to lowercase."""

import sys

print "".join(sys.stdin.readlines()).lower()

