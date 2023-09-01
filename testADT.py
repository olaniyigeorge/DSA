from ADT import Stack, Queue



def test_Stack():
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

def test_Queue():
    s= Queue((5,))
    d= Queue()

    assert s.size() == 1
    assert d.isEmpty() == True

    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)

    assert d.pop() == 1

    d.push(5)

    assert d.size() == 4
    assert d.pop() == 2
    assert d.pop() == 3

    d.push(12)
    d.push(35)
    d.push(46)

    assert d.isEmpty() == False
    assert d.isFull() == False


test_Queue()