#/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint
import re
def main():

 cfg=CiscoConfParse('Config-file.txt')
 temp_list=cfg.find_objects_wo_child(parentspec=r"^crypto map", childspec="AES")

 #print temp_list
 
 for entry in temp_list:
  for child in entry.children:
   if "transform" in child.text:
    match=re.search(r"set transform-set (.*)$", child.text)
    encryption=match.group(1)
   # print encryption

 print "Entry not using AES is " , entry.text , " and its encryption is " , encryption

#for entry in temp_list:

 #for entry in temp_list:
 #  print "Crypto Map not using AES " , entry.text 
   
 # temporary=entry.children
 # for item in temporary:
 #  print item.text
  

if __name__ == "__main__":
   main()
