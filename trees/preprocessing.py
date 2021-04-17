from nltk import Tree
import nltk
import argparse
import pandas as pandas
import pandas as pd

def get_brac_ind(word):
    for i, brac in enumerate(word):
        if brac ==')':
            return(i)
def rmsym(sym, tokens):
    if sym in tokens:
        if ')'in tokens:  
            index_barc = get_brac_ind(tokens.split(sym,1)[1])
            tokens = tokens.split(sym,1)[0] + tokens.split(sym,1)[1][index_barc:]
            return tokens
        else:
            tokens =  tokens.split(sym, 1)[0]
            return tokens
    return tokens

    
parser = argparse.ArgumentParser()
parser.add_argument('--infile', default='./ptb-collins.merge.txt', help="preprocessing tree")
#parser.add_argument('--seed', type=int, default=2004, help="random seed for initialization")
parser.add_argument('--outfile', default='./processed_ptb-collins.merge1.txt', help="file containing logs")

if (__name__ == "__main__"):
    args = parser.parse_args()
    trees_file = open(args.infile, 'r')
    lines = trees_file.readlines()
    list_lines = [line for line in lines]
    trees_file.close()
    processed_lines = []
    for list_line in list_lines:
        ls=[]
        for tokens in list_line.split():
            if tokens[0] == "(":
                try:   
                    if tokens[1] in string.ascii_letters:
                        tokens = rmsym('-',tokens)
                        tokens = rmsym('=', tokens)
                        tokens = rmsym('|', tokens)
                        tokens = rmsym('$', tokens)
                        tokens = rmsym('#', tokens)
                        tokens = rmsym('+', tokens)
                except:
                    print("some bugs")        

            ls.append(tokens)
        processed_line = " ".join(ls)
        processed_lines.append(processed_line)

    f=open(args.outfile,'w')
    for ele in processed_lines:
        f.write(ele+'\n')

    f.close()
    print("Pre-processing is done")