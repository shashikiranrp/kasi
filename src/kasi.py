#!/usr/bin/env python

import string, sys, getopt, codecs

DEFAULT_MAP_FILE = "../kw_maps/kw_map_kannada.txt"

def getKeywordMapFromFile(fileName):
  _k_map = {}
  with codecs.open(fileName, "r", "utf-8") as fh:
    for line in filter(lambda ln: 0 <> len(ln) and not ln.startswith("#"), map(string.strip, fh.readlines())):
      (k, _, v) = map(string.strip, line.partition("="))
      if not k or not v:
        continue
      _k_map[unicode(k)] = v
  return _k_map

def is_ascii(in_str):
  return all(ord(c) < 128 for c in in_str)

def kasi(kw_map_file, target_file):
  kw_map = getKeywordMapFromFile(kw_map_file)

  buffer_str = u""
  quote_seen = False
  line_no = 0
  need_to_buffer = False
  with codecs.open(target_file, "r", "utf-8") as rh, open("%s.C" % target_file, "w") as wh:
    # yes, single pass :-)
    for ln in rh:
      line_no += 1
      for ch in ln:
        # handling string literals
        if '"' == ch:
          # Yes toggle
          quote_seen = not quote_seen
        
        # if inside the code just write it
        if quote_seen:
          wh.write(ch)
          continue
        
        # in the state of handling foriegn keywords
        if need_to_buffer:
          # is_ascii will change the state
          if is_ascii(ch):
            c_kw = kw_map.get(buffer_str, None)
            # error out for an un mapped key word
            if None == c_kw:
              raise RuntimeError("no such keyword @ line_no %d" % line_no)

            # write the map and current ascii char
            wh.write(c_kw)
            wh.write(ch)
            # reset the state
            buffer_str = u''
            need_to_buffer = False
            continue
          else:
            # else append to unicode buffer
            buffer_str += ch
            continue

        # not ascii, drama starts
        if not is_ascii(ch):
          need_to_buffer = True
          buffer_str += ch
          continue
        
        # don't care, just stream
        wh.write(ch)


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
  
