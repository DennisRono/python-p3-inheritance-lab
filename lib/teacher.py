#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    
    def __init__(self, first_name, last_name):
        # Initialize the base User class with first and last names
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute with the provided list
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        # Return a random item from the knowledge list
        return random.choice(self.knowledge)