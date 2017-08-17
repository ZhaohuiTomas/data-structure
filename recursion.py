"""
定义了一个递归函数
"""

def list_sum(num_list):
    if len(num_list) == 1: #定义了递归停止条件
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,2,3,4,5,6,7,8,9,10]))


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *fac(n-1)

print(sum([fac(i) for i in range(1,10)]))

def toStr(n,base):
    converString = "0123456789ABCDE"
    if n < base:
        return converString[n]
    else:
        return toStr(n//base,base) + converString[n % base]
print(toStr(256,2))
"""
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > -105:
        myTurtle.forward(lineLen)
        myTurtle.right(30)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

"""
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()





