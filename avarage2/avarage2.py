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


class Avarage2(sm.StateMachine):
    start_state = 0

    def get_next_values(self, state, input_):
        self._validate_state(state)
        self._validate_input(input_)

        next_state = input_
        output = (state + input_) / 2

        self._validate_output(output)

        return next_state, output

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


if __name__ == "__main__":
    truth_table = [
        {"input": 100, "state": 0, "output": 50},
        {"input": -3, "state": 100, "output": 48.5},
        {"input": 4, "state": -3, "output": 0.5},
        {"input": -123, "state": 4, "output": -59.5},
        {"input": 10, "state": -123, "output": -56.5},
        {"input": 10, "state": 10, "output": 10},
    ]

    avg2 = Avarage2()

    avg2.start()

    for test in truth_table:
        print("Input:", test["input"])

        state = avg2.state

        if state != test["state"]:
            print("Expected state:", test["state"])
            print("Actual state:", state)
            print("Avarage 2 tests failed")
            exit(1)

        output = avg2.step(test["input"])

        if output != test["output"]:
            print("Expected output:", test["output"])
            print("Actual output:", output)
            print("Avarage 2 tests failed")
            exit(2)

    print("Avarage 2 tests passed")
