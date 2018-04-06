# Introduction

To do this project, I created a file that has the functions that are needed for this project, shown in the assignment. In addition, I created another file that uses one of the functions that I wrote to create a web application for the user to see a graphic output.

# Objective
* Develop an application to calculate metrics
* Provide tables to visualize data results
* Provide charts to visualize data results
* Bonus: use a toolkit to create a dashboard to access the results.

# Requirements
* R or Python must be used as programming language for this exercise.

# Functions
def retailer_affinity(focus_brand): a function that given a brand, returns the strongest retailer affinity relative to other brands

def count_hhs(brand=None, retailer=None, start_date=None, end_date=None): a function that returns the number of households (a household could have many transactions in the provided dataset), allowing for a dynamic optional set of inputs

def top_buying_brand(): identify brand with top buying rate ($ spent/HH)

# How it works

There are two files I used for this project: data.py and web.py.

## data.py
I chose to use the csv file, and used pandas to parse it into a dataframe.
For each of the questions, I would iterate through the rows of the dataframe to see if the query that I wanted was matched, and record the data into a dictionary. I then used an import called operator to sort the dictionaries, which turned them into tuples, and returned the sorted list of tuples for the first and third function.

When running data.py, the user inputs the brand and sees the biggest to smallest retailer affinities.

The second function has a static input with some parameters put in, and outputs the number of households. It could also be changed to output which household ID made the most purchases in terms of how many trips they made.

The third function is also automatically called for, and prints out the top buying brands from the ones that make the most money to the ones that make the least amount.

## web.py

In order to run this, the user must have dash, dash_core_components, and dash_html_components installed, as well as plotly.graph_objs.

Run 'python web.py', and when it starts running, go to https://127.0.0.1:8050/ on a web browser to access the web application.

From there, the user can choose one of the options on the drop down menu and after one is selected (or the option 'Red Bull' will be default), a bar graph will appear showing the units sold per retailer.

# Limitations

Unfortunately, since the dataset is so large, every time it ran one of the functions it would take a while to execute looping through each row, and in the way that I wrote my functions, the body would be the same in looping through but taking out different parameters of the row from the dataset.

A way to fix this might be to put all of this data into an SQL database using sqlite3, and fetching the queries by using the SQL commands, or by using streams, but I am unsure whether or not python has streams, and java was not an option for the requirements for the project.

In the second function, I found that the csv file dates are not completely sorted, so I looped through the entire dataset in order to not miss a potential data point. For example, even though typically the dates go in order, sometimes the rows with 1/3/2014 came before several rows with the date 1/2/2014.

In addition, I was confused on the third question, "Identify brand with top buying rate ($spent/HH)", on what it was looking for. Therefore, I created a function that returns the brand that had the most revenue (item units x item dollars), since I didn't understand where the household comes in.

In web.py, the only graph that is displayed is the biggest retailer affinity for the desired product. This could be improved upon if my function had also returned other parameters, such as seeing the trends of buying the brand throughout the months.
