import datetime
import psycopg2
import bleach

""" In this file, we will define the queries,
    and run them one by one. Ideally, we want
    the final product to be displayed on a
    www server hosted as a guest. """

# first we test if our view is running.
def first_query():
    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    path_variable = "/article/"
    slug_variable = "a.slug"
    c.execute("""select a.title, count(*) as views
    from articles as a, log as l
    where a.slug = l.path
    group by a.title""", (path_variable))
    manyresults = c.fetchall()
    for row in manyresults:
        print (row)
    db.close()

first_query()
