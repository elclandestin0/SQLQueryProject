import datetime
import psycopg2
import bleach
import csv

""" In this file, we will define the queries,
    and run them one by one. Ideally, we want
    the final product to be displayed on a
    www server hosted as a guest. """


def get_slugs():
    """This function gets the slugs as tuples,
        parses them into strings, and then is
        returned as a list called
        variables_of_slugs in order for us to
        use in the first query!"""
    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    get_slugs_query = """select slug from articles"""
    c.execute(get_slugs_query)
    variables_of_slugs = c.fetchall()
    for row in variables_of_slugs:
        print(row)
    return variables_of_slugs

def first_query():
    variables = ['/article/bad-things-gone',
                 '/article/balloon-goons-doomed',
                 '/article/bears-love-berries',
                 '/article/candidate-is-jerk',
                 '/article/goats-eat-googles',
                 '/article/media-obsessed-with-bears',
                 '/article/trouble-for-troubled',
                 '/article/so-many-bears']

    #slugs = get_slugs()
    #path_variable = "/article/"
    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()
    first_query = """select a.title, count (*) as views
    from articles as a
    left join log as l
    on %s = l.path
    group by a.title
    order by views desc"""

    for row in range(len(variables)):
         c.execute(first_query, (variables[row],))
         results = c.fetchall()
         print(results)


    # Here, the first_query results are stored in a variable
    # by the fetch all command.

    # if c.rowcount == 0:
    #     print "Query returned no results!"
    # else:
    #     for row in first_query_results:
    #         print(row)
    #
    # for row in slugs:
    #     print(row)
    #
    # print "First query is complete"
    # db.close()

first_query()
# get_slugs()
