#/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","webingpilot" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
	# execute SQL query using execute() method.
	cursor.execute("SELECT town_code,town_name FROM towns_temp")
	# cursor.execute("SELECT city_code,town_name,district_code FROM towns_temp")


	results = cursor.fetchall()
	countySet = set();
	for row in results:
		try:
			originTownName = row[1].split(' ');
			# countyName = originTownName[0]
			# print(countyName)
			# countyHash = countyName + str(row[2])
			# if(countyHash.decode('utf-8') not in countySet):
				# print(countyHash.decode('utf-8'))
				# countySet.add(countyHash.decode('utf-8'))
				# sql = "INSERT INTO COUNTYS_TEMP(city_code,county_name) VALUES({0}, '{1}')".format(row[0],countyName)
				# print(sql)
				# cursor.execute(sql)
			townName = originTownName[1]
			sql = "UPDATE towns_temp SET town_name = '{0}' WHERE town_code = {1}".format(townName,row[0])
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
