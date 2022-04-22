# Problem 1

def pairs_that_sum_generator(numlist, target_sum):
    ''' Return a generator expression of the consecutive pairs of values 
    in a list that sum to a given target
    
    For instance the pairs from [1, 9, 2, 4, 7, 4] that sum to 11 are
    (9,2), (4,7), and (7,4) and the generator expression returned will 
    yield those tuples one at a time.
    '''
    
    # handle the degenerate case
    if (len(numlist) == 0):
        return (_ for _ in range(0))
    
    # first create a generator expresion that produces the indices of the first 
    # element of each pair, in the above example 1, 3, and 4
    indices = (i for i in range(len(numlist) - 1) 
                    if numlist[i] + numlist[i + 1] == target_sum)
    
    # TODO: now return a generator expression that produces the tuple 
    # (numlist[i], numlist[i+1]) for each index we found
    pass




# Example 2 pairwise sums

def pairwise_sum_generator(numlist):
    ''' Return an iteration of the pairwise sums of a list of values
    
    for instance, the pairwise sums of [1,9,2,4,1,4] are
    [10,11,6,5,5] and the generator returned will yield those values one
    at a time.
    '''

    if len(numlist) > 1:
        for i in range(len(numlist)-1):
            # TODO: the next value yielded should be numlist[i] + numlist[i+1]
            yield numlist[i] + numlist[i+1]

# Example 3

def transpose_generator(matrix):
    ''' Return a generator of the elements of a transpose of a matrix
    in row-wise order
    
    The transpose of a matrix is a transformation of a matrix where rows
    become columns and columns become rows. 
    
    Each element (i,j) is moved to position (j,i)
    
    The transpose of an AxB sized matrix will be a BxA sized matrix.
    
    For instance, the transpose of 
        
        [[1,2,3],
         [6,5,4]] 
         
         is
         
        [[1,6], 
         [2,5], 
         [3,4]] 
    
    and the generator returned would yield the values 1,6,2,5,3,4 one at a time 
    before terminating
    '''
    
    # find our height and width
    h = len(matrix)
    w = 0 if h == 0 else len(matrix[0])
    
    # HINT: You do not need to calculate the transpose of the matrix, you
    # only need to produce values in the correct order
    yield None