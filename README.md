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
* To load the data, use the command `psql -d news -f newsdata.sql`
  **Here's what this command does:**
* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql
* Once into Virtual Machine you can use `psql -d news` and create the views given below in the **Views used** section
* Now run logsAnalysis.py and you will get the output of the required questions

## Views used

* fr view ( Gives the path and there respective views)
`create view fr as select path, count(*) as views from log where path != '/' group by path order by views desc limit 5;`
* First view ( Joins the authors and articles table on author.id and articles.author)
`create view First as select authors.name, articles.slug from authors join articles on authors.id = articles.author;`
* ntotalViews (Gives the outputV column with date and count of the total views for each day) 
`create view ntotalViews as
select date(time) as outputV,count(status) from log group by outputV;`
* ntotalErrors (Gives the outputE column with date and count of the total error status views for each day) 
`create view ntotalErrors as
select date(time) as outputE,count(status) from log where status like '%404%' group by outputE;`
* percentn view (Gives the Output in the date format and the Error percent columns with precision upto two digits)
`create view percentn as
select ntotalErrors.outputE,round(cast(cast(ntotalErrors.count as float)/ cast(ntotalViews.count as float)*100 as numeric),2) from ntotalViews join ntotalErrors on ntotalViews.outputV = ntotalErrors.outputE;`

## Author

* **Ankush Sankhe** - *Python scripting and creating Database queries and views* 


## Acknowledgments

* **Udacity** for teaching Python DB-API and SQL.
* Hat tip to anyone who's code was used.
