#!/usr/bin/env python3

increases = 0
previous = 0
with open('input', 'r') as f:
    for line in f.readlines():
        line = int(line.strip())
        if previous:
            if previous < line: increases += 1
        previous = line

print(increases)
