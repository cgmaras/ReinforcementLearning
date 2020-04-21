import numpy as np

class Reward:
    """
    Class for defining the reward function

    Parameters:
        options: Dictionary with all the necessary parameters
    """
    def __init__(self,
                options={'type': 'sum_exponential',
                     'number_limit_criteria': 1,
                     'number_maximum_criteria': 1,
                     'L1': (1.0,1.0),
                     'M1': (1.0,1.0)}
                ):

        self.options = options
    def evaluate(self,criteria_values):
        """
        Evaluates the desired reward function for a set of criteria values

        Parameters:
            criteria_values: the values of the function criteria
        """

        try:
            reward_function = getattr(self, self.options['type'])
        except:
            raise Exception('There is no reward function such as: {}'.format(self.options['type']))

        value = reward_function(criteria_values)
        return(value)

    def sum_exponential(self, criteria_values):
        """
        Sum of exponential terms for each criterion. Each criterion
        is weighted by a (limit or reference) value depending if it is
        a (limit or maximized) criterion, in order to represent relative
        values. Each exponential term has a multiplication coefficient. If
        any of the limit exponential terms becomes positive then the reward
        is multiplied by -1 to penalize for the exceeding any limit.

        R = bi*exp((Ci - Ci,l)/Ci,l) + bj*exp(Cj/Cj,m)

        Parameters:
            criteria_values: the values of the function criteria
        """
        limit_flag=0
        limit_values=np.zeros(self.options['number_limit_criteria'])
        for id in range(self.options['number_limit_criteria']):
            criterion_value = criteria_values[id]
            criterion_limit = self.options['L'+str(id+1)][0]
            coef = self.options['L'+str(id+1)] [1]
            if(criteria_values[id]>criterion_limit):
                limit_flag = 1
            limit_values[id] = np.exp((criterion_value - criterion_limit)/criterion_limit) *coef


        max_values=np.zeros(self.options['number_maximum_criteria'])
        for id in range(self.options['number_maximum_criteria']):
            criterion_value = criteria_values[id + self.options['number_limit_criteria']]
            criterion_ref = self.options['M'+str(id+1)][0]
            coef = self.options['M'+str(id+1)] [1]
            max_values[id] = np.exp(criterion_value/criterion_ref)*coef
        value = np.sum(limit_values) + np.sum(max_values)
        if(limit_flag):
            value *= -1
        return(value)

    def sum_linear(self, criteria_values):
        """
        Sum of linear terms for each criterion. Each criterion
        is weighted by a (limit or reference) value depending if it is
        a (limit or maximized) criterion, in order to represent relative
        values. Each linear term has a multiplication coefficient. If
        any of the limits is reached then the reward is multiplied by -1
        to penalize for the exceeding any limit.

        R = bi*(Ci - Ci,l)/Ci,l + bj*Cj/Cj,m

        Parameters:
            criteria_values: the values of the function criteria
        """
        
        limit_flag=0
        limit_values=np.zeros(self.options['number_limit_criteria'])
        for id in range(self.options['number_limit_criteria']):
            criterion_value = criteria_values[id]
            criterion_limit = self.options['L'+str(id+1)][0]
            coef = self.options['L'+str(id+1)] [1]
            if(criteria_values[id]>criterion_limit):
                limit_flag = 1
            limit_values[id] = coef*(1-(criterion_limit-criterion_value)/criterion_limit)


        max_values=np.zeros(self.options['number_maximum_criteria'])
        for id in range(self.options['number_maximum_criteria']):
            criterion_value = criteria_values[id + self.options['number_limit_criteria']]
            criterion_ref = self.options['M'+str(id+1)][0]
            coef = self.options['M'+str(id+1)] [1]
            max_values[id] = coef*criterion_value/criterion_ref
        value = np.sum(limit_values) + np.sum(max_values)
        if(limit_flag):
            value *= -1
        return(value)
        
