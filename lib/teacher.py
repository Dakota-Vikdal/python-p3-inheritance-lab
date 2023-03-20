#!/usr/bin/env python

from user import User

import random
# import ipdb


class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast"
        ]

    def teach(self):
        index = random.randint(0, len(self.knowledge) -1)
        return self.knowledge[index]
        # self.knowledge = knowledge

    # def get_info(self):
        # return self._knowledge

    # def set_info(self, info):
        # if(info == knowledge):
            # self._info = info
        # else:
            # print("not knowledge")

books = Teacher("first_name", "last_name")
