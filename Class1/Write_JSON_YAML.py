#!/usr/bin/env/python

import yaml
import json
import pprint


def main():

#my_dict={'karim':'32','yasmine':'26','amine':'1','dad':'76','mum':'67'}
 
 yaml_output="yaml_output.yml"
 json_output="json_output.json"
 my_dict={}
 my_dict['karim']='32'
 my_dict['yasmine']='26'
 my_dict['amine']='1'
 my_dict['dad']='76'
 my_dict['mum']='67'
 my_list=['Cisco','Juniper','BMB Group',my_dict,'BTAT']
 print my_list

 with open(yaml_output, "w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))

 with open(json_output, "w") as f:
    json.dump(my_list,f)


if __name__ == '__main__':
   main()
