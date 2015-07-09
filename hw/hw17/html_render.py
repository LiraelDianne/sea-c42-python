#!/usr/bin/env python

"""
Name: Crystal Stellwagen

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    def __init__(self, content="", tag=""):
        self.tag = tag
        self.children = [content] if content else []
        self.content = content

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, ind=""):
        indent = ind + "    "
        file_out.write(ind + "<%s> \n" % self.tag)
        for child in self.children:
            if type(child) == str:
                file_out.write(indent + child + "\n")
            else:
                child.render(file_out, indent)
        file_out.write("%s</%s>\n" % (ind, self.tag))


class Html(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="html")

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html> \n")
        Element.render(self, file_out, ind="")


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="body")


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="p")


class Head(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="head")

class OneLineTag(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="")

    def render(self, file_out, ind=""):
        file_out.write(ind + "<%s> %s </%s>\n" % (self.tag, self.content, self.tag))


class Title(OneLineTag):

    def __init__(self, content=""):
        Element.__init__(self, content=content, tag="title")
