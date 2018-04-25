# 
import os 
import argparse
import audioread


# parse command line input
PARSER = argparse.ArgumentParser(description=
					"""
					

					"""	)

PARSER.add_argument('-i', '--infile', help=
					"""
					Name of input files.
					"""
					, default="", required=False)

PARSER.add_argument('-I', '--input_dir', default = "", help = "input dir for multi files")
ARGS = PARSER.parse_args()

if __name__ == '__main__':
	
	if ARGS.input_dir:
		for in_file in os.listdir(ARGS.input_dir):
			os.system(" bazel run tensorflow/examples/speech_commands:test_streaming_accuracy --  --graph=/tmp/speech_commands_train_20180321-161243.pb --labels=/tmp/speech_commands_train/conv_labels1.txt --wav="+ARGS.input_dir+in_file+" --verbose")


	else:
		os.system(" bazel run tensorflow/examples/speech_commands:test_streaming_accuracy --  --graph=/tmp/speech_commands_train_20180321-161243.pb --labels=/tmp/speech_commands_train/conv_labels1.txt --wav="+ARGS.infile+" --verbose ")
# os.system("./run.sh")
