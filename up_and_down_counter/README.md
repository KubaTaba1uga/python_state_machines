## Up and down counter

This machine can count up and down; its state space is the countably infinite set of integers. It starts in state 0. Now, if it gets input u, it goes to state 1; if it gets u again, it goes to state 2. If it gets d, it goes back down to 1, and so on. For this machine, the output is always the same as the next state.

```
S = integers
I = {u, d}
O = integers

        / - s + 1 if i=u
n(s,i) =  - s - 1 if i=d

o(s,i) = n(s, i)

s0 = 0
```
