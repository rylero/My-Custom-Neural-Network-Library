#
#Sample Test for netWorksPyLib
#Find if string is jaric, or gorec
#jaric = 0010111
#goric = 1110000
#

import random
import time

def train(l):
	while True:
		ranEXP = [[0,0,1,0,1,1,1],[1,1,1,0,0,0,0],[0,0,1,1,1,0,1], [1,0,0,1,1,0,0]]
		ran = random.choice(ranEXP)

		print(ran)

		l[1].ComputeNodes()
		l[2].ComputeNodes()
		l[3].ComputeNodes()


		c = 0
		k = 0

		lout1=0
		lout2=0
		for n in layers[3].nodeObjs:
			print(n.value)
			if n.value > 0.85:
				c+=1
			if n.value < 0.1:
				k+=1

		if c == 1 and k == 1:
			if ran[0] == 0 and ran[-1] == 1: # goric
				if layers[3].nodeObjs[0].value > 0.9 and layers[3].nodeObjs[1].value < 0.2:
					print("perfect1")
					file = open("wAndBSave.txt","w")
					file.write((' '.join(layers[1].listWeightsAndBiases())))
					file.write("\n")
					file.write((' '.join(layers[2].listWeightsAndBiases())))
					file.write("\n")
					file.write((' '.join(layers[3].listWeightsAndBiases())))
					break
			elif ran[0] == 1 and ran[-1] == 0: # jaric
				if layers[3].nodeObjs[1].value > 0.9 and layers[3].nodeObjs[0].value < 0.2:
					print("perfect2")
					file = open("wAndBSave.txt","w")
					file.write((' '.join(layers[1].listWeightsAndBiases())))
					file.write("\n")
					file.write((' '.join(layers[2].listWeightsAndBiases())))
					file.write("\n")
					file.write((' '.join(layers[3].listWeightsAndBiases())))
					break
		elif c == 2:
			for layer in [l[1],l[2],l[3]]:
				layer.ChangeNodes()
		else:
			for layer in [l[1],l[2],l[3]]:
				layer.ChangeNodes()

		if lout1 == layers[3].nodeObjs[0].value and lout2 == layers[3].nodeObjs[1].value:
			print("local/global minimum reached")
			break
		#time.sleep(1)

		lout1 = layers[3].nodeObjs[0].value
		lout2 = layers[3].nodeObjs[1].value

from layer import *

layers = []

l1 = 7
l2 = 3
l3 = 3
out = 2

cash = 0

layers.append(Inputlayer(l1))
layers.append(Hiddenlayer(layers[0],l2))
layers.append(Hiddenlayer(layers[1],l3))
layers.append(Outputlayer(layers[2],out))

train(layers)
