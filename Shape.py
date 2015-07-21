#import abc

class Shape(object):
    #__metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

#
#    @abc.abstractmethod
#    def getArea(self):
#        """Method to find and return area of shape."""
#        return
