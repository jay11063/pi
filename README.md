# Calculate &pi; (pi)

This calculates as many digits of pi as possible.

## Description

### Machin-like formula

$$
\begin{aligned}
&\pi = 16\arctan\left(\frac{1}{5}\right) - 4\arctan\left(\frac{1}{239}\right)\\
&\pi = \sum_{k=1}^{\infty} \left(\frac{16(-1)^{k-1}}{2k-1}\left(\frac{1}{5}\right)^{2k-1} - \frac{4(-1)^{k-1}}{2k-1}\left(\frac{1}{239}\right)^{2k-1}\right)
\end{aligned}
$$

- I employed this formula within an algorithm I devised for computing the digits of pi.
- Utilizing this algorithm, I was able to calculate pi to 100,655 decimal places. 
I refrained from computing further digits due to the rapidly increasing calculation time; 
it took approximately 7 hours to compute 100,000 digits.
- Additionally, I have saved the calculated value of pi in a txt file, [pi_calculated(100,655).txt](/data/pi_calculated(100,655).txt).

## Getting Started

### Dependencies

* Python 3.10

### Run
```
python get_pi.py
```

## Analysis

### Time complexity graph of algorithm using Machin-like formula
![Alt text](/data/time_complexity_graph_with_polynomial(10,000_digits).png)
- I utilized the Python library matplotlib to calculate pi up to 10,000 decimal places, dividing it into 100 steps to collect data, and then visualized it with a graph.
- Alongside the data graph, I have included a graph of a polynomial function $(y = ax^b)$ with constants $a = 10^{-10}$ and $b = 2.86$ for comparison.


## Authors

Jaeyoon Lee


## Acknowledgments

* [[네이버 블로그] 슈퍼컴퓨터는 원주율(π)을 어떻게 50조 자리까지 계산할까?](https://post.naver.com/viewer/postView.nhn?volumeNo=28129380)
* [Python fractions module](https://docs.python.org/3/library/fractions.html#module-fractions)


## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

