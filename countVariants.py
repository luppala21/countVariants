# NAME: Lavanya Uppala
# EMAIL: lvu06382@creighton.edu
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

class countVariants:

    # outputs usage information such as command line options/arguments
    def usage(self):
        print("Usage: countVariants [-i FILE] [-o FILE]")
        print("\t-i: input file (.txt, tab-delimited); STDIN if not used.")
        print("\t-o: output file (.csv-formatted); STDOUT if not used.")

    def main(self):

        # CHANGE THIS LINE TO SPECIFY THE INPUT FILE
        input_file_name = "vcfFile-long.txt"

        # CHANGE THIS LINE TO SPECIFY THE OUTPUT FILE
        output_file_name = "variantCounts.csv"

        try:
            # reads in arguments from the command line
            opts, args = getopt.getopt(sys.argv[1:], "i:o:c")
            
            

            # sets values of variables depending on command line arguments
            for (opt, args) in opts:
                if opt == "-i":
                    input_file_name = args
                elif opt == "-o":
                    output_file_name = args


        # exception handling for invalid options
        except getopt.GetoptError as err:
            sys.stdout = sys.stderr
            print(str(err))
            self.usage()
            sys.exit(2)

        # sets the input location of the program, stdin if not specified
        if input_file_name == "":
            inFile = sys.stdin
        else:
            inFile = open(input_file_name, "r")

        # reads in the entirety of the .txt file
        patient_ids = pd.read_csv(input_file_name, delimiter="\t",
                                        dtype=str, header=(0), lineterminator="\n")

        # this drops the first 8 columns of the vcf file which is
        # extraneous data that's not needed
        patient_ids = patient_ids.drop(patient_ids.columns[0:9], axis=1)

        family_id = []
        countWildtype = []
        countHetVar = []
        countHomoVar = []

        for column in patient_ids:
            wildtypeVar = 0
            hetVar = 0
            homoVar = 0

            # this is the list of variants associated with a specific patient
            for i in range(len(patient_ids[column])):

                # this loop makes a running count of the different
                # mutation types associated with each patient
                if patient_ids[column][i] != ".:.:.:.:.:.:.:.":
                   
                   # gets the variant type as a string
                    variantType = patient_ids[column][i][0:3]
                   
                    if variantType == "0/0":
                        wildtypeVar = wildtypeVar + 1
                    elif variantType == "0/1":
                        hetVar = hetVar + 1
                    elif variantType == "1/1":
                        homoVar = homoVar + 1
            
            family_id.append(column.strip())
            countWildtype.append(wildtypeVar)
            countHetVar.append(hetVar)
            countHomoVar.append(homoVar)

        variantCounts = pd.DataFrame({"family_id": family_id,
                                      "countWildType": countWildtype,
                                      "countHetVar": countHetVar,
                                      "countHomoVar": countHomoVar})

        # where output is sent, default stdout
        outPut = sys.stdout

        # outputs text to screen or file depending on option argument
        if output_file_name != "":
            outPut = open(output_file_name, "w")
        
        variantCounts.to_csv(output_file_name, sep=",", encoding="utf-8", index=False)

        outPut.close()
        inFile.close()

        


# creates an object of the FindSeq class to use functionality
# of the class's main method
objectTest = countVariants()
objectTest.main()