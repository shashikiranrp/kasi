#!/usr/bin/env python

import string, sys, getopt

DEFAULT_MAP_FILE = "../kw_maps/kw_map_kannada.txt"

def getKeywordMapFromFile(fileName):
  _k_map = {}
  with open(DEFAULT_MAP_FILE) as fh:
    for line in filter(lambda ln: 0 <> len(ln) and not ln.startswith("#"), map(string.strip, fh.readlines())):
      (k, _, v) = map(string.strip, line.partition("="))
      if not k or not v:
        continue
      _k_map[k] = v
  return _k_map

def kasi(kw_map_file, target_file):
  kw_map = getKeywordMapFromFile(kw_map_file)

  with open(target_file) as rh, open("%s.C" % target_file, "w") as wh:
    pass


def usage():
  sys.stderr.write('''usage: %s [-h] [-k <keyword_map_file>] [-v] <file>
    -h, --help: show this help and exit.
    -k, --kw_map: key word map file (default: %s).
    -v, --verbose: enable verbose.
''' % (sys.argv[0], DEFAULT_MAP_FILE))

def main():
  if 2 > len(sys.argv):
    usage()
    sys.exit(2)

  try:
    opts, args = getopt.getopt(sys.argv[1:], "hk:v", ["help", "kw_map", "verbose"])
  except getopt.GetoptError as err:
    sys.stderr.write("Error: %s\n" % str(err))
    usage()
    sys.exit(2)

  kw_map_file = DEFAULT_MAP_FILE
  verbose = False
  for o, a in opts:
    if o in ('-v', '--verbose'):
      verbose = True
    elif o in ('-c', '--kw_map'):
      kw_map_file = a
    elif o in ('-h', '--help'):
      usage()
      sys.exit()

  kasi(kw_map_file, sys.argv[-1])
      
if __name__ == '__main__':
  main()
  
