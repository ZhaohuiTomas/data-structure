"""
Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
"""
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push("dog")
    s.push(4)
    print(s.peek())


    """
    区分括号是否匹配的能力是识别很多编程语言结构的重要部分。具有挑战的是如何编写一个算法，
    能够从左到右读取一串符号，并决定符号是否平衡。为了解决这个问题，我们需要做一个重要的观察。
    从左到右处理符号时，最近开始符号必须与下一个关闭符号相匹配(见 Figure 4)。此外，处理的
    第一个开始符号必须等待直到其匹配最后一个符号。结束符号以相反的顺序匹配开始符号。他们从内到外匹配。
    这是一个可以用栈解决问题的线索。
    判断  （）是否对等
    """

    def parChecker(symbolString):
        s = Stack()
        balanced = True
        index = 0
        while index < len(symbolString) and balanced:
            symbol = symbolString[index]
            if symbol == "(":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    s.pop()
            index += 1
        if balanced and s.isEmpty():
            return True
        else:
            return False

    print(parChecker("()()((()))"))

    """
    现处理[(){}({})]更复杂的问题
    """

    def parcheck(symbolString):
        s = Stack()
        checkString = "({["
        index = 0
        balanced = True
        while index < len(symbolString) and balanced:
            symbol = symbolString[index]
            if symbol in checkString:
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    top = s.pop()
                    if not matches(top,symbol):
                        balanced = False
            index += 1
        if balanced and s.isEmpty():
            return True
        else:
            return False

    def matches(open,close):
        opens = "({["
        closes = ")}]"
        return opens.index(open)== closes.index(close)


    print(parcheck("{}()(){]"))



    """
    下面写一个十进制转换成二进制数据
    """

    def divideBy2(decNumber):

        s = Stack()
        while decNumber > 0:
            p = decNumber % 2
            decNumber = decNumber // 2
            s.push(p)
        twoString = ""
        while not s.isEmpty():
            twoString += str(s.pop())

        return twoString

    print(divideBy2(26))

    """
    现在改写上述程序，将程序扩展成统一的转换代码
    """

    def data_base_change(number,base):
        data_Stack = Stack()
        digits = "0123456789ABCDEF"
        change_data = ""
        while number > 0:
            reminder = number % base
            number //= base
            data_Stack.push(reminder)
        while not data_Stack.isEmpty():
            change_data += digits[data_Stack.pop()]

        return change_data


    """
    中缀转前缀
    """
    def infixToPostfix(infixexpr):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = Stack()
        tokenList = infixexpr.split()

        for token in tokenList:
