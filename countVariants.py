# NAME: Lavanya Uppala
# EMAIL: lvu06382@creighton.edu
#
# Partners: NONE
#
# The program reads in a .txt file, extracts the appropriate columns,
# such as the variant type and patient-family identification id
# and then returns a .csv which summarizes the different mutations by
# family and type
# -i name of the input file, if nonexistent then input will be read
#       from standard input
# -o name of the output file, if nonexistent then input will be sent
#       to standard output

import sys
import getopt
import re
import pandas as pd
import csv

class countVariants:

    # outputs usage information such as command line options/arguments
    def usage(self):
        print("Usage: FindSeq [-i FILE] [-o FILE] [-c CHROMOSOME]")
        print("\t-i: input file (.txt, tab-delimited); STDIN if not used.")
        print("\t-o: output file (.csv-formatted); STDOUT if not used.")

    def main(self):

        try:
            # reads in arguments from the command line
            opts, args = getopt.getopt(sys.argv[1:], "i:o:c")
            
            input_file_name = ""
            output_file_name = ""

            # sets values of variables depending on command line arguments
            for (opt, arg) in opts:
                if opt == "-i":
                    input_file_name = arg
                elif opt == "-o":
                    output_file_name = arg

        
        # CHANGE THIS LINE TO SPECIFY THE INPUT FILE
        # input_file_name = ""

        # CHANGE THIS LINE TO SPECIFY THE OUTPUT FILE
        # output_file_name = ""


        # exception handling for invalid options
        except getopt.GetoptError as err:
            sys.stdout = sys.stderr
            print(str(err))
            self.usage()
            sys.exit(2)

        # list which stores all the lines read in from input
        file_input = []

        # file to be read
        inFile = ""

        if input_file_name == "":
            inFile = sys.stdin
        else:
            inFile = open(input_file_name, "r")

        # reads in the entirety of the .txt file
        reader = csv.reader(inFile, delimiter="\t")
        d = list(reader)
        print(d)

        # where output is sent, default stdout
        outPut = sys.stdout

        # outputs text to screen or file depending on option argument
        if output_file_name != "":
            outPut = open(output_file_name, "w")

        outPut.close()

        


# creates an object of the FindSeq class to use functionality
# of the class's main method
objectTest = countVariants()
objectTest.main()