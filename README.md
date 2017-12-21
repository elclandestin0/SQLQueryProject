# SQLQueryProject
A sample SQL database project that contains 3 sample queries in the queries.py
file, written in Python.

To connect to the database, make sure you have <code>psql</code> installed on your terminal
as a command. Then, unzip the <code>newsdata.zip</code> to get a <code>newsdata.sql</code> file, and move that
file to your directory. <code>cd</code> into the directory, and run the following commands:
- <code> psql </code>
- <code> -d news </code>
- <code> -f newsdata.sql </code>
This connects to the installed database, creates the tables from the file, and populates
them with data. From there, you can run many <code> psql </code> commands to query the
data, or to explore the relations and their respective columns of data.

To run this application, change directory into this application via bash and run
the command: "python queries.py" from bash. You are then given 3 different queries
to choose from:
1) Find the top 3 articles of all time based on views.
2) Find the top authors of all time on an aggregation count of all article views
   by the same actor.
3) Find the day(s) where the number of errors a website encountered is greater than 1%.
0) Exit the program.

For the results on those queries, kindly refer to the results.txt file.
