import sys, os, io
from fnmatch import fnmatch

def greb(pattern, keyword):
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in filter(lambda f: fnmatch(f, pattern), filenames):
            with io.open(os.path.join(dirpath, filename), encoding='utf-8') as file:
                for row, line in enumerate(file):
                    if keyword in line:
                        yield '{}\n{}: {}'.format(filename, row+1, line)

pattern, keyword = sys.argv[1], sys.argv[2]

for i in greb(pattern, keyword):
    print i

