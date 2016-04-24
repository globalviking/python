#!/usr/bin/env python
# Years till 100
import sys

name = sys.argv[1]
age = int(sys.argv[2])
diff = 50 - age

print 'Hello', name.title() + ', you will be 50 in', diff, 'years!'
