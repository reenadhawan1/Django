import unittest

def reverseList(arr):
    for i in range(int(len(arr)/2)):
        hold = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = hold
    # arr.reverse()
    return arr

def isPalindrome(randStr):
    randStr = randStr.upper()
    for i in range(int(len(randStr)/2)):
        if randStr[i] != randStr[-1 -i]:
            return False
    return True

def coins(monies):
    d = {
        'q' : 25,
        'd' : 10,
        'n' : 5,
        'p' : 1,
        }
    totalCoins = []
    for i in d:
        count = int(monies / d[i])
        totalCoins.append(count)
        monies -= d[i] * count
    return totalCoins


class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
    def test3(self):
        return self.assertEqual(reverseList(['Daniel', 'Jhon', 'Elizabeth', 'Kinsley']), ['Kinsley','Elizabeth', 'Jhon','Daniel'])
    def test4(self):
        return self.assertEqual(reverseList([5,3,88,1]), [1,88,3,5])
    def test5(self):
        return self.assertEqual(reverseList(['one', 'two', 'three', 'four']), ['four','three', 'two','one'])
class isPalindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(isPalindrome("rabbit"), False)
    def test3(self):
       return self.assertEqual(isPalindrome("abcddcba"), True)
    def test4(self):
       return self.assertEqual(isPalindrome("cake"), False)
    def test5(self):
       return self.assertEqual(isPalindrome("Madam"), True)
class coinsTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def test2(self):
        return self.assertEqual(coins(92), [3,1,1,2])
    def test3(self):
        return self.assertEqual(coins(99), [3,2,0,4])
    def test4(self):
        return self.assertEqual(coins(50), [2,0,0,0])
    def test5(self):
        return self.assertEqual(coins(22), [0,2,0,2])

if __name__ == "__main__":
    unittest.main()