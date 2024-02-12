# February 12, 2024
# Jaeyoon Lee

from decimal import Decimal
import os
import time
from multiprocessing import Pool
from using_fraction import *



# This is the first version of a function that uses a Machin-like formula to calculate pi.
def calc_pi(end) -> Decimal:
    pi = Decimal(0)
    k = Decimal(1+end*10)
    while k <= (end+1)*10:
        pi += (1/5**(2*k-1))*(16*(-1)**(k-1))/(2*k-1) - (1/239**(2*k-1))*(4*(-1)**(k-1))/(2*k-1)
        k += 1
    return pi


# Check the calculated value of pi with a file
def check_pi_with_file(pi_str:str) -> int:
    # Load million digits of pi from text file
    current_path = os.path.dirname(__file__)
    file_name = os.path.join(current_path, 'pi(1m).txt')
    txt_file = open(file_name, 'r')
    txt_pi = txt_file.readline()

    # Check from the first digit
    count = 0
    while pi_str[count] == txt_pi[count]:
        count += 1
    txt_file.close()
    return count

# This function provides a list of range tuples
def get_ranges(Max,step):
    return [(1+i*step,(1+i)*step) for i in range(Max//step)]


def main():
    start = time.time()
    num_cores = 4
    pool = Pool(num_cores)

    list_pi = frac_to_dec_list(sum_of_fracs(pool.map(calc_pi_fraction, get_ranges(Max=100,step=10))))

    pi = ''.join(map(str, list_pi))
    print('\nCalculated:', pi)

    count = check_pi_with_file(pi)

    print('Matched:   ',pi[:count])
    # print('Actual pi: ',txt_pi[:count+5],'\n')
    # print(count/len(pi), count,'/',len(pi))
    print('TOTAL_TIME:',time.time()-start)

    # Save digits
    # save_file_name = os.path.join(current_path, f'pi_calculated({count:,}).txt')
    # save_file = open(save_file_name, 'x')
    # save_file.write(txt_pi[:count])
    # save_file.close()
    # print('Save Complete')


if __name__ == "__main__":
    main()
