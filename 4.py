#!/usr/bin/env python3

#Поиск SegmentationFault
def searchSegmentationFault(path):
  f = open(path, 'r');
  output = [''];
  flag = 0;
  i = 0;

  for line in f:    
    output[i], flag = search(line, output[i], flag)
    if flag == 2:
      i += 1;
      output.append('');
      flag = 0;

  f.close();

  for record in output:
    print(record);

#Поиск всех частей лога SegmentationFault
def search(line, output, flag):    
  patterns = ['Segmentation fault', 'EAX=', 'ESI=', 'ESP=', 'EIP=', 'pid='];
  i = -1;

  while(True):
    if i == 5:
      i = -1;
      break;

    i += 1;    
    index = line.find(patterns[i]);
    
    if index >= 0:
      break;

  if i == 0:
    output = 'SF_AT: ' + line[index + 22:];    
  elif not flag: return (output, 0);
  elif i == 1:    
    output += 'SF_TEXT:\n' + line[index:];
  elif 2 <= i <=4:    
    output += line[index:];
  elif i == 5:    
    output = 'PID: ' + line[index + 4:] + output;    
    return (output, 2);

  return (output, 1);


searchSegmentationFault('log.txt');
