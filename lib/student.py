#!/usr/bin/env python

from user import User

class Student(User):

    # Individual students should initialize with an attribute, self.knowledge, that points to an empty list.
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    # Expand the learn() method in the Student class so that in takes in a string and adds that string to the student's self.knowledge list.
    def learn(self, string):
        self.knowledge.append(string)