#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","Starter?5","WEBING-PILOT" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT AS_MEM.assembly_id, CA_MEM.candidacy_id FROM ASSEMBLY_MEMBERS as AS_MEM INNER JOIN CANDIDACY_MEMBERS as CA_MEM ON AS_MEM.name = CA_MEM.name AND AS_MEM.birth = substr(CA_MEM.birth,1,4)")


	results = cursor.fetchall()

	for row in results:
		print "update assembly id to %d on row that candidacy_id is %d" % (row[0],row[1])
		cursor.execute("UPDATE CANDIDACY_MEMBERS SET assembly_id = %d WHERE candidacy_id = %d" % (row[0],row[1]))

	db.commit()
except:
	db.rollback()

# disconnect from server
db.close()
