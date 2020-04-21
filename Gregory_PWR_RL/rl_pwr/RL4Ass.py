import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from reward import Reward as rwd
import copy

class RL_4ass:
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
        """
        Initialization of the qtable to random initial values
        """
        qt={}
        for i in range(self.fsize):
            for ii in range(self.fsize):
                for iii in range(self.fsize):
                        for iiii in range(self.fsize):
                            qt[(i,ii,iii,iiii)] = np.reshape([np.random.uniform(-1,0 ) for j in range(self.fsize*4)], (self.fsize,4))
                            qt[(i,ii,iii,iiii)][i,0] = -np.inf
                            qt[(i,ii,iii,iiii)][ii,1] = -np.inf
                            qt[(i,ii,iii,iiii)][iii,2] = -np.inf
                            qt[(i,ii,iii,iiii)][iiii,3] = -np.inf
        return(qt)


    def state_converter(self, state):
        """
        Converts the state values to the qtable indices
            - state is an array of fuel types configuration
            - the state is returned as a tuple
        """
        return(tuple(state -1))

    def get_state(self):
        """
        Returns the state of the class
            - the state is returned as a tuple
        """
        state=np.array(self.state)
        return(tuple(state+1))

    def impose_state(self,state):
        """
        Imposes a desired state and updates the current reward
            - state is an array of fuel types configuration
        """
        self.state = self.state_converter(state)
        self.current_reward= self.rwd.evaluate(np.array(self.get_state()))

    def action(self,state):
        """
        Finds the indices for the maximum of the qtable indicating the action
            - state is a tuple of indices
            - the action is return as a list of two indices: act[0] is the
            fuel type to be used and act[1] the location
        """
        Qsel=self.qtable[state]
        act = list(np.unravel_index(np.argmax(Qsel),Qsel.shape))
        return(act)


    def get_qvalue(self,s,a):
        """
        Returns the qvalue for a specific state and action
            - s is the state as a tuple
            - a is the action as a list of size 2
        """
        return(self.qtable[s][a[0],a[1]])

    def load_qtable(self,qt):
        """
        Loads a saved qtable
            - s is the state as a tuple
            - a is the action as a list of size 2
        """
        self.qtable = copy.deepcopy(qt)

    def update_state(self,lr,dc,RAND=False):
        """
        It performs the RL policy by updating the state based on an action
            - lr is the LEARNING_RATE
            - dc is the DISCOUNT
            - RAND True if a random update is to be performed

        First, the action is selected by taking the maximum of the qtable
        for the current state.

        Second, the state is updated and the reward is calculated

        Third, the current qvalue before the action and the maximum future
        qvalue after the action are computed and combined with the reward to
        calculate the new qvalue for the initial state and action.
        """

        current_state = copy.deepcopy(self.state)
        if RAND:
            current_q = -np.inf
            while current_q==-np.inf:
                current_act = [np.random.randint(0,self.fsize),np.random.randint(0,4)]
                current_q = self.get_qvalue(current_state,current_act)

        else:
            current_act = self.action(current_state)
        current_q = self.get_qvalue(current_state,current_act)


        new_state = list(self.state)
        new_state[current_act[1]] = current_act[0]
        self.state = tuple(new_state)

        self.current_reward= self.rwd.evaluate(np.array(self.get_state()))
        new_act = self.action(self.state)
        max_future_q = self.get_qvalue(self.state,new_act)
        qvalue_update = (1 - lr) * current_q + lr * (self.current_reward + dc * max_future_q)
        self.update_qtable(current_state,current_act,qvalue_update)


    def get_qstate(self):
        """
        Returns the q values for the current state
        """
        return(self.qtable[self.state])

    def update_qtable(self,state,action,value):
        """
        Updates the qvalue for a specific state and action
            - state the tuple of state indices
            - action the list of the selected action
            - value the new value of the qvalue
        """
        self.qtable[state][action[0],action[1]]=value
