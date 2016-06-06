__author__ = 'Lili'
#coding: utf-8
import turtle
import Queue
import time
import threading
##----------  Setup a queque to store the grow node ------------------------
NodeQue = Queue.Queue()
##----------  Initialize the parameter ------------------------
length = 50   #  setup the branch length
angle = 45    #  setup the branch angle
turtle.speed(1)   #  setup the grow speed,the speed is 0-10,1 is the lowest, 1-10 the speed becomes faster.But 0 is the fastest.
turtle.color('green')  # setup the line color
turtle.pensize(5)       # setup the line width

##----------  Setup the class of node ------------------------
class Node():
    NodeType = ' '
    NodePosition = (0,0)
    GrowAngle = 90
    ##----------  Initialize the node object ------------------------
    def __init__(self, type, position, angle):
        self.NodeType = type
        self.NodePosition = position
        self.GrowAngle = angle
    ##----------  Setup the node behavior of type a ------------------------
    def a_branch(self):
        global length
        global NodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        turtle.forward(length)
        d = Node('d', turtle.pos(),turtle.heading() )
        NodeQue.put(d)
        turtle.left(angle)
        turtle.forward(length)
        c = Node('c',turtle.pos(),turtle.heading() )
        NodeQue.put(c)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        b = Node('b',turtle.pos(),turtle.heading() )
        NodeQue.put(b)
    ##----------  Setup the node behavior of type b ------------------------
    def b_branch(self):
        global length
        global NodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        turtle.forward(length/3)
        d = Node('d',turtle.pos(),turtle.heading())
        NodeQue.put(d)
        turtle.right(angle)
        turtle.forward(length)
        e = Node('e',turtle.pos(),turtle.heading())
        NodeQue.put(e)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        a = Node('a',turtle.pos(),turtle.heading())
        NodeQue.put(a)
    ##----------  Setup the node behavior of type c ------------------------
    def c_branch(self):
        global length
        global NodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        turtle.forward(length/3)
        b = Node('b',turtle.pos(),turtle.heading())
        NodeQue.put(b)
    ##----------  Setup the node behavior of type d ------------------------
    def d_branch(self):
        global length
        global NodeQue
        d = Node('d',self.NodePosition,self.GrowAngle)
        NodeQue.put(d)
    ##----------  Setup the node behavior of type e ------------------------
    def e_branch(self):
        global length
        global NodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        turtle.forward(length/3)
        d = Node('d',turtle.pos(),turtle.heading())
        NodeQue.put(d)
        turtle.left(angle)
        turtle.forward(length)
        a = Node('a',turtle.pos(),turtle.heading())
        NodeQue.put(a)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        b = Node('b',turtle.pos(),turtle.heading())
        NodeQue.put(b)
    ##----------  Run the node behavior according to its type ------------------------
    def run(self):
        global NodeQue
        if self.NodeType == 'a':
            self.a_branch()
        elif self.NodeType == 'b':
            self.b_branch()
        elif self.NodeType == 'c':
            self.c_branch()
        elif self.NodeType == 'd':
            self.d_branch()
        elif self.NodeType == 'e':
            self.e_branch()

##----------  Setup the first node and start to build the tree ------------------------
FirstNode = Node('a',(0,-250),90)
NodeQue.put(FirstNode)
while( not NodeQue.empty()):
    GrowNode = NodeQue.get()
    GrowNode.run()

