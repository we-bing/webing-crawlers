#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","Starter?5","WEBING-PILOT" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT AS_MEM.assembly_id, BI_KEY.keyword_id FROM ASSEMBLY_MEMBERS as AS_MEM INNER JOIN BILL_KEYWORDS as BI_KEY ON AS_MEM.name = BI_KEY.name AND AS_MEM.birth = BI_KEY.birth")


	results = cursor.fetchall()

	for row in results:
		cursor.execute("UPDATE BILL_KEYWORDS SET assembly_id = %d WHERE keyword_id = %d" % (row[0],row[1]))

	db.commit()
except:
	db.rollback()

# disconnect from server
db.close()
