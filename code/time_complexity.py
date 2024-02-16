import matplotlib.pyplot as plt
from get_pi import *


def draw_graph(time_data):
    plt.figure(figsize=(6, 4))

    data = list(map(list, zip(*time_data)))

    plt.plot(data[0],data[1], '-r', linewidth=0.5)

    plt.ylabel('time (s)')
    plt.xlabel('n digits')
    plt.title('Time complexity')
    plt.axis([0, 10100, 0, 30])
    plt.legend()
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

    print(data)
    draw_graph(data)

if __name__=="__main__":
    time_complexity()
