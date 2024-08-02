## Language Acceptor

Here is a finite-state machine whose output is true if the input string adheres to a simple pattern, and false otherwise. In this case, the pattern has to be:
```
a, b, c, a, b, c, a, b, c, ...
```

It uses the states 0, 1, and 2 to stand for the situations in which it is expecting an a, b, and c, respectively; and it uses state 3 for the situation in which it has seen an input that was not the one that was expected. Once the machine goes to state 3 (sometimes called a rejecting state), it never exits that state.
```
S = {0, 1, 2, 3}
I = {a, b, c}
O = {true, false}

         /- 1 if s=0, i=a
        / - 2 if s=1, i=b
n(s,i) =  - 0 if s=2, i=c
        \ - 3 otherwise

        /- false if n(s, i) = 3
o(s,i) = - true otherwise

s0 = 0
```
