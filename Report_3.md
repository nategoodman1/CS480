# Report 3

## How do we test things?

We plan to create an answer key of the sample data provided to us by solving it by hand. 
Once we have an answer key we will be running our program to compare the results to the answer key to see where there are disparities in the matching which will ideally allow us to fine tune our algorithm and see where it is messing up. 
Additionally, we would like to allow others to test the GUI and give us feedback as to whether or not we should change anything for further clarity on how it works.

## What did we find?

We found that the csv default library is a valuable resource and that the files read in just as we need them to without any data cleaning needed. 
Tkinter is also a nice resource for us to utilize as it provides everything we need for a GUI.

## What prototypes have we made?

We made a prototype gui using tkinter containing all the elements for the gui that we expect the final version of this project to contain.

## What have we done so far?

We have implemented a csv parser that works exactly as we want it to. 
We are working on implementing custom classes for both the students and the schedules to make the data easier to work with. 
Finally, we have implemented a GUI that looks nicer than the one we made in paint.

## Problems encountered so far:

As of this point, our project is progressing steadily. 
We are having minor issues with the process of sorting our data in an appropriate manner; however, this will be cleaned up with little issues. 
The glaring issue is obviously our algorithm as we understand what we want it to do, but the implementation has been challenging to wrap our heads around. 
We are still fluctuating between the ideas of sorting data and assigning it as opposed to assigning weights to each student and selecting classes for students utilizing those weights.

## Current state of the project:

Currently, we have working implementations of the csv parser and our GUI. 
Under development we have the matching algorithm itself and the data sorting to finish as well as final touches to the custom classes. 
What we would like to do is fine tune the algorithm in the long run as well as explore alternative options as data containers to further improve the runtime of our project.

## What you plan to do next:

Implement a matching algorithm to match the students to respective classes as well implement sorting algorithms to sort the lists that have gone through the csv parser. 
Using classes the students have taken as our parameter, students will be sorted in the order of least to most flexible.