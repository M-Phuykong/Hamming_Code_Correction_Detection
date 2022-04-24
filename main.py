# CIS 1166: Phuykong Meng
# 11-04-2022
#
# Coding Theory #2
#
# Problems:
#  Given a binary code with minimum distance k, where k is a positive integer,
# write a program that will detect errors in codewords in as many as k − 1
# positions and correct errors in as many as ⌊(k − 1)/2⌋ positions.t
#
import sys

DEF_VALID_INPUT = ["0", "1"]

def isPowerOfTwo(n):
    return (n != 0) and ((n & (n-1)) == 0)

def calc_redundant_bit(m):

    for i in range(len(m)):
        if (2 ** i >= i + len(m) + 1):
            return i

def calc_val_of_parity_bit(m):
    
    modified_code_word = ["x"]
    modified_code_word.extend([bit for bit in m[::-1]])

    parity_bit = ""

    # calculate the value of each parity bit
    #
    for ind in range(len(modified_code_word)):
        
        if ind != 0 and isPowerOfTwo(int(ind)):
            
            check_bit = []

            for i in range(ind,len(modified_code_word),ind+1):
                
                if ind == 1:
                    check_bit.extend(modified_code_word[i])
                else:
                    check_bit.extend(modified_code_word[i:i+ind])
                    i = ind + 1

            check_bit = [int(i) for i in check_bit]
            parity_value = sum(check_bit) % 2
            parity_bit += str(parity_value)

    # reverse the parity bit after calculation
    #
    parity_bit = parity_bit[::-1]

    return parity_bit, modified_code_word[1:]

def detecting_correcting_error(parity_bit):

    # No error
    #
    if len(set(parity_bit)) == 1 and set(parity_bit).pop() == "0":
        return False
    else:
        return True

def correct_code(receive_code_word, error_position):
    
    # reversing the bit at the error location
    #
    if receive_code_word[error_position - 1] == "0":
        receive_code_word[error_position-1] = "1"
    else:
        receive_code_word[error_position - 1] = "0"

    return "".join(bit for bit in receive_code_word[::-1])
        

def main():

    print("Please input the received code word: (Seperate them by space and assuming that it has even parity)")
    receive_code_word = input()

    # error checking before continuing
    #
    for bit in receive_code_word:
        if bit not in DEF_VALID_INPUT:
            print("Invalid Input")
            sys.exit()

    # sanitize the input
    #
    receive_code_word = receive_code_word.replace(" ","")

    # calculate the parity check bit
    #
    parity_bit, receive_code_word = calc_val_of_parity_bit(receive_code_word)

    # see if the parity check bit has any error
    #
    if detecting_correcting_error(parity_bit):

        print("There is an error in the received transmission")

        error_position = int(parity_bit, 2)
        print(f"The error bit is in position {error_position} (starting from the right at index 1)")

        corrected_code = correct_code(receive_code_word, error_position)
        print(f"The corrected code is : {corrected_code}")

    else:
        print("There is no error in the recevied transmission")

##### Usage Example #####
#
# Input: 
# 
#   1110101 or 1 1 1 0 1 0 1 
# 
# Output:
#  
#   There is an error in the received transmission
#   The error bit is in position 6 (starting from the right at index 1)
#   The corrected code is : 1010101
#   
#


if __name__ == "__main__":
    main()