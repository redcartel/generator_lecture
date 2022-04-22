import pytest
import lecture

def test_transpose():
    input1 = [[1,2,3], [6,5,4]]
    generator = lecture.transpose_generator(input1)
    
    # a generator produces results one at a time, "pausing" after each yield statement
    # the results of a generator can be retrieved one at a time with the next function
    assert next(generator) == 1
    assert next(generator) == 6
    assert next(generator) == 2
    assert next(generator) == 5
    assert next(generator) == 3
    assert next(generator) == 4
    
    # when a generator ends its iteration, it raises StopIteration
    with pytest.raises(StopIteration):
        next(generator)
    
    # you can 'unspool' a finite generator result with a conversion to
    # list or tuple
    input2 = [[1,2,3], [4,5,6], [7,8,9]]
    generator2 = lecture.transpose_generator(input2)
    assert tuple(generator2) == (1,4,7,2,5,8,3,6,9)