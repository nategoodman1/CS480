# CS 480 TA Assignment Program - Assigns TAs to Classes

Tools needed to run this program include: Python 3, required .csv files<br>
To build, run main.py, select appropriate files, select output location, select appropriate quarter and year, and click "generate matches" button

## How Program is Structured:
Converts the .csv files into student objects and schedule objects<br>
Gets the quarters till graduation<br>
Sorts both the students and the schedules into lists<br>
Run the matching algorithm<ul>
	Checks if student has taken the proper classes<br>
	Checks if student is eligible to TA based on location<br>
	Checks if student has the correct timeslots<br>
	Appends all selected students to a list in the order of matched classes</ul>
Converts list to .csv file and outputs it to the proper location<br>
<br />
Noted issue: if no start time is given for a class, it will output an empty list<br>
<br />
Contributers: Zack Perkins, Kyle Atchley, Nate Goodman, Abdiasis Abdi