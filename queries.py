import datetime
import psycopg2
import bleach
import csv

"""In this file, we will define the queries,
    and run them one by one. Ideally, we want
    the final product to be displayed on a
    www server hosted as a guest."""



def first_query():
    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    first_query = """select a.title, count(*) as views
    from articles as a join log as l
    on l.path like concat('%', a.slug)
    group by a.title
    order by views desc
    fetch next 3 rows only"""
    c.execute(first_query)
    first_query_results = c.fetchall()
    # Here, the first_query results are stored in a variable
    # by the fetch all command.

    if c.rowcount == 0:
        print "Query returned no results!"
    else:
        for row in first_query_results:
            print(row)
    print "First query is complete"
    db.close()


first_query()


# user_input = input("""Hello and welcome to the Logs analysis
#       program! Please select the following:
#       1) Find the top 3 articles of all time
#       2) Find the top 3 authors of all time
#       3) Find the day where more than 1 percent
#       of the requests lead to errors""")

# if user_input == 1:
#     first_query()
