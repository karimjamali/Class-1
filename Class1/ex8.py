#/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint

def main():

 cfg=CiscoConfParse('Config-file.txt')
 temp_list=cfg.find_objects(r"^crypto map CRYPTO")

 for entry in temp_list:
  print "Entry ", entry.text
  temporary=entry.children
  for item in temporary:
   print item.text
  

if __name__ == "__main__":
   main()
