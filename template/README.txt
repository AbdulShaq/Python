Examples of template.py input and output
---------------------------------------

Processing in1.txt with template.py produces out1.html with vars1.dat substitutions using varsub.py
Processing in2.txt with template.py produces out2.html with vars2.dat substitutions using varsub.py

Thus, for example, the command to produce out1.html might be

python ..\template.py vars1.dat in1.txt out1.html

assuming template.py is in the parent directory and in1.txt and vars1.dat is in the
current directory.

template.py will write the text in the txt document in html format reading line starting with '@' as bullet points,
starting with '#' as comments (that will be ignored), and any variable name from the dat file between 2 '$' as a place
for variable substitution. and anything else as regular paragraph form

the dat file will provide the variable assignment, txt file provides what needs to be written and the html file is 
where the txt file iinformation with the proper substitutions will be written
 

