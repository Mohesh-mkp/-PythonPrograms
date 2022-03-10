input_str = print("Enter a sentence: ")
sub_str_to_search = ("Enter the word to search: ")

input_str_index=0

sub_str_to_search_len = len(sub_str_to_search)

if input_str(input_str_index:(input_str_index+sub_str_to_search_len)) == sub_str_to_search:
    input_str_index+=1
    print ("The word {} repeated {} in the given sentence".format(sub_str_to_search,input_str_index))
else:
    print("Search failed, Try Again! ")

#######################################################################################################################

input_str = input("Enetr a sentence: ")
input_str_to_search = input("Enter word to search: ")

word_list = []

input_str_index = 0
sub_str_len = len(input_str_to_search)
str_len = len(input_str)
'''print(sub_str_len)'''

while input_str_index < str_len:
    '''print(input_str[input_str_index:input_str_index+sub_str_len])'''
    if input_str[input_str_index:input_str_index+sub_str_len] == input_str_to_search:
        print(input_str_index)
    input_str_index+=1
    
