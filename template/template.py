"""Text to HTML converter supporting bullet lists and variable replacement"""
# MCS 260 Fall 2020 Project 3
# Abdul Shaqildi
# Declaration: I, Abdul Shaqildi, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus.

import sys
import varsub

if len(sys.argv) != 4:
    print("Usage: {} INFILE OUTFILE".format(sys.argv[0]))
    print("The text file INFILE is then converted to an HTML file OUTFILE and the DAT file is FILLERFILE provides text replacement (if any) for the HTML file.")
    sys.exit()

Fillfn = sys.argv[1]
infn = sys.argv[2]
outfn = sys.argv[3]

# open input and output files
fin = open(infn,"r")
fout = open(outfn,"w")

File = open(Fillfn, "r") #opens and reads the dat file
filler = {}

for text in File:
    #creates dictionary and saves it to a larger dictionary
     line = text.split('=') 
     one = '$'+line[0]+'$'
     two = line[1]
     Dict = {one:two}
     filler.update(Dict)
File.close()
 

# print header
fout.write("<!DOCTYPE html>\n")
fout.write("<html>\n")
fout.write("<head><title>HTML document</title></head>\n")
fout.write("<body>\n")
opentags = []  # Stack containing open tags inside <body>
               # (only a single p tag, in this program)
for line in fin:
    isblank = not bool(line.strip())
    if opentags and isblank:
        # Pop the currently open p tag off the stack
        # and close it.  Here we rely on the fact that
        # only one tag will be open when we reach this line.
        fout.write("</{}>\n".format(opentags.pop()))
    if not isblank:
        # Line is not blank, must appear in output
        if not opentags: # if opentags is empty 

            if line[0]=='#': #if the line starts with a # then dont write it
               fout.write(" ")

            elif line[0]=='@': #if it starts with @ its a bullet point
               fout.write("<ul>\n") #starts unordered line
               opentags.append("ul")
               Newline = varsub.substitute(filler, line)
               fout.write("<li>\n") #starts li tag
               fout.write(Newline.replace('@',''))
               fout.write("</li>\n")  #ends li tag

            else: 
               fout.write("<p>\n") #start a paragraph
               opentags.append("p")
               Newline = varsub.substitute(filler, line)
               fout.write(Newline)
        
        elif line[0]=='#': #if opentags is not empty and the line starts with a # then dont write it
            fout.write(" ")

        elif line[0]=='@': #if opentags is not empty and it starts with @ its a bullet point

            if 'ul' not in opentags:
               fout.write("</{}>\n".format(opentags.pop()))
               fout.write("<ul>\n")
               opentags.append("ul")
               Newline = varsub.substitute(filler, line)
               fout.write("<li>\n")
               fout.write(Newline.replace('@',''))
               fout.write("</li>\n")

            elif 'ul' in opentags:
               Newline = varsub.substitute(filler, line)
               fout.write("<li>\n")
               fout.write(Newline.replace('@',''))
               fout.write("</li>\n")
        
        else:
            if 'p' in opentags:
                Newline = varsub.substitute(filler, line)
                fout.write(Newline)

            if 'p' not in opentags:
               fout.write("</{}>\n".format(opentags.pop()))
               fout.write("<p>\n")
               opentags.append("p")
               Newline = varsub.substitute(filler, line)
               fout.write(line)
# done reading from input file
fin.close()

# close all open tags in the body
while opentags:
    fout.write("</{}>\n".format(opentags.pop()))

# print the standard footer that closes body and html tags
fout.write("</body>\n")
fout.write("</html>\n")

# done writing to output file
fout.close()

