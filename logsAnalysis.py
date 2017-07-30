#/usr/bin/python2.7.12
#
#

import psycopg2

# load the psycopg extras module
import psycopg2.extras

# Try to connect
try:
    db = psycopg2.connect("dbname=news")
except BaseException:
    print "I am unable to connect to the database."

cur = db.cursor()
imp = "(regexp_split_to_array(path, E'/article/'))[2]"
query1 = "select articles.title, count(*) as views from articles join log on articles.slug = " + \
    imp + " where path != '/' group by " + imp + ", articles.title order by views desc limit 3;"
view1 = "create view First as select authors.name, articles.slug from authors join articles on authors.id = articles.author;"
query2 = "select authors.name, count(*) as views from authors join First on authors.name = First.name join log on First.slug = " + \
    imp + "where path != '/'group by authors.name order by views desc;"
query3 = "select * from Answer where ErrorPercent > 1;"
# Question 1 Solution
try:
    cur.execute(query1)
except BaseException:
    print "I can't SELECT from query1"

rows = cur.fetchall()
print("Most popular three articles of all time are:");
for item in rows:
    # print item
    print('{} {} {}'.format(item[0], "==>", item[1]))

# Question 2 Solution
try:
    cur.execute(query2)
except BaseException:
    print "I can't SELECT from query2"

rows = cur.fetchall()
print("\nMost popular article authors of all time are:");
for item in rows:
    # print item
    print('{} {} {}'.format(item[0], "==>", item[1]))

# Question 3 Solution
try:
    cur.execute(query3)
except BaseException:
    print "I can't SELECT from query3"

rows = cur.fetchall()
print("\nFollowing days leads to errors which are more than 1% of requests")
for item in rows:
    # item
    print('{} {} {}'.format(item[0], "==>", item[1]))
db.close()
