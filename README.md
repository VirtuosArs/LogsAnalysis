# Logs Analysis Project

Logs Analysis is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See how to run section for notes on how to deploy the project on a live system.

### Prerequisites

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.


## How to Run

* In order to bring the virtual machine online use `vagrant up`
* Then log into it with `vagrant ssh`
* Change the directory to vagrant use `cd/vagrant`
* Once into Virtual Machine you can use `psql` and create the views given below in the **Views used** section
* Now run logsAnalysis.py and you will get the output of the required questions

## Views used

* First view ( Joins the authors and articles table on author.id and articles.author)
`create view First as select authors.name, articles.slug from authors join articles on authors.id = articles.author;`
* totalViews (Gives the outputV column in the required date format and count of the total views for each day) 
`create view totalViews as
select to_char(time,'FMMonth FMDDth yyyy') as outputV,count(status) from log group by outputV;`
* totalErrors (Gives the outputE column in the required date format and count of the total error status views for each day) 
`create view totalErrors as
select to_char(time,'FMMonth FMDDth yyyy') as outputE,count(status) from log where status like '%404%' group by outputE;`
* Answer view (Gives the Output in the date format and the Error percent columns)
`create view Answer as
select totalErrors.outputE,cast(cast(totalErrors.count as float)/ cast(totalViews.count as float)*100 as float) as Errorpercent from totalViews join totalErrors on totalViews.outputV = totalErrors.outputE;`

## Author

* **Ankush Sankhe** - *Python scripting and creating Database queries and views* 


## Acknowledgments

* **Udacity** for teaching Python DB-API and SQL.
* Hat tip to anyone who's code was used.
