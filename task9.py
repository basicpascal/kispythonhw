from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class StateMachine:
    state = State.A

    def log(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 1],
            State.D: [State.E, 5],
            State.F: [State.F, 9],
        })

    def stay(self):
        return self.update({
            State.B: [State.D, 2],
            State.C: [State.C, 4],
            State.E: [State.F, 6],
            State.F: [State.D, 8],
        })

    def herd(self):
        return self.update({
            State.C: [State.D, 3],
            State.F: [State.G, 7],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()
