import matplotlib.pyplot as plt
from get_pi import *

# constants for a polynomial function
a = 10**(-10)
b = 2.86


def draw_graph(time_data):
    plt.figure(figsize=(6, 4))

    data = list(map(list, zip(*time_data)))

    # draw a polynomial function graph [y=a*x^b]
    plt.plot(range(10000),[a*i**b for i in range(10000)], linewidth=0.8)

    plt.plot(data[0],data[1], '-r')

    plt.ylabel('time (s)')
    plt.xlabel('n digits')
    plt.title('Time complexity')
    plt.axis([0, 10100, 0, 30])
    plt.legend(('y=a*x^b','data'))
    plt.show()


def time_complexity():
    num_cores = 4
    pool = Pool(num_cores)
    data = []
    for i in range(1,101):
        start = time.time()
        list_pi = frac_to_dec_list(sum_of_fracs(pool.map(calc_pi_fraction, get_ranges(Max=i*72,step=72))))
        pi = ''.join(map(str, list_pi))

        data.append((check_pi_with_file(pi), time.time()-start))

    # print(data)
    draw_graph(data)

if __name__=="__main__":
    time_complexity()