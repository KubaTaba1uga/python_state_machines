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


class Delay(sm.StateMachine):
    start_state = 0

    def get_next_values(self, state, input_):
        new_state = input_
        output = state

        return new_state, output


if __name__ == "__main__":
    truth_table = [
        {"input": 3, "state": 0, "output": 0},
        {"input": 1, "state": 3, "output": 3},
        {"input": 2, "state": 1, "output": 1},
        {"input": 5, "state": 2, "output": 2},
        {"input": 9, "state": 5, "output": 5},
        {"input": 9, "state": 9, "output": 9},
    ]

    delay = Delay()

    delay.start()

    for test in truth_table:
        print("Input:", test["input"])

        state = delay.state

        if state != test["state"]:
            print("Expected state:", test["state"])
            print("Actual state:", state)
            print("Delay tests failed")
            exit(1)

        output = delay.step(test["input"])

        if output != test["output"]:
            print("Expected output:", test["output"])
            print("Actual output:", output)
            print("Delay tests failed")
            exit(2)

    print("Delay tests passed")
