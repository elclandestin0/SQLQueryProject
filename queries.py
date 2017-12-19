import datetime
import psycopg2
import bleach
import csv

"""In this file, we will define the queries,
    and run them one by one. Ideally, we want
    the final product to be displayed on a
    www server hosted as a guest."""


def first_query():
    """In the first query, we want to fetch
    the top 3 rows that contain the article
    names with the greatest views"""

    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()

    # Our first query selects the article title
    # and it's number of views after aggregating
    # the database to match the path name LIKE
    # the slug name. The reason why we use LIKE
    # is to concatenate the "/article/" to the
    # article's slug. Doing this successfully
    # matches the article's appended slug with
    # the log path. After receiving those results,
    # fetch only the first 3 rows to get the three
    # juiciest articles of all time!

    first_query = """select a.title, count(*) as views
    from articles as a, log as l
    where l.path like concat('/article/', a.slug)
    group by a.title
    order by views desc
    fetch next 3 rows only"""
    c.execute(first_query)
    first_query_results = c.fetchall()
    # Here, the first_query results are stored in
    # a variableby the fetch all command. We print
    # no results if there are no rows. Otherwise
    # we print the results of the query, tuple by
    # tuples
    if c.rowcount == 0:
        print "Query returned no results!"
    else:
        for row in first_query_results:
            print(row)
    print "First query is complete"
    db.close()


def second_query():
    """In the second query, we want to fetch the top
    authors of all time. We add on top of the logic of
    our first query by making sure that the author of
    article (id) = the id of the author."""

    db_name = "news"
    db = psycopg2.connect(dbname=db_name)
    c = db.cursor()

    # First, we select the author name and number of hits
    # that were aggregated from equating the author ID with
    # the article's author (in ID), AND equating the path of
    # the log with the concatenated slug of the article.
    # Since we
    second_query = """select auth.name, count(*) as views
    from articles as art, authors as auth, log as l
    where art.author = auth.id and l.path like concat('%', art.slug)
    group by auth.name
    order by views desc"""
    c.execute(second_query)
    second_query_results = c.fetchall()

    if c.rowcount == 0:
        print "Second query returned no results!"
    else:
        for row in second_query_results:
            print(row)
    print "Second query is complete"
    db.close()

# first_query()
second_query()

# user_input = input("""Hello and welcome to the Logs analysis
#       program! Please select the following:
#       1) Find the top 3 articles of all time
#       2) Find the top 3 authors of all time
#       3) Find the day where more than 1 percent
#       of the requests lead to errors""")

# if user_input == 1:
#     first_query()
