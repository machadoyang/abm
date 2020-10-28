# -*- coding: utf-8 -*-
"""
@author: machadoyang
"""


from mesa import Agent, Model
from mesa.time import BaseScheduler, StagedActivation

import matplotlib.pyplot as plt
import numpy as np

class FarmerAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.poverr = 0.3  # Probability of override
        self.pcrop = [0.55, 0.4, 0.05]  # Proabability of crop choice
        
    def cropsselection(self):
        list_of_crops=['Rice', 'Maize', 'Soya']
        self.crop_choice = np.random.choice(list_of_crops, 1, p = self.pcrop)
        
    def demandwater(self):
        pass

    def step(self):
        self.cropsselection()
        print ("Hi, I am farmer and chose to plant " + str(self.crop_choice[0]) +".")
        
class ManagerAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.testvar = 1
        
    def step(self):
        print ("Hi, I am the manager" +".")

class IrrigationModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = StagedActivation(self)
        # Create agents
        for i in range(self.num_agents):
            f = FarmerAgent(i, self)
            self.schedule.add(f)
        m = ManagerAgent(i, self)
        self.schedule.add(m)
            
    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
        
empty_model = IrrigationModel(11)
empty_model.step()