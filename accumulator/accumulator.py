def enable_internal_imports():
    import os
    import sys

    # Path to be added
    new_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the parent directory to sys.path
    if new_path not in sys.path:
        sys.path.insert(0, new_path)


enable_internal_imports()
# Now you can import internal modules
import sm


class Accumulator(sm.StateMachine):
    start_state = 0

    def get_next_values(self, state, input_):
        self._validate_state(state)
        self._validate_input(input_)

        output = state + input_

        self._validate_output(output)

        return output, output

    @classmethod
    def _validate_state(cls, state):
        if not isinstance(state, (int, float)):
            raise ValueError(state)

    @classmethod
    def _validate_input(cls, input_):
        if not isinstance(input_, (int, float)):
            raise ValueError(input_)

    @classmethod
    def _validate_output(cls, output):
        if not isinstance(output, (int, float)):
            raise ValueError(output)


def print_accumulator(accumulator):
    print("Accumulator step: %i" % accumulator.state)


if __name__ == "__main__":
    accumulator = Accumulator()

    accumulator.start()
    print_accumulator(accumulator)

    accumulator.step(200)
    print_accumulator(accumulator)

    accumulator.step(20)
    print_accumulator(accumulator)

    accumulator.step(2)
    print_accumulator(accumulator)
