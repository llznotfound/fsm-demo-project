from transitions import Machine


class StateTwo(object):
    # 定义状态
    states = ['init_listen', 'state_one_fsm', 'state_two_fsm', 'state_three_fsm']

    # 定义状态转移
    transitions = [
        {'trigger': '0.1', 'source': 'init_listen', 'dest': 'state_one_fsm'},
        {'trigger': '0.1', 'source': 'state_one_fsm', 'dest': 'init_listen'},
        {'trigger': '0.2', 'source': 'init_listen', 'dest': 'state_two_fsm'},
        {'trigger': '0.4', 'source': '*', 'dest': 'init_listen'},
        {'trigger': '0.3', 'source': 'init_listen', 'dest': 'state_three_fsm'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=StateTwo.states, transitions=StateTwo.transitions,
                               initial='init_listen',
                               before_state_change='previous_state', after_state_change='current_state')

    def current_state(self):
        print('current state: ' + self.state)

    def previous_state(self):
        print('changing from state: ' + self.state + ' to ')
