'''
python Makefile.py Foo --> Build with test/FooTest.c and run
'''

import os
import sys

pathjoin = os.path.join

projroot = '.'
with open('.projroot', 'r') as f:
  lines = f.readlines()
  reg = {}
  for line in lines:
    line = line.strip().split(' ', 1)
    reg[line[0].strip()] = line[1].strip()
  if sys.platform.startswith('win'):
    projroot = reg['Windows:']
  elif sys.platform.startswith('linux'):
    projroot = reg['Linux:']

def srcfilter(entry: str):
  return entry.endswith('.c')

def srcmapper(entry: str):
  return pathjoin(projroot, 'src', entry)

def objectfilter(entry: str):
  return entry.endswith('.o')

def objectmapper(entry: str):
  return pathjoin(projroot, entry)

def join(xs: list):
  s = ''
  for x in xs:
    s += x + ' '
  return s

srcfiles = join(list(map(srcmapper, filter(srcfilter, os.listdir(pathjoin(projroot, 'src'))))))

test = 'clean'
if len(sys.argv) > 1:
  test = sys.argv[1]

if test == 'clean':
  objfiles = list(map(objectmapper, filter(objectfilter, os.listdir(projroot))))
  for entry in objfiles:
    print(entry)
    os.remove(entry)
  os.remove(pathjoin(projroot, 'a'))
  exit(0)

def testmapper(name: str) -> str:
  testpath = pathjoin(projroot, 'test')
  ls = os.listdir(testpath)
  for entry in ls:
    if entry == name + 'Test.c':
      return pathjoin(testpath, name + 'Test.c')
  raise IOError('Test module %s not found' % name)

testfile = testmapper(test)

CC = 'gcc -g -c ' + srcfiles + testmapper(test)
print(CC)
os.system(CC)

objfiles = join(list(map(objectmapper, filter(objectfilter, os.listdir(projroot)))))

LD = 'gcc -o a ' + objfiles
print(LD)
os.system(LD)

print('\nTest starting...\n----------------')
os.system(pathjoin(projroot, 'a'))
