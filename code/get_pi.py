# February 12, 2024
# Jaeyoon Lee

from decimal import Decimal
from fractions import Fraction
import os
from math import log10
import time
from multiprocessing import Pool



def calc_pi(end) -> Decimal:
    # range: [start:end)
    pi = Decimal(0)
    k = Decimal(1+end*2)
    while k <= (end+1)*2:
        pi += (1/5**(2*k-1))*(16*(-1)**(k-1))/(2*k-1) - (1/239**(2*k-1))*(4*(-1)**(k-1))/(2*k-1)
        k += 1
    return pi


def calc_pi_fraction(end):
    start = time.time()
    pi = Fraction()
    k = 1+end*10
    while k <= (end+1)*10:
        pi += Fraction((16*(-1)**(k-1)),(2*k-1)*5**(2*k-1)) - Fraction((4*(-1)**(k-1)),(2*k-1)*239**(2*k-1))
        k += 1
    print(end,'CALCULATE_TIME:',time.time()-start)
    return pi

def frac_to_dec_list(frac:Fraction):
    # start = time.time()
    pi_ratio = frac.as_integer_ratio()
    pi = []

    rem = 10*(pi_ratio[0]%pi_ratio[1])
    for _ in range(int(log10(pi_ratio[0])/4)): # divide by 4 to reduce unnecessary calculations
        pi.append(rem//pi_ratio[1])
        rem = 10*(rem%pi_ratio[1])
    
    # print('CONVERT_TIME:',time.time()-start)

    return pi

def sum_of_fracs(fracs:list[Fraction]):
    # start = time.time()
    s = Fraction()
    for f in fracs:
        s = s + f
    # print('SUMATION_TIME:',time.time()-start)
    return s


def main():
    start = time.time()
    num_cores = 4
    pool = Pool(num_cores)

    list_pi = frac_to_dec_list(sum_of_fracs(pool.map(calc_pi_fraction, range(10))))

    pi = ''.join(map(str, list_pi))
    print('\nCalculated:', pi)

    current_path = os.path.dirname(__file__)
    file_name = os.path.join(current_path, 'pi.txt')
    txt_file = open(file_name, 'r')
    txt_pi = txt_file.readline()

    # Match digits
    count = 0
    while pi[count] == txt_pi[count]:
        count += 1
    
    txt_file.close()
    print('Matched:   ',txt_pi[:count])
    print('Actual pi: ',txt_pi[:count+5],'\n')
    print(count/len(pi), count,'/',len(pi))
    end_time = round(time.time()-start,2)
    print('TOTAL_TIME:',end_time)

    # Save digits
    # save_file_name = os.path.join(current_path, f'pi_calculated({count:,}).txt')
    # save_file = open(save_file_name, 'x')
    # save_file.write(txt_pi[:count])
    # save_file.close()
    # print('Save Complete')



    # DIGITS = 200
    # for p in pool.map(calc_pi, range(DIGITS)):
    #     list_pi.append(list(map(int,list("{:.1000f}".format(p)[2:]))))
    #     pi += p
    #     print("{:.500f}".format(p))

    # pi = [0 for i in range(1000)]

    # for i in range(999,-1,-1):
    #     for j in range(DIGITS-1,-1,-1):
    #         if list_pi[j][i] == 0:
    #             for k in range(1,7):
    #                 if list_pi[j][i-k]!=0:
    #                     break
    #         pi[i] += list_pi[j][i]
    #     if pi[i] > 9:
    #         pi[i-1] += pi[i]//10
    #         pi[i] %= 10
    # print(pi)

    # n = 2
    # sigma = 1
    # count = 1
    # while True:
    #     pi = math.sqrt(6 * (sigma))
    #     if n % 10000000 == 0:
    #         print(pi)
    #         count += 1
    #     if pi >= math.pi:
    #         print(n, pi)
    #         break
    #     sigma += 1 / (n**2)
    #     n += 1


if __name__ == "__main__":
    main()
