def primo(num):
    if x % 2 == 0 and x > 2:
        False
    return (all(num%i for i in range(3,int((num**0.5)+1),2)))
rept = int(input())
for x in range(rept):
    if primo(int(input())): print('Prime')
    else: print('Not Prime')
    