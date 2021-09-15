# MCS 260 Fall 2020 Project 3
# Abdul Shaqildi
# Declaration: I, Abdul Shaqildi, am the sole author of this code, which
# was developed in accordance with the rules in the course syllabus.
def substitute(vars,s):
 """Accepts a dictionary vars of templating variables and a string s
 and replaces references to templating variables in s with the values of those variables in vars,
 returning the result."""
 
 for k in vars.keys():
     s = s.replace(k, vars[k])
     
 return s



