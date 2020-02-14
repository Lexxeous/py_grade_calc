#coding: utf-8

#--------------------------------------------- IMPORTING MODULES --------------------------------------------#

import grades_utils as gu

#---------------------------------------------- ERROR CHECKING ----------------------------------------------#

# If count or percentage value is 0, set both to 0
if(gu.args.homework[0] == 0 or gu.args.homework[1] == 0):
	gu.args.homework[0] = 0
	gu.args.homework[1] = 0
if(gu.args.quizzes[0] == 0 or gu.args.quizzes[1] == 0):
	gu.args.quizzes[0] = 0
	gu.args.quizzes[1] = 0
if(gu.args.tests[0] == 0 or gu.args.tests[1] == 0):
	gu.args.tests[0] = 0
	gu.args.tests[1] = 0
if(gu.args.projects[0] == 0 or gu.args.projects[1] == 0):
	gu.args.projects[0] = 0
	gu.args.projects[1] = 0
if(gu.args.attendance[0] == 0 or gu.args.attendance[1] == 0):
	gu.args.attendance[0] = 0
	gu.args.attendance[1] = 0

# Dont allow any percentage values to exceed 100
if(gu.args.homework[1] > 100 or gu.args.quizzes[1] > 100 or gu.args.tests[1] > 100 or gu.args.projects[1] > 100 or gu.args.attendance[1] > 100):
	exit("ERROR: No percentage values may exceed 100.")

# Dont allow attendance to be counted more than once
if(gu.args.attendance[0] > 1):
	exit("ERROR: Attendance has a binary count value (0 ~ 1).")

# All percentage values must add up to 100
tot_perc = gu.args.homework[1] + gu.args.quizzes[1] + gu.args.tests[1] + gu.args.projects[1] + gu.args.attendance[1]
if(tot_perc != 100):
	print("Homework:", gu.args.homework[1],\
				"+ Quizzes:", gu.args.quizzes[1],\
				"+ Tests:", gu.args.tests[1],\
				"+ Projects:", gu.args.projects[1],\
				"+ Attendance:", gu.args.attendance[1],\
				"= Total:", tot_perc)
	exit("ERROR: All grade percentage values do not add up to 100.")

#---------------------------------------------- INITIALIZATION ----------------------------------------------#

range_offset = 1 # the "range()" function is non inclusive on the upper bound

for s in range(1, gu.args.students[0] + range_offset):
	s_name = input("\nWhat is the students name?: ")
	print("Give all inputs as a whole number percentage (0 ~ 100).\n")

	h_arr = [] # homework array
	q_arr = [] # quizzes array
	t_arr = [] # tests array
	p_arr = [] # projects array
	a_arr = [] # attendance array
	grades_array = [] # list of weighted grades

	#---------------------------------------------- HOMEWORK LIST ----------------------------------------------#

	if(gu.args.homework[0] != 0):
		for h in range(1, gu.args.homework[0] + range_offset): # for all of the homework
			curr_h = -1 # initialize current homework grade as invalid
			while(gu.out_of_range(curr_h)): # loop until grade is within proper range
				try:
					curr_h = float(input(s_name + "\'s grade for homework " + str(h) + ": ")) # get a input string value
					if(gu.out_of_range(curr_h)): print("Value out of bounds...")
				except ValueError:
					print("Must be a numeric value...")
			h_arr.append(curr_h) # add current quiz grade to the list
		h_tot = (sum(h_arr)/len(h_arr)) * (gu.args.homework[1]/100.0) # get the weighted average
		grades_array.append(h_tot) # add the weighted average to the grades list
		print(s_name + "\'s total homework grade:", h_tot, '/', gu.args.homework[1], "\n")

	#------------------------------------------------ QUIZ LIST ------------------------------------------------#

	if(gu.args.quizzes[0] != 0):
		for q in range(1, gu.args.quizzes[0] + range_offset): # for all of the quizzes
			curr_q = -1 # initialize current quiz grade as invalid
			while(gu.out_of_range(curr_q)): # loop until grade is within proper range
				try:
					curr_q = float(input(s_name + "\'s grade for quiz " + str(q) + ": ")) # get a input string value
					if(gu.out_of_range(curr_q)): print("Value out of bounds...")
				except ValueError:
					print("Must be a numeric value...")
			q_arr.append(curr_q) # add current quiz grade to the list
		q_tot = (sum(q_arr)/len(q_arr)) * (gu.args.quizzes[1]/100.0) # get the weighted average
		grades_array.append(q_tot) # add the weighted average to the grades list
		print(s_name + "\'s total quiz grade:", q_tot, '/', gu.args.quizzes[1], "\n")

	#------------------------------------------------ TEST LIST ------------------------------------------------#

	if(gu.args.tests[0] != 0):
		for t in range(1, gu.args.tests[0] + range_offset): # for all of the tests
			curr_t = -1 # initialize current test grade as invalid
			while(gu.out_of_range(curr_t)): # loop until grade is within proper range
				try:
					curr_t = float(input(s_name + "\'s grade for test " + str(t) + ": ")) # get a input string value
					if(gu.out_of_range(curr_t)): print("Value out of bounds...")
				except ValueError:
					print("Must be a numeric value...")
			t_arr.append(curr_t) # add current test grade to the list
		t_tot = (sum(t_arr)/len(t_arr)) * (gu.args.tests[1]/100.0) # get the weighted average
		grades_array.append(t_tot) # add the weighted average to the grades list
		print(s_name + "\'s total test grade:", t_tot, '/', gu.args.tests[1], "\n")

	#------------------------------------------------ PROJ LIST ------------------------------------------------#

	if(gu.args.projects[0] != 0):
		for p in range(1, gu.args.projects[0] + range_offset): # for all of the projects
			curr_p = -1 # initialize current project grade as invalid
			while(gu.out_of_range(curr_p)): # loop until grade is within proper range
				try:
					curr_p = float(input(s_name + "\'s grade for project " + str(p) + ": ")) # get a input string value
					if(gu.out_of_range(curr_p)): print("Value out of bounds...")
				except ValueError:
					print("Must be a numeric value...")
			p_arr.append(curr_p) # add current test grade to the list
		p_tot = (sum(p_arr)/len(p_arr)) * (gu.args.projects[1]/100.0) # get the weighted average
		grades_array.append(p_tot) # add the weighted average to the grades list
		print(s_name + "\'s total project grade:", p_tot, '/', gu.args.projects[1], "\n")

	#------------------------------------------------ ATTENDANCE -----------------------------------------------#

	if(gu.args.attendance[0] != 0):
		for a in range(1, gu.args.attendance[0] + range_offset): # for all of the attendance
			curr_a = -1 # initialize current attendance grade as invalid
			while(gu.out_of_range(curr_a)): # loop until grade is within proper range
				try:
					curr_a = float(input(s_name + "\'s grade for attendance: ")) # get a input string value
					if(gu.out_of_range(curr_a)): print("Value out of bounds...")
				except ValueError:
					print("Must be a numeric value...")
			a_arr.append(curr_a) # add current test grade to the list
		a_tot = (sum(a_arr)/len(a_arr)) * (gu.args.attendance[1]/100.0) # get the weighted average
		grades_array.append(a_tot) # add the weighted average to the grades list
		print(s_name + "\'s total attendance grade:", a_tot, '/', gu.args.attendance[1], "\n")

	#-------------------------------------------------- OUTPUT -------------------------------------------------#

	overall = sum(grades_array)

	if(overall >= 90.0):
		print(s_name, "has earned a final course score of", overall, "=> A.")
	elif(overall >= 80.0 and overall < 90.0):
		print(s_name, "has earned a final course score of", overall, "=> B.")
	elif(overall >= 70.0 and overall < 80.0):
		print(s_name, "has earned a final course score of", overall, "=> C.")
	elif(overall >= 60.0 and overall < 70.0):
		print(s_name, "has earned a final course score of", overall, "=> D.")
	else:
		print(s_name, "has earned a final course score of", overall, "=> F.")

