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


class UpAndDownCounter(sm.StateMachine):
    start_state = 0

    def get_next_values(self, state, input_):
        self._validate_state(state)
        self._validate_input(input_)

        if input_ == "u":
            new_state = state + 1
        if input_ == "d":
            new_state = state - 1

        self._validate_output(new_state)

        return new_state, new_state

    @classmethod
    def _validate_state(cls, state):
        if not isinstance(state, int):
            raise ValueError(state)

    @classmethod
    def _validate_input(cls, input_):
        if input_ not in ["u", "d"]:
            raise ValueError(input_)

    @classmethod
    def _validate_output(cls, output):
        if not isinstance(output, int):
            raise ValueError(output)


if __name__ == "__main__":
    truth_table = [
        {"input": "u", "state": 0, "output": 1},
        {"input": "u", "state": 1, "output": 2},
        {"input": "u", "state": 2, "output": 3},
        {"input": "d", "state": 3, "output": 2},
        {"input": "d", "state": 2, "output": 1},
        {"input": "u", "state": 1, "output": 2},
        {"input": "u", "state": 2, "output": 3},
    ]

    counter = UpAndDownCounter()

    counter.start()

    for test in truth_table:
        print("Input:", test["input"])

        state = counter.state

        if state != test["state"]:
            print("Expected state:", test["state"])
            print("Actual state:", state)
            print("Up and Down Counter tests failed")
            exit(1)

        output = counter.step(test["input"])

        if output != test["output"]:
            print("Expected output:", test["output"])
            print("Actual output:", output)
            print("Up and Down Counter tests failed")
            exit(2)

    print("Up and Down Counter tests passed")
