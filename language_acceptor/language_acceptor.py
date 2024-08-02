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


class LanguageAcceptor(sm.StateMachine):
    start_state = 0

    def get_next_values(self, state, input_):
        self._validate_state(state)
        self._validate_input(input_)

        next_state = self._get_next_state(state, input_)
        output = next_state != 3

        self._validate_output(output)

        return next_state, output

    @classmethod
    def _get_next_state(self, state, input_):
        if state == 0 and input_ == "a":
            return 1
        if state == 1 and input_ == "b":
            return 2
        if state == 2 and input_ == "c":
            return 0
        return 3

    @classmethod
    def _validate_state(cls, state):
        if state not in [0, 1, 2, 3]:
            raise ValueError(state)

    @classmethod
    def _validate_input(cls, input_):
        if not isinstance(input_, (str, chr)):
            raise ValueError(input_)

    @classmethod
    def _validate_output(cls, output):
        if not isinstance(output, bool):
            raise ValueError(output)


if __name__ == "__main__":
    truth_table = [
        {"input": "a", "state": 0, "output": True},
        {"input": "b", "state": 1, "output": True},
        {"input": "c", "state": 2, "output": True},
        {"input": "a", "state": 0, "output": True},
        {"input": "a", "state": 1, "output": False},
        {"input": "a", "state": 3, "output": False},
        {"input": "b", "state": 3, "output": False},
        # Last test has to be performed twice to confirm deasired state
        {"input": "b", "state": 3, "output": False},
    ]

    la = LanguageAcceptor()

    la.start()

    for test in truth_table:
        print("Input:", test["input"])

        state = la.state

        if state != test["state"]:
            print("Expected state:", test["state"])
            print("Actual state:", state)
            print("Language Acceptor tests failed")
            exit(1)

        output = la.step(test["input"])

        if output != test["output"]:
            print("Expected output:", test["output"])
            print("Actual output:", output)
            print("Language Acceptor tests failed")
            exit(2)

    print("Language Acceptor tests passed")
