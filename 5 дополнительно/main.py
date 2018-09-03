#!/usr/bin/env python3

import json
from jsoncomment import JsonComment
import re
from readterms import readTerms
from urllib.parse import urlsplit

def urlDomain(url, domain):
  domains = urlsplit(url).netloc;  
  if re.fullmatch(r'.*\.?\b' + domain + '\.[a-z]+', domains):
    return True;
  else: return False;

def changePriority(data, terms):
  priority = terms["priority"];

  if urlDomain(data["url"], next(iter(terms["domain"]))):
    priority += next(iter(terms["domain"].values()));
  
  for what in terms["url"]:
    if "ends" in terms["url"][what] and data["url"].lower().endswith(what):
      priority += terms["url"][what]["ends"];
    elif "contains" in terms["url"][what] and any(s in data["url"] for s in what):
      priority += terms["url"][what]["contains"];    
  
  for key in terms:
    if key != "priority" and key != "url" and key != "domain":
      for what in terms[key]:
        if "starts" in terms[key][what] and "ends" in terms[key][what]:
          if str(data["info"][key]).startswith(what):
            priority += terms[key][what]["starts"];
          if str(data["info"][key]).endswith(what):
            priority += terms[key][what]["ends"];
        elif "starts" in terms[key][what]:
          if str(data["info"][key]).startswith(what):
            priority += terms[key][what]["starts"];
        elif "ends" in terms[key][what]:
          if str(data["info"][key]).endswith(what):
            priority += terms[key][what]["ends"];
        elif "contains" in terms[key][what]:
          if any(s in str(data["info"][key]) for s in what):
            priority += terms[key][what]["contains"];

  return priority;

path = "terms.txt";
terms = readTerms(path);
print('Terms were loaded from ' + path);

data = '';

print("Enter data: ");
data = '\n'.join(iter(input, data));
parser = JsonComment(json)
data = parser.loads(data);

priority = changePriority(data, terms);

print(priority);
