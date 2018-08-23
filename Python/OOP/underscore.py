class Underscore:
    def map(self,l,f):
        for i in range(len(l)):
            l[i] = f(l[i])
        return l
    def reduce(self,l,f):
        memo = l[0]
        for i in range(1,len(l)):
            memo = f(memo, l[i])
        return memo
    def find(self,l,f):
        for i in range(len(l)):
            if f(l[i]) == True:
                return l[i]
        return False
    def filter(self,L,F):
        pass
    def reject(self):
        pass
        
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

map1 = _.map([1,2,3], lambda x: x*3)
print(map1)

redused = _.reduce([1,2,3,4,5,6], lambda memo,x: memo + x)
print(redused)

found = _.find([1,2,4,5,6,9,10,11,12,1,3,14], lambda x: x % 30 ==0)
print(found)

