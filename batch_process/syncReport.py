#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","webingpilot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT assembly_id,completed_pledges_rate FROM ASSEMBLY_MEMBERS_TEMP")


	results = cursor.fetchall()

	for row in results:
		try:
			sql = "UPDATE ASSEMBLY_MEMBERS SET completed_pledges_rate = '{0}' WHERE assembly_id = {1}".format(row[1],row[0])
			print(sql)
			cursor.execute(sql)
		except Exception as e:
			print(e)
		

	db.commit()
except:
	db.rollback()

# disconnect from server
db.close()
