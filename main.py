from transitions import Machine
import time

class MainFSM(object):

    # 定义状态
    states = ['init_listen', 'state_one_fsm', 'state_two_fsm', 'state_three_fsm']

    # 定义状态转移
    transitions = [
        {'trigger': '0.1', 'source': 'init_listen', 'dest': 'state_one_fsm' },
        {'trigger': '0.1', 'source': 'state_one_fsm', 'dest': 'init_listen' },
        {'trigger': '0.2', 'source': 'init_listen', 'dest': 'state_two_fsm' },
        {'trigger': '0.4', 'source': '*', 'dest': 'init_listen' },
        {'trigger': '0.3', 'source': 'init_listen', 'dest': 'state_three_fsm' }
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=MainFSM.states, transitions=MainFSM.transitions, initial='init_listen',
                               before_state_change='previous_state', after_state_change='current_state')

    def current_state(self):
        print('current state: ' + self.state + ' : 状态改变后输出')

    def previous_state(self):
        print('changing from state: ' + self.state + ' : 状态改变前输出')

    def on_enter_state_one_fsm(self):
        print('enter state one fsm' + ' : 进入状态1输出')

    def on_exit_state_one_fsm(self):
        print('exit state one fsm' + ' : 退出状态1输出')


if __name__ == '__main__':
    main_fsm = MainFSM()
    transition_sequence = ['0.1', '0.1', '0.2', '0.4', '0.4', '0.3', '0.4', '0.1']
    for tri in transition_sequence:
        main_fsm.trigger(tri)
        time.sleep(3)
