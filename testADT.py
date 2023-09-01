from ADT import Stack



def testStack():
    s= Stack((5,))
    d= Stack()

    print(s)
    print(d)
    print(d.isEmpty())
    print("")
    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)
    d.push(5)
    print(d)
    d.pop()
    print(d)
    d.push(12)
    d.push(23)
    d.push(34)
    s.push(45)
    d.push(13)
    d.push(24)
    s.push(35)
    d.push(46)
    d.push(35)
    d.push(46)
    print(d)
    print(s)
    print(d.isEmpty())
    print(d.isFull())


