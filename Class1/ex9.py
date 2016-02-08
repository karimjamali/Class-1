#/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint

def main():

 cfg=CiscoConfParse('Config-file.txt')
 temp_list=cfg.find_objects_w_child(parentspec=r"^crypto map", childspec="pfs group2")

 #for entry in temp_list:

 for entry in temp_list:
   print "Crypto Map " , entry.text , " is using PFS Group 2"

 # temporary=entry.children
 # for item in temporary:
 #  print item.text
  

if __name__ == "__main__":
   main()
