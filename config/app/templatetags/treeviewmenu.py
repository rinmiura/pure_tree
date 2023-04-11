from django.template import Library

from app.models import Menu


register = Library()


@register.simple_tag
def draw_menu(current):
    pass


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

class Tree:
    head = None
    def add(self, name, parent):
        node = Node(name, parent)
        if not self.head:
            self.head = node
        else:
            nex = self.head
            while nex.name != parent:
                _children = [child.name for child in nex.children]
                try:
                    index = _children.index(parent)
                except:
                    nex = 



for item in Menu.objects.all():

