#!/usr/bin/env python3
###############################################################################
# Copyright 2019 Matthew Khouzam
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
###############################################################################

import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description='Generates a subtitle file with evenly spread subtitles from a text file.')
parser.add_argument('-i','--input',  help='The input file', required=True)
parser.add_argument('-d','--duration', help='The duration of the video in seconds', required=True)

args = parser.parse_args()


if __name__=='__main__':
   inputfile = args.input
   duration = float(args.duration)
   num_lines = sum(1 for line in open(inputfile))
   step = (duration - (num_lines/2)) / num_lines
   i = 0
   time = 0.5
   for line in open(inputfile):
        i = i+1
        print(i)
        h1 = int(int(time) / 3600)
        m1 = int(int(time) / 60)
        s1 = int(time%60)
        d1 = int((time - int(time))* 1000 % 1000)
        time = time + step + 0.5
        h2 = int(int(time) / 3600)
        m2 = int(int(time) / 60)
        s2 = int(int(time%60))
        d2 = int((time - int(time)) * 1000 % 1000)

        print("{}:{}:{},{} --> {}:{}:{},{}".format( h1,m1,s1,d1,h2,m2,s2,d2))
        print(line)

