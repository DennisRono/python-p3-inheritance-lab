#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        # Initialize the base User class with first and last names
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute as an empty list
        self.knowledge = []

    def learn(self, info):
        # Add the information to the knowledge list
        self.knowledge.append(info)