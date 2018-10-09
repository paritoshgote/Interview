my_string = "abdeghsajk"

#Approach 1 No Data Structure:

def isUnique1(my_string):
	
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for i in my_string:
		if i in alphabet:
			alphabet = alphabet.replace(i, "")
		else:
			return False
	return True

print(isUnique1(my_string))


#Approach 2 Dictionary:

def isUnique2(my_string):

	my_dict = {}

	for i in my_string:
		if i in my_dict:
			return False
		else:
			my_dict[i] = 1
	return True

print(isUnique2(my_string))