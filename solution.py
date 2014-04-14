#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
from json import dumps

def output(dictionary):    
    print(dumps(dictionary, sort_keys=True))

def solve_challenge(file_path):
    """ This is the heart of the script """
    with open(file_path) as hul:
        list_line = hul.readlines()

    prev_list_line = []
    for i, line in enumerate(list_line):
        # save the contents until we find ### which means the start of the queries 
        if line.startswith("###"):
            # go through the queries
            for next_line in list_line[i+1:]:
                list_elems = next_line.strip().split(",")
                validated_list = []

                # search for the lines containing all the queried keywords
                for prev_line in prev_list_line:
                    passed = True
                    for elem in list_elems:
                        if not elem in prev_line:
                            passed=False
                            break
                    if passed:
                        validated_list.extend([elem for elem in prev_line if not elem in list_elems])
                # print the results
                output(dict((k, validated_list.count(k)) for i, k in enumerate(validated_list) if not k in validated_list[:i]))
            break
        else:
            prev_list_line.append(line.strip().split(","))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', action="store", dest="input", 
                        required=True,
                        help='The input file')

    ns = parser.parse_args()

    input_filepath = ns.input

    solve_challenge(input_filepath)