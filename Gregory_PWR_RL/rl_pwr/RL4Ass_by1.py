import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from reward import Reward as rwd
import copy

class RL_4ass_by1:
    """
    Object for reinforcement learning
    """
    def __init__(self,options):
        self.ftypes = options["fuel_types"]
        self.state = self.state_converter(options["initial_state"])
        self.fsize = len(self.ftypes)
        self.rwd = rwd(options["reward_options"])
        self.current_reward=self.rwd.evaluate(np.array(self.get_state()))
        self.qtable = self.init_qtable()
        self.move_sel =0

    def init_qtable(self):
        qt={}
        for i in range(self.fsize):
            for ii in range(self.fsize):
                for iii in range(self.fsize):
                        qt[(i,ii,iii)] = np.random.uniform(-1,0, (1,self.fsize))

        return(qt)


    def state_converter(self, state):
        return(tuple(state -1))

    def get_state(self):
        state=np.array(self.state)
        return(tuple(state+1))

    def impose_state(self,state):
        self.state = self.state_converter(state)
        self.current_reward= self.rwd.evaluate(np.array(self.get_state()))

    def action(self,state):
        Qsel=self.qtable[state]
        act = np.argmax(Qsel)
        return(act)


    def get_qvalue(self,s,a):
        return(self.qtable[s][0][a])

    def update_state(self,lr,dc):
        current_state = self.state
        self.move_sel += 1
        if(self.move_sel==4):
            self.move_sel==0
        effective_cstate = tuple(np.delete(current_state,self.move_sel))
        current_act = self.action(effective_cstate)
        current_q = self.get_qvalue(effective_cstate,current_act)

        new_state = list(self.state)
        new_state[self.move_sel] = current_act
        self.state = tuple(new_state)

        self.current_reward= self.rwd.evaluate(np.array(self.get_state()))
        self.move_sel += 1
        if self.move_sel==4 :
            self.move_sel=0
        effective_nstate = tuple(np.delete(self.state,self.move_sel))
        new_act = self.action(effective_nstate)
        max_future_q = self.get_qvalue(effective_nstate,new_act)
        qvalue_update = (1 - lr) * current_q + lr * (self.current_reward + dc * max_future_q)
        self.update_qtable(effective_cstate,current_act,qvalue_update)

    def get_qstate(self,state):
        return(self.qtable[state])

    def update_qtable(self,state,action,value):
        self.qtable[state][0][action]=value
