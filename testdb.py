#!/usr/bin/python

hostname = 'localhost'
username = 'satishseshadri'
password = 'L0llipops$%'
database = 'test1'

print 'Hello'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT *  FROM information_schema.tables" )

    for table_catalog, table_schema, table_name, table_type in cur.fetchall() :
        print table_catalog, table_schema, table_name, table_type

print 'Using PyGreSQL…'
import pgdb
myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
doQuery( myConnection )
myConnection.close()

