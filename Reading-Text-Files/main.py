# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
   with open('/workspace/zuri_python_task./Reading-Text-Files/story.txt') as file:
    contents = file.read()
    print(contents)
    return "Hello World"


def count_words():
    text = open("/workspace/zuri_python_task./Reading-Text-Files/story.txt", "r")
    d = dict()
    for line in text:
	    line = line.strip()
	    line = line.lower()
	    words = line.split(" ")
	    for word in words:
		    if word in d:
			    d[word] = d[word] + 1
		    else:
			    d[word] = 1
    for key in list(d.keys()):
	    print(key, ":", d[key])
    
   
#return {"as": 10, "would": 20}

read_file_content("./story.txt")
count_words()