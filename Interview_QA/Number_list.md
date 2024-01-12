### Write a program in a language of your choice to find all six-digit numbers which have same digits as the original number when multiplied by 2.

```python
def find_matching_numbers():
    num_list = []
    for num in range(100000, 1000000):
        st_num = str(num)
        end_num = str(num * 2)
        if sorted(st_num) == sorted(end_num):
            num_list.append(num)
    return num_list

matching_numbers = find_matching_numbers()
print(f'Six-digit numbers with the same digits when multiplied by 2:\n{matching_numbers}')

```
