import logging

logging.basicConfig(level=logging.INFO, filename='outputPS13.txt', filemode='w', format='%(message)s')

# Function for matrix chain multiplication using memoisation
def matrixMultiplicationCost(dimension_array, i, j):
    logging.debug(f"START >> i={i}, j={j}")
    if(i == j):
        return 0                                                                        # if i == j then there is no cost of multiplication, as these are the same matrix
        
    if(COST_MATRIX[i][j] != -1):
        return COST_MATRIX[i][j]                                                        # return the previously calculated COST i.e. RE-USING.

    COST_MATRIX[i][j] = float('inf')                                                    # set the cost to be infinity, this will help in calculation of MIN cost
 
    for k in range(i,j):
        logging.debug(f"FOR >> START k={k}, i={i}, j={j}")
        COST_MATRIX[i][j] = min(
            COST_MATRIX[i][j], 
            matrixMultiplicationCost(dimension_array, i, k) + 
            matrixMultiplicationCost(dimension_array, k + 1, j) + 
            dimension_array[i - 1] * dimension_array[k] * dimension_array[j]
        )
    
    logging.debug(f"RETURN >> i={i}, j={j}, COST_MATRIX[{i}][{j}]={COST_MATRIX[i][j]}")
    return COST_MATRIX[i][j]


if __name__ == "__main__":
    inputfile='inputPS13.txt'
    try:
        file = open(inputfile, "r")
    except IOError as e:
        raise("****Please provide input file ****\n", e)

    input_file = file.readlines()                                                           # reading input from the file inputPS13.txt

    replace_chars = {" ": "", "{": "[", "}": "]"}
    input_file = list(map(lambda str: str.strip(), input_file))                             # cleaning the raw information read from the input file

    for b_find, b_replace in replace_chars.items():
        input_file = list(map(lambda str: str.replace(b_find, b_replace), input_file))

    for instruction in input_file:                                                          # converting instruction from input file to python variables
        exec(instruction)

    assert(len(a) == int(N))                                                                # raise exception if input array 'a' length is not equal to N. 

    COST_MATRIX = [[-1 for x in range(N - 1)] for x in range(N - 1)]                        # initializing the cost matrix with default cost as -1
    COST_MATRIX                                                                             # size of COST_MATRIX is (N-1) X (N-1)

    RESULT = matrixMultiplicationCost(a, 0, int(N) - 2)                                     # answer will be the last element of the first row i.e. 0th row and (N-2)th column
    logging.info(RESULT)
