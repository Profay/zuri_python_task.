# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#iporting string to remove punctuations
import string


def read_file_content(filename):
	#With is specified with open to automatically close file when not accessed.
   with open(filename) as file:
	   contents = file.read()
	   print(contents)
   return filename #Since the function return in strings, counting words from string is not plausible thus, filename is returned.


def count_words():
	#./story.txt is not recognized thus the path needs to be specified.
    text = read_file_content("/workspace/zuri_python_task./Reading-Text-Files/story.txt")
	#The file is close after opening with "with open", The above function return path to the file to text.
    contents = open(text, "r") 
	#initializing dictionary
    d = dict()
    for line in contents:
		#striping lines both side
	    line = line.strip()
		#coverting all case to lower to avoid casematcth and removing punctuations
	    line = line.lower().translate(line.maketrans("", "", string.punctuation))
		#spliting words 
	    lines = line.split(" ")
		#referecing word to dictionary and increment of word by one if already appear
	    for word in lines:
		    if word in d:
			    d[word] = d[word] + 1
		    else:
			    d[word] = 1
	#looping through dictionary
    for key in list(d.keys()):
	    print(key, ":", d[key])
    
   		#return {key, d[key]}
#passing the path to file to the function
#read_file_content("/workspace/zuri_python_task./Reading-Text-Files/story.txt")
count_words()