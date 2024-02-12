# February 12, 2024
# Jaeyoon Lee
# This program provide a function that calculates pi using fraction form of Machin-like formula

from fractions import Fraction
from math import log10
import time

# This function calculates a sum of fractions in given range
def calc_pi_fraction(Range:tuple[int,int]) -> Fraction:
    # ex) [1:100],[101:200],...
    # start = time.time()
    pi = Fraction()
    k = Range[0]
    while k <= Range[1]:
        pi += Fraction((16*(-1)**(k-1)),(2*k-1)*5**(2*k-1)) - Fraction((4*(-1)**(k-1)),(2*k-1)*239**(2*k-1))
        k += 1
    # print(end,'CALCULATE_TIME:',time.time()-start)
    return pi # datatype: Fraction(nominator, denominator)

# This fuction converts fraction to decimal format
def frac_to_dec_list(frac:Fraction) -> list[int]:
    # start = time.time()
    pi_ratio = frac.as_integer_ratio() # Fraction => tuple(nominator, denominator)
    pi = []
    rem = 10*(pi_ratio[0]%pi_ratio[1]) # remainder
    for _ in range(int(log10(pi_ratio[0])/4)): # divide by 4 to reduce unnecessary calculations
        pi.append(rem//pi_ratio[1])
        rem = 10*(rem%pi_ratio[1])
    # print('CONVERT_TIME:',time.time()-start)
    return pi

# This function calculates a sum of all given fractions
def sum_of_fracs(fracs:list[Fraction]) -> Fraction:
    # start = time.time()
    s = Fraction()
    for f in fracs:
        s = s + f
    # print('SUMATION_TIME:',time.time()-start)
    return s

def main():
    start = time.time()
    pi_list = frac_to_dec_list(calc_pi_fraction((1,100)))
    print(time.time()-start)
    # print(''.join(map(str, pi_list)))

# print(pi)

if __name__=="__main__":
    main()
