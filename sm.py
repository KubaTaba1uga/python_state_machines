from __future__ import annotations

from abc import ABC, abstractmethod


class StateMachine(ABC):
    """
    The SM class contains generally useful methods that apply to all state machines. A state machine is an instance of any subclass of SM, that has defined the attribute startState and the method getNextValues.
    """

    start_state = None

    def __init__(self):
        pass

    def start(self):
        self.state = self.start_state

    def step(self, input_):
        """Once sm has started, we can ask it to take a step, using the step method, which, given an input, computes the output and updates the internal state of the machine, and returns the output value."""
        (s, o) = self.get_next_values(self.state, input_)
        self.state = s
        return o

    def transduce(self, inputs):
        """To run a machine on a whole sequence of input values, we can use the transduce method, which will return the sequence of output values that results from feeding the elements of the list inputs into the machine in order."""
        self.start()
        return [self.step(inp) for inp in inputs]

    @abstractmethod
    def get_next_values(self, state, inp):
        """It is crucial that get_next_value be a pure function; that is, that it not change the state of the object (by assigning to any attributes of self). It must simply compute the necessary values and return them. We do not promise anything about how many times this method will be called and in what circumstances."""
        pass
