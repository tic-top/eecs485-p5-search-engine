#!/usr/bin/env python3
"""Document Counter"""
import sys
import csv
sys.stdout.write(f"a\t{sum(1 for line in sys.stdin)}\n")