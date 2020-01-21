import sys
import os
import data_cleaner

args = sys.argv
args = args[1:]

fantasy="clean_fantasy"
lit="clean_literature"
res="clean_research_paper"

for i in range(len(args)):
    if(str(args[i])=="fan"):
        args[i]=fantasy
    elif(str(args[i])=="lit"):
        args[i]=lit
    elif(str(args[i])=="res"):
        args[i]=res
    else:
        print(args[i]+" Not a proper argument")
        continue

#clean_data = data_cleaner.data_loader(args)

