
input_str = input("Enter a string: ")
sub_strs = input("Enter substrings to search for: ")

sub_str_list = sub_strs.split()

input_str_list = input_str.split()
print(input_str_list)

for sub_str in sub_str_list:
    count = 0
    for word in input_str_list:
        if word == sub_str:
            count+=1
    print("The sub_str = {} appeared {} number of times ".format(sub_str, count))
