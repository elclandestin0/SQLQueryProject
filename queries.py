qimport datetime
import psycopg2
import bleach

""" In this file, we will define the queries,
    and run them one by one. Ideally, we want
    the final product to be displayed on a
    www server hosted as a guest. """

def first_query():
    path_variable = "/article/"
    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    first_query = """select a.title, count (*) as views
    from articles as a
    join log as l
    on %s = l.path
    group by a.title"""
    c.execute(first_query,(path_variable + "a.slug", ))

    # Here, the first_query results are stored in a variable
    # by the fetch all command.
    first_query_results = c.fetchall()

    if c.rowcount == 0:
        print "Query returned no results!"
    else:
        for row in first_query_results:
            print (row)
    print "First query is complete"
    db.close()

first_query()
