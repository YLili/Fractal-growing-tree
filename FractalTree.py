__author__ = 'Lili'
#coding: utf-8
import turtle
import Queue

##----------  Setup a queque to store the grow node ------------------------
dNodeQue = Queue.Queue()
NewNodeQue = Queue.Queue()
##----------  Initialize the parameter ------------------------
length = 50   #  setup the branch length
angle = 45    #  setup the branch angle
lineWidth = 10
turtle.speed(1)   #  setup the grow speed,the speed is 0-10,1 is the lowest, 1-10 the speed becomes faster.But 0 is the fastest.


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
        global NewNodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        d = Node('d', self.NodePosition,self.GrowAngle)
        dNodeQue.put(d)
        turtle.left(angle)
        turtle.forward(length)
        c = Node('c',turtle.pos(),turtle.heading() )
        NewNodeQue.put(c)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        b = Node('b',turtle.pos(),turtle.heading())
        NewNodeQue.put(b)
    ##----------  Setup the node behavior of type b ------------------------
    def b_branch(self):
        global length
        global NewNodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        d = Node('d',self.NodePosition,self.GrowAngle)
        dNodeQue.put(d)
        turtle.right(angle)
        turtle.forward(length)
        e = Node('e',turtle.pos(),turtle.heading())
        NewNodeQue.put(e)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        a = Node('a',turtle.pos(),turtle.heading())
        NewNodeQue.put(a)
    ##----------  Setup the node behavior of type c ------------------------
    def c_branch(self):
        global NewNodeQue
        b = Node('b',self.NodePosition,self.GrowAngle)
        NewNodeQue.put(b)
    ##----------  Setup the node behavior of type d ------------------------
    #def d_branch(self):

    ##----------  Setup the node behavior of type e ------------------------
    def e_branch(self):
        global length
        global NewNodeQue
        turtle.up()
        turtle.setpos(self.NodePosition)
        turtle.down()
        turtle.setheading(self.GrowAngle)
        d = Node('d',self.NodePosition,self.GrowAngle)
        dNodeQue.put(d)
        turtle.left(angle)
        turtle.forward(length)
        a = Node('a',turtle.pos(),turtle.heading())
        NewNodeQue.put(a)
        turtle.up()
        turtle.setpos(d.NodePosition)
        turtle.down()
        turtle.setheading(d.GrowAngle)
        turtle.forward(length)
        b = Node('b',turtle.pos(),turtle.heading())
        NewNodeQue.put(b)
    ##----------  Run the node behavior according to its type ------------------------
    def run(self):
        global NewNodeQue
        if self.NodeType == 'a':
            self.a_branch()
        elif self.NodeType == 'b':
            self.b_branch()
        elif self.NodeType == 'c':
            self.c_branch()
        #elif self.NodeType == 'd':
            #self.d_branch()
        elif self.NodeType == 'e':
            self.e_branch()

##----------  Setup the first node and start to build the tree ------------------------
turtle.color('brown')  # setup the line color
turtle.pensize(lineWidth*2)       # setup the line width
turtle.up()
turtle.setpos(0,-250)
turtle.down()
turtle.setheading(90)
turtle.forward(length*2)
turtle.color('green')  # setup the line color
turtle.pensize(lineWidth)
FirstNode = Node('a',turtle.pos(),turtle.heading())
NewNodeQue.put(FirstNode)
Index = 0
while( (not NewNodeQue.empty()) and (Index<100) ):
    GrowNode = NewNodeQue.get()
    GrowNode.run()
    Index += 1
turtle.done()
