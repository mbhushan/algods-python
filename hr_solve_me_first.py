"""
https://www.hackerrank.com/challenges/solve-me-first

"""

class SolveMeFirst(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def getAddition(self):
        return self.first + self.second


def main():
    x = int(input())
    y = int(input())
    obj = SolveMeFirst(x, y)
    ans = obj.getAddition()
    print("addition: {}".format(ans))

if __name__ == "__main__":
    main()