#!/usr/bin/env python3

import json
from jsoncomment import JsonComment
import re
from urllib.parse import urlsplit

def urlDomain(url):
  domains = urlsplit(url).netloc;
  
  if re.fullmatch(r'.*\.?\bdrweb\.[a-z]+', domains):
    return True;
  else: return False;

def urlEnds(url):
  url = url.lower();
  if url.endswith(".exe") or url.endswith(".dll") or url.endswith(".pdf"):
    return True;
  else: return False;

def urlContains(url):
  url = url.lower();
  if url.find(".exe") >= 0 or url.find(".dll") >= 0 or url.find(".pdf") >= 0:
    return True;
  else: return False;

def changePriority(data):
  priority = 50;

  if urlEnds(data["url"]):
    priority += 15;
  elif urlContains(data["url"]):
    priority += 5;

  if urlDomain(data["url"]):
    priority += 50;

  if str(data["info"]["as"]).find("666") >= 0:
    priority += 50;

  iso = data["info"]["iso"];
  if iso.find("US") >= 0:
    priority -= 10;
  elif iso.find("RU") >= 0:
    priority += 10;
  elif iso.find("CN") >= 0 or iso.find("TW") >= 0:
    priority -= 30;

  return priority;

data = '';

print("Enter data: ");
data = '\n'.join(iter(input, data));

parser = JsonComment(json)
data = parser.loads(data);


priority = changePriority(data);

print(priority);
