# 1/n- Cycle  (6 kyu)
[1/n- Cycle codewars link](https://www.codewars.com/kata/5a057ec846d843c81a0000ad)

### Details
Let be n an integer prime with 10 e.g. 7.

1/7 = 0.142857 142857 142857 ....

We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:

1/11 = 0.09 09 09 .... Cycle length is 2.
Task

Given an integer n (n > 1) the function cycle(n) returns the length of the cycle if there is one otherwise (n and 10 not coprimes) return -1.
Examples:
```python
cycle(5) = -1
cycle(13) = 6 -> 0.076923 076923 0769
cycle(21) = 6 -> 0.047619 047619 0476
cycle(27) = 3 -> 0.037 037 037 037 0370
cycle(33) = 2 -> 0.03 03 03 03 03 03 03 03
cycle(37) = 3 -> 0.027 027 027 027 027 0
cycle(94) = -1 
```