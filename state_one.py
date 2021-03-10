from transitions import Machine


class StateOne(object):

    # 定义状态
    states = ['init_listen', 'data_check', 'pid_driven']

    # 定义状态转移
    transitions = [
        {'trigger': '0.1', 'source': 'init_listen', 'dest': 'data_check'},
        {'trigger': '0.1', 'source': 'pid_driven', 'dest': 'data_check'},
        {'trigger': '0.1.0', 'source': 'pid_driven', 'dest': 'init_listen'},
        {'trigger': '1.1and1.2', 'source': 'data_check', 'dest': 'pid_driven'}
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=StateOne.states, transitions=StateOne.transitions,
                               initial='init_listen',
                               before_state_change='previous_state', after_state_change='current_state')

    def current_state(self):
        print('current state: ' + self.state)

    def previous_state(self):
        print('changing from state: ' + self.state + ' to ')
