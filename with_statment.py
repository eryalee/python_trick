#!/usr/bin/python

#Warning: python version >= 2.5 using with..as statement

def filter(txt, oldfile, newfile):
    '''
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text 
    after the name before appending the line to the output file.
    '''
    with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
        for line in infile:
            if line.startswith(txt):
                line = line[0:len(txt)] + "- Truly a great person!\n"
            outfile.write(line)

if __name__ == '__main__':
    text = input('Please enter the name of a great person')
    filter(text, 'log', 'log.1')
