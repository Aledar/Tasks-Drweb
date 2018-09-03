#!/usr/bin/env python3

import subprocess
import time
import re
from sys import argv

def searchDate(string):	
	date = re.search(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d', string)[0];
	return date;

def searchNs(string):
	ns = re.search(r'\S+:\s+(\S+)', string)[1];
	return ns;

def searchOrg(string):
	org = re.search(r'\S+:\s+(.+)', string)[1];
	return org;

def toStruct(string):
	try:
		string = time.strptime(string, "%Y-%m-%dT%H:%M:%SZ");
	except ValueError:
		try:
			string = time.strptime(string, "%Y-%m-%dT%H:%M:%S");
		except ValueError:
			string = time.strptime(string, "%Y-%m-%d");
	return string;

def fromWhois(cmd):
	stringsWhois = subprocess.check_output(cmd, universal_newlines=True).split("\n")

	output = [];
	flag = False;
	for string in stringsWhois:
		if string.lower().startswith("creation date:") or string.lower().startswith("created:"):
			output.append(searchDate(string));
			output[0] = toStruct(output[0]);
			flag = True;
			break;

	if flag:
		for string in stringsWhois:
			if string.lower().startswith("name server:") or string.lower().startswith("nserver:"):
				output.append(searchNs(string));
			if string.lower().startswith("org:"):
				output.append(searchOrg(string));
	else:
		output = False;

	if output:
		for line in output:
			print(line);
	else:
		print(False);


try:
	cmd = ["whois", argv[1]];
	fromWhois(cmd);
except:
	print("Run program with domain");


