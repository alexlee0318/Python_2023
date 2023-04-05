fruits = ['감', '밤', '배']
try:
    print(fruits[3])
except:
    print('IndexError예외 발생')

#     D:\Workspace\02.Python\06.예외처리>python test.py
# ->IndexError예외 발생
# -> 5050

sum = 0
for i in range(1, 101):
    sum += i
    
print(sum)
