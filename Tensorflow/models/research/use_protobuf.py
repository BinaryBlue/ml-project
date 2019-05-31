import os
import sys

#args = sys.argv
directory = "object_detection/protos";
protocpath = "/Users/jasimuddin/ml-python/ml-project/oDetection/bin/protoc"

for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protocpath+" "+directory+"/"+file+" --python_out=.")

