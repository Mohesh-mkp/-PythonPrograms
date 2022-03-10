count=0
input_str = input("Enter a senetence: ")
vowels_list = ['aeiouAEIOU']
for words in input_str:
    for vowels in vowels_list:
        for vowel in vowels:
            if words == vowel:
                count+=1
if count != 0:
    print("The number of vowels present in sentence are: ",count)
else:
    print("No vowels present in sentence")


