# Group Project,  Part 1

# Project 1: Unit Testing
*Revised: 7/08/26*

## General Instructions

**Introduction**

This assignment allows you to apply the concepts in this class in a working program. Java or Python or recommended, but you can do this in any language where you have experience.

**Group Work**

This is a *group collaboration assignment*. You will need to choose a group for this assignment. If you would like to work individually, you can do that too. If you work as a group, but all names on your assignment. Let me know your groups in Slack.

**Special Instructions for submitting in Git Hub.**

1. You should simulate a "real world experience," by doing your work in a new branch. Before you submit, merge it into the main branch (pull request). I'll only look at the main branch in this class, and I will assume that any branches are works in progress.  You can make as many branches as you want.  I won't look at them. 
1. Submit the link to your Git Hub repository in Slack. I will not look for your assignment unless I see this, and if I don't see this I will assign a zero since it will appear to me that the assignment was not turned in.
1. Your assignments in your Git Hub Repo should be organized in Directories with Markdown files.  See "sample-github-structure." 

## Part 1: Write a program in the language of your choice to determine "valid triangle" and "type of triangle" based on input of 3 sides

- Using an IDE of your choice, write a program that accepts three values for the length of the sides of a triangle, and returns:
  - Is the triangle valid?
  - the type of triangle, e.g. scalene, isosceles, or equilateral. Be sure to read Chapter 1 of the text so that you are aware of the types of things to think about when making this program robust.

## Part 2: Handling "Rainy Day Cases"

Add code to handle "rainy day cases," e.g. the user enters a side that is zero. There are different ways to do this. You can handle errors with program logic or you can write custom exceptions.

## Part 3: Write Unit Tests

Write Unit Tests using the testing libraries for your language (e.g. Junit) to represent at least three of the test cases described in Chapter 1 of the text. For example:

- Test for a valid triangle.
- Test for scalene triangle
- Test that accepts the sides of a scalene triangle in all possible orders
- Test that accepts a zero length side

## Deliverables

- You will submit writeup of the exercise covering the following points in the Rubric. Use section headers for each part.

## Rubric Summary

| CRITERIA | QUESTIONS TO ADDRESS |
|---|---|
| **Introduction** | Provide an overview of the program, how you handled errors, and your choice of Unit Tests. |
| **Details of the program** | What IDE did you use? How did you get data into the program? Driver file, prompt user for input, menu, read data from a file, through your Unit tests only? Did you write results to a file? |
| **Table with example test data** | What test data did you input into the program. |
| **Unit Tests** | Describe the Unit Tests you created. Why did you choose those. |
| **Bugs encountered during testing.** | Describe any bugs you encountered as the result of your testing and what did you do to fix them? |
| **Problems** | What kinds of problems did you encounter. |
| **Screen Shots** | Includes screen shots showing successful program runs and Unit test runs. Clearly label each. |

> **Submit the link to your Git Hub Repo in Slack after you merge your project into the main branch (pull request).  Follow the Rubric directly above.**

