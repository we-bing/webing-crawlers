#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","webingpilot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT city_code,district_name,district_code FROM DISTRICTS")


	results = cursor.fetchall()

	for row in results:
		try:
			sql = "UPDATE TOWNS SET district_code = {0} WHERE city_code = {1} AND district_name = '{2}'".format(row[2],row[0],row[1])
			print(sql)
			cursor.execute(sql)
		except Exception as e:
			print(e)
		

	db.commit()
except:
	db.rollback()

# disconnect from server
db.close()
