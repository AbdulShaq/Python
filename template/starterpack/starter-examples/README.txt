Examples of starter.py input and output
---------------------------------------

Processing in1.txt with starter.py produces out1.html
Processing in2.txt with starter.py produces out2.html

Thus, for example, the command to produce out1.html might be

python ..\starter.py in1.txt out1.html

assuming starter.py is in the parent directory and in1.txt is in the
current directory.

WARNING!! If you want to test starter.py, you should be careful to
avoid overwriting the example output files, which the command given
above would do.  A better way to test would be with a command like:

python ..\starter.py in1.txt test1.html

Then you should check that test1.html (that you just produced) and
out1.html (included with the starter pack) are identical.
