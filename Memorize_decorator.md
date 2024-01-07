
```python
memory = {}
def memo_decorator(func):
    def wrap(num):
        if num not in memory:
            res = func(num)
            memory[num] = res
            print('Result saved in memory')
        else:
            print('Returning value from memory')
            res = memory[num]
        return res
    return wrap

@memo_decorator
def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num-1)

try:
    base = int(input('Enter a value: '))
    print(fact(base))
except:
    print('Try with valid number')
```
