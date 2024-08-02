## Delay

An even simpler machine just takes the input and passes it through to the output, but with one step of delay, so the kth element of the input sequence will be the k + 1st element of the output sequence. Here is the formal machine definition: 
```
S = anything
I = anything
O = anything

n(s,i) = i

o(s,i) = i

s0 = 0
```

Given an input sequence:
```
i0,i1,i2, ...
```
this machine will produce an output sequence:
```
0,i0,i1,i2, ...
```
The initial 0 comes because it has to be able to produce an output before it has even seen an input, and that output is produced based on the initial state, which is 0. 
