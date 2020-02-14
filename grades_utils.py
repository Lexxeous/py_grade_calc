#coding: utf-8

#------------------------------------------ HANDLING CMD LINE ARGS ------------------------------------------#

general = "Grade calculator. " 
perc = "All percentage values must add to 100. " 
quantity = "There is no limit on the quantity of assignments. "
att = "The attendance quantity must be either 0 or 1. "
desc = general + perc + quantity + att

import argparse
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-w", "--homework", type=int, help="Homework count, Homework percentage value.", nargs=2, metavar=("W_COUNT", "W_PERC"), default=[4, 10], required=False)
parser.add_argument("-q", "--quizzes", type=int, help="Quiz count, Quiz percentage value.", nargs=2, metavar=("Q_COUNT", "Q_PERC"), default=[4, 15], required=False)
parser.add_argument("-t", "--tests", type=int, help="Test count, Test percentage value.", nargs=2, metavar=("T_COUNT", "T_PERC"), default=[4, 25], required=False)
parser.add_argument("-p", "--projects", type=int, help="Project count, Project percentage value.", nargs =2, metavar=("P_COUNT", "P_PERC"), default=[4, 40], required=False)
parser.add_argument("-a", "--attendance", type=int, help="Attendance count, Attendance percentage value.", nargs=2, metavar=("A_COUNT", "A_PERC"), default=[1, 10], required=False)
parser.add_argument("-m", "--max_grade", type=int, help="Upper bound for potential score; letter grade still calulated based on 100.", nargs=1, default=[100], required=False)
parser.add_argument("-s", "--students", type=int, help="Number of students grades to calculate.", nargs=1, default=[1], required=False)
args = parser.parse_args()
print(args)

#--------------------------------------------- HELPER FUNCTIONS --------------------------------------------#

def out_of_range(val):
	if(val < 0.0 or val > args.max_grade[0]):
		return True
	else:
		return False
