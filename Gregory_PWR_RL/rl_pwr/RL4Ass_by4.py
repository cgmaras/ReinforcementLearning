import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from reward import Reward as rwd
import copy

class RL_4assBy4:
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

    def init_qtable(self):
        qt={}
        for i in range(self.fsize):
            for ii in range(self.fsize):
                for iii in range(self.fsize):
                        for iiii in range(self.fsize):
                            qt[(i,ii,iii,iiii)] = np.reshape([np.random.uniform(-1,0 ) for j in range(self.fsize*4)], (self.fsize,4))
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
        flat_ind=Qsel.argsort(axis=None)[-4:]
        act=np.transpose(np.array((np.unravel_index(flat_ind,Qsel.shape))))
        return(act)

    def get_qvalue(self,s,a):
        q=[]
        for i in range(4):
            ai = a[i]
            q.append(self.qtable[s][ai[0],ai[1]])
        return(np.array(q))

    def update_state(self,lr,dc):
        current_state = self.state
        current_act = self.action(current_state)
        current_q = self.get_qvalue(current_state,current_act)

        new_state = list(self.state)
        for i in range(4):
            new_state[current_act[i][1]] = current_act[i][0]
        self.state = tuple(new_state)

        self.current_reward= self.rwd.evaluate(np.array(self.get_state()))
        new_act = self.action(self.state)
        max_future_q = self.get_qvalue(self.state,new_act)
        qvalue_update = (1 - lr) * current_q + lr * (self.current_reward + dc * max_future_q)
        self.update_qtable(current_state,current_act,qvalue_update)

    def get_qstate(self):
        return(self.qtable[self.state])

    def update_qtable(self,state,action,value):
        for i in range(4):
            self.qtable[state][action[i][0],action[i][1]]=value[i]
