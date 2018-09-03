#!/usr/bin/env python3

import os
import re

def search(path):
  files = os.listdir(path);
  names = set();

  for filename in files:
    name = re.fullmatch(r'image-(.+)-\d+T?\d+\.tar\.gz',filename);
    if name:    
      name = name[1];
      names.add(name)

  for name in list(names):
    print(name);

search(".")
