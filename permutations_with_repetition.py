# Python program to print all permutations with repetition 
# of characters 

__Nconf=0

def toString(List): 
	return ''.join(List) 

# The main function that recursively prints all repeated 
# permutations of the given string. It uses data[] to store 
# all permutations one by one 
def allLexicographicRecur(string, data, last, index, configuration): 
    global __Nconf
    length=len(string) 
	# One by one fix all characters at the given index and 
	# recur for the subsequent indexes 
    for i in range(length): 
		# Fix the ith character at index and if this is not 
		# the last index then recursively call for higher 
		# indexes
        data[index]=string[i]

        # If this is the last index then print the string 
        # stored in data[] 
        if index==last:
            configuration[__Nconf]=toString(data)
            __Nconf+=1
            #print(f'{Nconf:6d} {toString(data)}')
        else:
            allLexicographicRecur(string, data, last, index+1, configuration)

# This function sorts input string, allocate memory for data 
# (needed for allLexicographicRecur()) and calls 
# allLexicographicRecur() for printing all permutations 
def allLexicographic(string,sequence=-1): 
    if sequence==-1: length=len(string) 
    else: length=sequence

    # allocate list to store all permutations
    configuration=[None]*len(string)**length

	# Create a temp array that will be used by 
	# allLexicographicRecur() 
    data=[""]*(length+1)
    
	# Sort the input string so that we get all output strings in 
	# lexicographically sorted order 
    string=sorted(string)
    
    # Now print all permutaions 
    allLexicographicRecur(string, data, length-1, 0, configuration)
    return configuration
    

if __name__=='__main__':
    # Driver program to test the above functions 
    string="01"
    size=8
    Nperm=len(string)**size
    print(f'Calculating {Nperm} permutations')
    print(f'All permutations with repetition of {string} of length {size} are:')
    conf=allLexicographic(string,sequence=size)
    for i,c in enumerate(conf): print(f'{i:6d} {c}')
    print(f'Total Number: {__Nconf}')

# This code is contributed to Bhavya Jain 
