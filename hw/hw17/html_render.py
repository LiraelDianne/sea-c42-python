#!/usr/bin/env python

"""
Name: Crystal Stelwagen

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    def __init__(self, name="", content=""):
        self.name = name
        self.content = content

    def append(self, new_text):
        self.content += new_text

    def render(self, file):
        file.write(self.content)
