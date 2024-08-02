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
        if not self.validate_state(state):
            raise ValueError(state)

        if not self.validate_input(input_):
            raise ValueError(input_)

        output = state + input_

        if not self.validate_output(output):
            raise ValueError(output)

        return output, output

    @classmethod
    def validate_state(cls, state) -> bool:
        return isinstance(state, (int, float))

    @classmethod
    def validate_input(cls, input_) -> bool:
        return isinstance(input_, (int, float))

    @classmethod
    def validate_output(cls, output) -> bool:
        return isinstance(output, (int, float))


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
