import re

def readTerms(path):
  terms = {};
  try:
    f = open(path, "r");
  except:
    print('Please, create file ' + path);
  i = 0;
  terms["priority"] = 0;

  for line in f:
    i += 1;
    if line.startswith("priority "):
      try: terms["priority"] = int(re.search(r'(-?\d+)', line)[0]);
      except TypeError:
        print('Ошибка в файле правил (строка ' + str(i) + ')');

    elif line.startswith("domain "):
      try:
        terms["domain"] = {};
        terms["domain"][re.search(r'domain (\w+) ', line)[1]] = int(re.search(r'domain \w+ (-?\d+)', line)[1]);
      except TypeError:
        print('Ошибка в файле правил (строка ' + str(i) + ')');      

    elif line.startswith("url "):
      try:
        where = re.search(r'url (contains|ends) ', line)[1];        
        what = re.search(r'url \w+ (\S+)', line)[1].split("/");
        what = tuple(what)
        if "url" not in terms: terms["url"] = {};
        if what not in terms["url"]: terms["url"][what] = {};
        terms["url"][what][where] = int(re.search(r'-?\d+', line)[0]);        
      except TypeError:
        print('Ошибка в файле правил (строка ' + str(i) + ')');

    else:
      try:
        key = re.search(r'(\w+) \w+ \S+ -?\d+', line)[1];
        where = re.search(r'\w+ (\w+) \S+ -?\d+', line)[1];
        what = re.search(r'\w+ \w+ (\S+) -?\d+', line)[1].split("/");
        what = tuple(what);
        pr = re.search(r'\w+ \w+ \S+ (-?\d+)', line)[1];
        
        if key not in terms: terms[key] = {};
        if what not in terms[key]: terms[key][what] = {};
        terms[key][what][where] = int(pr);
      except TypeError:
        print('Ошибка в файле правил (строка ' + str(i) + ')');

  return terms;