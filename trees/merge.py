
if (__name__ == "__main__"):

    filenames = ['ptb-collins.train02-21.txt', 'ptb-collins.dev22.txt', 'ptb-collins.test23.txt']
  
# Open file3 in write mode
    with open('ptb-collins.merge.txt', 'w') as outfile:
  
    # Iterate through list
        for names in filenames:
  
        # Open each file in read mode
            with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
                outfile.write(infile.read())
  
            # Add '\n' to enter data of file2
            # from next line
            outfile.write("\n")
