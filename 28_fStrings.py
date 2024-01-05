# fstrings are same as template litereal in javascript and typescript i.e. use variables in strings

name = "Deependra Parmar"
college = "AITR"
course = "B.Tech."
semester = 6

sentence = "Hello, my name is {}. I am currently in {}th semester of pursuing {} from {}"
# Previously, it is done like this way 
print(sentence.format(name,semester,course,college))


# now, we can use fstrings in python 
print(f"Hello, my name is {name}. I am currently in {semester}th semester of pursuing {course} from {college}")