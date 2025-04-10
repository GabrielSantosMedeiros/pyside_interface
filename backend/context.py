from PySide6.QtCore import QObject
from typing import Optional


class Node:
    
    def __init__(self, id:str, component:QObject, parent:Optional['Node']=None):
        self.__id = id
        self.__component = component
        self.__parent = parent
        self.__children = []

    def getId(self):
        return self.__id
    
    def getComponent(self):
        return self.__component
    
    def getParent(self):
        return self.__parent
    
    def setParent(self, parent:'Node'):
        self.__parent = parent
    
    def getChildren(self):
        return self.__children
    
    def addChild(self, node:'Node'):
        if node not in self.__children:
            self.__children.append(node)
            node.setParent(parent=self)


class Tree:
    
    def __init__(self):
        self.root:Node = None
    
    def findById(self, current:Node, id:str):
        
        if current.getId() == id:
            return current
        
        for child in current.getChildren():
            result = self.findById(child, id)
        
            if result:
                return result


    def insert(self, node:Node):

        if self.root is None and node.getParent() == None:
            self.root = node

        elif self.root is not None and node.getParent() is not None:
            parent = self.findById(self.root, node.getParent().getId())
            parent.addChild(node)

    
    def getAll(self, current:Node, depth=0):
        
        print(
            ' '*depth + f'id :: {current.getId()}\n' +
            ' '*depth + f'component :: {current.getComponent()}'
        )
        
        for child in current.getChildren():
            self.getAll(child, depth=depth+3)

