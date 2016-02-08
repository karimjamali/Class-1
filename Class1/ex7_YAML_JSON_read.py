#!/usr/bin/env/python

import yaml
import json
from pprint import pprint

def output_format(my_list, my_str):
   
   # Make the output format easier to read
   # '''
    
    print "Converting from " , my_str ,"FORMAT"
    print "#" * 30
    pprint (my_list)



def main():

#my_dict={'karim':'32','yasmine':'26','amine':'1','dad':'76','mum':'67'}
 
 yaml_output="yaml_output.yml"
 json_output="json_output.json"

 json_list=[]
 yaml_list=[]

 with open(yaml_output,"r") as f:
    yaml_list=yaml.load(f) 


 with open(json_output,"r") as f:
    json_list=json.load(f)
 
 print "JSON_LIST: ", output_format(json_list,'JSON')
 print "YAML_LIST: ",output_format(yaml_list,'YAML')
 
 
if __name__ == '__main__':
   main()
