from nltk import Tree
import nltk
import argparse
import pandas as pandas
from nltk import Nonterminal
#from nltk.corpus import treebank
#from nltk import treetransforms
from nltk import induce_pcfg
from nltk.parse import pchart
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--trees_file', default='../trees/trees-collins-head-rules/processed_ptb-collins.merge1.txt', help="location of tree")
parser.add_argument('--store_gram_dir', default='./csv/desired_merged_grammer.csv', help="generated PCFG file in csv")
parser.add_argument('--len_endsym', default=10, help="length of end symbol ")
parser.add_argument('--collaspe', default=False, help="Collapse subtrees with a single child (ie. unary productions) into a new non-terminal (Tree node) joined by ‘+’")
parser.add_argument('--chomsky', default=False, help="convert trees in chomsky normal ")



def grammar2csv(grammar, store_gram_dir):
    """
    generate production rules in csv formate 
    """

    lhs = [l.lhs() for l in grammar.productions()]
    rhs = []
    rhs_n = 1 

    for r in grammar.productions():
        rhs.append(r.rhs())
        rhs_n = max(rhs_n, len(r.rhs()))
    #print(rhs_n)

    list_list_rhs = []
    for i in range(rhs_n):
        list_rhs = []
        for r in grammar.productions():
            try:
                list_rhs.append(r.rhs()[i])
            except:
                list_rhs.append("nan")
        list_list_rhs.append(list_rhs)
    
    prob = [ p.prob() for p in grammar.productions(())]
    dict = {'probability': prob, 'start_symbol': lhs}

    for i in range(rhs_n):
        dict["end_symbol"+str(i)] = list_list_rhs[i]
    dict["end_symbols"] = rhs

    df = pd.DataFrame(dict)   
    # saving the dataframe 
    df.to_csv(args.store_gram_dir, index=False) 

if (__name__ == "__main__"):
    args = parser.parse_args()
    trees_file = open(args.trees_file, 'r')
    lines = trees_file.readlines()
    list_lines = [line for line in lines]
    trees_file.close()

    """
        Example of tree in trees
          ex = nltk.Tree.fromstring("( (S (NP (NNP Ms.) (NNP Haag)) (VP (VBZ plays) (NP (NNP Elianti))) (. .)))")
    """
    trees = []
    
    count=0
    for line_ind,line in enumerate(list_lines):
        try:
            # adding ROOT as start symbol
            t = "(ROOT"+str(line[1:-1]) 
            trees.append(nltk.Tree.fromstring(t))
        except:
            print("error in the line index ")
            print(line_ind)
            count = count+1
            continue 
    print("follwing number of lines are showing error: "+str(count))
    

    productions = []
    rej_tree = 0
    for tree in trees:
        if collaspe:
            tree.collapse_unary()# Remove branches A-B-C into A-B+C
        if chomsky:
            tree.chomsky_normal_form(horzMarkov = 0)# Remove A->(B,C,D) into A->B,C+D->D
        
        counter =0
        for pro in tree.productions():
            if len(pro.rhs()) >args.len_endsym:
                 counter = -1
                 break
        if counter == -1 :
            rej_tree = rej_tree + 1
            continue
        productions += tree.productions()# CFGs
    print("following number of trees got reject due to long rhs or end symbols in their CFG form {}", rej_tree)


    S = Nonterminal('ROOT' ) # start nonterminal
    grammar = induce_pcfg(S, productions)

    grammar2csv(grammar, args.store_gram_dir)
    print("Done")
