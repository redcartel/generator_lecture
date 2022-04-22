import pytest
import lecture

def test_target_sum():
    input1 = [1, 9, 2, 4, 7, 4]
    generator = lecture.pairs_that_sum_generator(input1, 11)
    
    assert next(generator) == (9, 2)
    assert next(generator) == (4,7)
    assert next(generator) == (7,4)
    
    with pytest.raises(StopIteration):
        next(generator)
    
def test_tuple_conversion():
    input2 = [11,10,1,20,-5,26]
    generator2 = lecture.pairs_that_sum_generator(input2, 21)
    
    assert tuple(generator2) == ((11,10), (1,20), (-5,26))
