import math
import random
from node import Node

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

class Hiddenlayer:

	def __init__(self, lBefore, nodes):
		self.nodes = nodes
		self.nodeObjs = []
		self.bConns = []
		self.lBefore = lBefore

		for o in self.lBefore.nodeObjs:
			self.bConns.append(o)

		for i in range(nodes):
			self.nodeObjs.append(Node(0,self.bConns))

	def InitalizeNodes(self):
		for node in self.nodeObjs:
			node.biase = random.random()*10
			for k in range(nodes*lBefore.nodes):
				node.weights.append(random.random())

	def ChangeNodes(self):
		for j in range(self.nodes):
			self.nodeObjs[j].biase += random.uniform(1,-1)
			for k in range(len(self.nodeObjs[j].weights)):
				self.nodeObjs[j].weights[k] += random.uniform(1,-1)

	def ComputeNodes(self):
		for node in self.nodeObjs:
			nV = 0
			c = 0
			for w in node.weights:
				nV += w*self.lBefore.nodeObjs[c]
				c+=1
			nV-=node.biase
			node.value = sigmoid(nV)

	def listWeightsAndBiases(self):
		l = []
		for node in self.nodeObjs:
			l.append(node.weights)
			l.append(node.biase)

		return l


class Inputlayer:

	def __init__(self, nodes):
		self.nodes = nodes
		self.nodeObjs = []

		for i in range(nodes):
			self.nodeObjs.append(Node(0,[]))

	def giveVals(self, vals):
		c = 0
		for n in self.nodeObjs:
			n.value = vals[c]
			c+=1

class Outputlayer:

	def __init__(self, lBefore, nodes):
		self.nodes = nodes
		self.nodeObjs = []
		self.bConns = []
		self.lBefore = lBefore

		for o in self.lBefore.nodeObjs:
			self.bConns.append(o)

		for i in range(nodes):
			self.nodeObjs.append(Node(0,self.bConns))

	def InitalizeNodes(self):
		for node in self.nodeObjs:
			node.biase = random.random()*10
			for k in range(nodes*lBefore.nodes):
				node.weights.append(random.random())

	def ChangeNodes(self):
		for j in range(self.nodes):
			self.nodeObjs[j].biase += random.uniform(1,-1)
			for k in range(len(self.nodeObjs[j].weights)):
				self.nodeObjs[j].weights[k] += random.uniform(1,-1)

	def ComputeNodes(self):
		for node in self.nodeObjs:
			nV = 0
			c = 0
			for w in node.weights:
				nV += w*self.lBefore.nodeObjs[c]
				c+=1
			nV-=node.biase
			node.value = sigmoid(nV)

	def listWeightsAndBiases(self):
		l = []
		for node in self.nodeObjs:
			l.append(node.weights)
			l.append(node.biase)

		return l