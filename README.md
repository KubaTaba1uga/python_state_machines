## Primitive state machine theory

We can specify a transducer (a process that takes as input a sequence of values which serve as inputs to the state machine, and returns as ouput the set of outputs of the machine for each input) as a state machine (SM) by specifying:  
• a set of states, `S`.  
• a set of inputs, `I`, also called the input vocabulary.  
• a set of outputs, `O`, also called the output vocabulary.  
• a next-state function, `n(it, st) → st+1`, that maps the input at time `t` and the `state` at time `t` to the `state` at time `t + 1`,  
• an output function, `o(it, st) → ot`, that maps the `input` at time `t` and the `state` at time `t` to the output at time `t`.  
• an initial state, `s0`, which is the `state` at time `0`.  

Here are a few state machines, to give you an idea of the kind of systems we are considering.

• A tick-tock machine that generates the sequence 1, 0, 1, 0, . . . is a finite-state machine that ignores its input.  
• The controller for a digital watch is a more complicated finite-state machine: it transduces a sequence of inputs (combination of button presses) into a sequence of outputs (combinations of segments illuminated in the display).  
• The controller for a bank of elevators in a large office building: it transduces the current set of buttons being pressed and sensors in the elevators (for position, open doors, etc.) into commands to the elevators to move up or down, and open or close their doors. 

