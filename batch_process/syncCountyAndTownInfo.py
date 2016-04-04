#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","webingpilot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT county_code,county_name,city_code FROM COUNTYS_TEMP")


	results = cursor.fetchall()
	for row in results:
		try:
			sql = "UPDATE TOWNS_TEMP SET county_code = {0} WHERE town_name REGEXP '{1}' AND city_code = {2}".format(row[0],row[1],row[2])
			print(sql)
			cursor.execute(sql)
		except Exception as e:
			print(e)
		
	# print(countySet)
	db.commit()
except:
	db.rollback()

# disconnect from server
db.close()
