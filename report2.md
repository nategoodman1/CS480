# Report 2

## General Program Design Plan

Our program will operate in this general structure:
1. Sort list of TAs by graduation date
2. Generate class preferences for each TA
3. Generate TA preferences for classes
3. Use Gale-Shapley algorithm to assign TAs classes based on their preferences
4. Check for any possible errors
5. Fix errors if possible
6. Output final list

## Project Flow

The first issue we will need to overcome is the reading and storing of data from the csv file.
This is necessary to complete first because we will need this information to functionally test other pieces of the program.
Once we have the data stored we will sort the list of TAs by graduation date, accounting for classes that still need to be taken.
The list sorting portion can be in development in concurrence with the file reading segment.
After the sorted list is complete we will use the data from the file to generate a list of class preferences for each TA, taking into consideration every restriction and need (in person vs online, class experience, etc.).
We will also generate preferences of TAs for each class.
We expect this to be much simpler as there are fewer requirements for classes than TAs.
Once we have a list of preferences from each TA we will use a variation of the Gale-Shapley matching algorithm to match TAs to classes favoring TAs.
Because the information we are using for this segment is so rooted in the data from the CSV files, this will likely need to be developed after we have previous parts completed.
After we have TAs matched with classes we will check the matchings for any possible complications or errors and fix them accordingly.

## Algorithm

We plan to use a variation of the Gale-Shapley stable matching algorithm for this project.
It is a variation because for each class there will be up to two TAs.
The algorithm will start by matching TAs to classes based on their top preferences, starting at the top of the list (graduating soonest), with the class accepting its most preferred TAs.
The algorithm will then go into another round, with the classes accepting their most preferred TAs regardless of whether they have already been matched with.
This process will repeat until every TA slot has been filled.

## What we Have Done so Far

- Researched possible matching algorithms and settled with Gale-Shapley
- Addressed different scenarios to resolve potential matching issues
- Strategized and planned general approaches on how to list and prioritize the students based on preference and graduation status

## Problems Encountered

- Identifying the manner in which we will be reading in the CSV due to the many different methods of sorting that must be done

## Current State

- Implemented a mostly functional read-in of CSV files
- General outline of project completed

## What We Plan to do Next

- Sort list of TAs by graduation date to ensure they get the slots they need
- Implement the Gale-Shapley algorithm
