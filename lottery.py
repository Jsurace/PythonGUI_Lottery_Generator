"""
Program: lottery.py
Author: Jenna
Date: 3/27/2019

Program which will continuously randomly generate a series of numbers 
for a lottery number generator. 
** Requires breezypythongui.py file within same directory in order to 
see results with EasyFrame. 
"""
from breezypythongui import EasyFrame
import random

class LotteryGame(EasyFrame):

	def __init__(self):
		# Creates window & widget layout
		EasyFrame.__init__(self, title = "Lottery Generator", background = "light blue", width = 450, height = 260)

		# Label for Lottery Number Generator header
		headerPanel = self.addPanel(row = 0, column = 0, columnspan = 4, background = "Aqua")
		headerPanel.addLabel(text = "Lottery Number Generator", row = 0, column = 0, columnspan = 4,
		sticky = "NSEW", background = "slate gray", foreground = "black", font = "Algerian")

		# Lottery Numbers
		numPanel = self.addPanel(row = 1, column = 0, background = "black")
		self.num1 = numPanel.addIntegerField(value = 0, row = 0, column = 0, width = 3)
		self.num2 = numPanel.addIntegerField(value = 0, row = 0, column = 1, width = 3)
		self.num3 = numPanel.addIntegerField(value = 0, row = 0, column = 2, width = 3)
		self.num4 = numPanel.addIntegerField(value = 0, row = 0, column = 3, width = 3)
		self.num5 = numPanel.addIntegerField(value = 0, row = 0, column = 4, width = 3)
		

		# Button for Generator
		self.addButton(text = "Generate", row = 1, column = 0, columnspan = 4, command = self.randomNum)
		# text label
		outterPanel = self.addPanel(row = 2, column = 0, background = "Aqua", columnspan = 4)
		outterPanel.addLabel(text = "Test your luck -- Good Luck!", row = 0, column = 0, 
		columnspan = 2 , sticky = "NSEW", foreground = "light blue", background = "black", font = "Algerian")

	# Random number generator function
	def randomNum(self):
		q = random.randint(1, 55)
		w = random.randint(1, 55)
		e = random.randint(1, 55)
		r = random.randint(1, 55)
		t = random.randint(1, 55)

		self.num1.setNumber(q)
		self.num2.setNumber(w)
		self.num3.setNumber(e)
		self.num4.setNumber(r)
		self.num5.setNumber(t)
		
def main():
	LotteryGame().mainloop()

main()
