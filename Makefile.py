import os
import sys

projroot = '.'
with open('.projroot', 'r') as f:
  lines = f.readlines()
  projroot = lines[0]

def srcfilter(entry: str):
  return entry.endswith('.c')

def srcmapper(entry: str):
  return projroot + '/src/' + entry

def join(xs: list):
  s = ''
  for x in xs:
    s += x + ' '
  return s

srcfiles = join(list(map(srcmapper, filter(srcfilter, os.listdir(projroot + '/src')))))

test = 'Main'
if len(sys.argv) > 1:
  test = sys.argv[1]

def testmapper(name: str):
  return projroot + '/test/' + test + 'Test.c'

os.system('gcc -g -c ' + srcfiles + testmapper(test))
os.system('gcc -o a *.o')
