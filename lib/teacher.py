#!/usr/bin/env python

from user import User

import random


class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        
        if knowledge and isinstance(knowledge, list) and len(knowledge)> 0:
            self.knowledge = knowledge
        else:
            self.knowledge = ["default knowledge"]
        
    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, knowledge):
        if isinstance(knowledge, list) and len(knowledge)> 0:
            self._knowledge = knowledge
            
        else:
            raise ValueError ("knowledge must be a non-empty list")

    def teach(self):
        return random.choice(self.knowledge)