for i in range(0,151,1):
    print(i)

for i in range(5,1000000,5):
    print(i)

for i in range(1,101,1):
    if i%10 == 0:
        print(i,"Dojo")
    elif i%5 ==0:
        print(i,"Coding")
    else: 
        print(i)

sum = 0
for i in range(0,500001,1):
    if i%2 != 0:
        sum = sum + i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum +1,1):
    if i > 0:
        if i%mult == 0:
            print(i)

# 3,5,1,2

# error: 'list' object cannot be interpreted as an integer

# 0,1,2,3