from ADT import Stack, Queue

def test_Stack():
    s= Stack((5,))
    d= Stack()


    assert d.isEmpty() == True

    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)

    assert d.pop() == [1,2,3]
    assert d.peek() == 3

    d.push(5)

    
    assert d.pop() == [1,2,3]
    assert d.pop() == [1,2]

    d.push(12)
    d.push(35)
    d.push(46)

    assert d.isEmpty() == False
    assert d.isFull() == False

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
