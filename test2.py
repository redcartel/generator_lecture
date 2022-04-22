import pytest
import lecture

def test_pairwise():
    input = [1,9,2,4,1,4]
    generator = lecture.pairwise_sum_generator(input)
    
    assert next(generator) == 10
    assert next(generator) == 11
    assert next(generator) == 6
    assert next(generator) == 5
    assert next(generator) == 5
    
    with pytest.raises(StopIteration):
        next(generator)
        
    input2 = [1,-2,3,-4,5,-6,7]
    generator2 = lecture.pairwise_sum_generator(input2)
    
    assert tuple(generator2) == (-1,1,-1,1,-1,1)