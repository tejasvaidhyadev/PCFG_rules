# PCFG_rules  

The Repository contains code to generate and generated production-rules for the following languages.
- [Basque](production_rules_PCFG/Basque.csv), 
- [English](production_rules_PCFG/English.csv),
- [French](production_rules_PCFG/French.csv),
- [German](production_rules_PCFG/German.csv),
- [Hebrew](production_rules_PCFG/Hebrew.csv),
- [Hungarian](production_rules_PCFG/Hungarian.csv),
- [Korean](production_rules_PCFG/Korean.csv),
- [Polish](production_rules_PCFG/Polish.csv),
- [Swedish](production_rules_PCFG/Swedish.csv)

## Tree banks  

 The following treebanks are used to generate above results
- [English data](https://catalog.ldc.upenn.edu/LDC99T42)
- Non-English data are from SPMRL 2013/2014 Shared Tasks   
  - Request data from the organizers by following these [steps](https://dokufarm.phil.hhu.de/spmrl2013/doku.php?id=how_to_obtain_licenses_for_the_shared_task_data)

## Directory Struture  

- ```codes```: contains code to generate production rules used for each langues.
- ```production_rules_PCFG```: Contains the production rules in csv format.
- ```trees```: script to preprocess trees(in labelled bracketed data formate).

## Dependencies

| Dependency                  | Version | Installation Command                                                |
| ----------                  | ------- | ------------------------------------------------------------------- |
| Python                      | 3.8.5   | `conda create --name pcfg python=3.8` and `conda activate pcfg` |
| nltk                        | 1.5.0   | `pip install --user -U nltk`            |
| pandas                      | 1.5.0   | `pip install --user -U nltk`            |
| argparse                    | 0.20.3  | `pip install pandas=0.20.3`             |


## Instructions  

### 1. Setting up the codebase and the dependencies.
- Clone this repository - ```git clone https://github.com/tejasvaidhyadev/PCFG_rules.git```
- Follow the instructions from the Dependencies Section above to install the dependencies.

### 2. Instruction for Generating production-rules  

```
python trees/preprocessing.py --infile trees.ptb --outfile processed_trees.ptb
```
To generate production rules

```
python codes/pcfg.py --trees_file processed_trees.ptb --store_gram_dir English.csv
```
## Miscellanous  

- License: MIT

