#!/usr/bin/env python

"""
Name: Crystal Stellwagen

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    def __init__(self, content="", tag="", **kwargs):
        self.tag = tag
        self.children = [content] if content else []
        self.content = content
        self.attributes = kwargs

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, ind=""):
        indent = ind + "    "
        file_out.write(ind + "<%s" % self.tag)
        for attrib in self.attributes:
            file_out.write(' %s="%s"' % (attrib, self.attributes[attrib]))
        file_out.write("> \n")
        for child in self.children:
            if type(child) == str:
                file_out.write(indent + child + "\n")
            else:
                child.render(file_out, indent)
        file_out.write("%s</%s>\n" % (ind, self.tag))


class Html(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="html", **kwargs)

    def render(self, file_out, ind="", **kwargs):
        file_out.write("<!DOCTYPE html> \n")
        Element.render(self, file_out, ind="")


class Body(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="body", **kwargs)


class P(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="p", **kwargs)


class Head(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="head", **kwargs)


class OneLineTag(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="", **kwargs)

    def render(self, file_out, ind="", **kwargs):
        file_out.write(ind + "<%s" % self.tag)
        for attrib in self.attributes:
            file_out.write(' %s="%s"' % (attrib, self.attributes[attrib]))
        file_out.write(">%s</%s>\n" % (self.content, self.tag))


class Title(OneLineTag):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="title", **kwargs)


class SelfClosingTag(Element):
    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="", **kwargs)

    def render(self, file_out, ind="", **kwargs):
        file_out.write(ind + "<%s" % self.tag)
        for attrib in self.attributes:
            file_out.write(' %s="%s"' % (attrib, self.attributes[attrib]))
        file_out.write(" />\n")


class Br(SelfClosingTag):
    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="br", **kwargs)


class Hr(SelfClosingTag):
    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, tag="hr", **kwargs)


class A(OneLineTag):
    def __init__(self, link, content):
        self.tag = "a"
        self.content = content
        self.attributes = {'href': link}
