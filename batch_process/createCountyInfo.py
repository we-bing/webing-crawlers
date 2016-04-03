#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","webingpilot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT city_code,town_name FROM towns")


	results = cursor.fetchall()
	countySet = set();
	for row in results:
		try:
			originTownName = row[1].split(' ');
			countyName = originTownName[0]
			# print(countyName)
			if(countyName.decode('utf-8') not in countySet):
				# print(countyName)
				countySet.add(countyName.decode('utf-8'))
				sql = "INSERT INTO COUNTYS(city_code,county_name) VALUES({0}, '{1}')".format(row[0],countyName)
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
