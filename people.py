__author__ = 'Alfred'

class people(object):
    def __init__(self):
        print "Init class"

    def getName(self, name):
        print "getName in class people: ", name
        return name


if __name__ == '__main__':
    name = people()
    name.getName('ALfred')