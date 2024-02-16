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
I refrained from computing further digits due to the exponential increase in calculation time; 
it took approximately 7 hours to compute 100,000 digits.
- Additionally, I have saved the calculated value of pi in a txt file, [pi_calculated(100,655).txt](/data/pi_calculated(100,655).txt).

### Time complexity graph of algorithm using Machin-like formula
![Alt text](/data/time_complexity_graph(10,000_digits).png)
- I utilized the Python library matplotlib to calculate pi up to 10,000 decimal places, dividing it into 100 steps to collect data, and then visualized it with a graph.

## Getting Started

### Dependencies

* Python 3.10
* Matplotlib 3.6.0

### Run
```
python get_pi.py
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Jaeyoon Lee

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

