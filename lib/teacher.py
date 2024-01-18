#!/usr/bin/env python

from user import User

import random

# modify the Teacher class so that it initializes with this list stored as an attribute, self.knowledge.

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self,first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    # Expand the teach() method in the Teacher class so that it returns a random element from self.knowledge.
    def teach(self):
        # random.choice(seq) Returns a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
        return random.choice(self.knowledge)
        # OR - return self.knowledge[random.randint(0, len(self.knowledge) - 1)]