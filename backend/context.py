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


