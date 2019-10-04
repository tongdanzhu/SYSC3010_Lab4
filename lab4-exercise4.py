#!/usr/bin/env python3
import sqlite3
dbconnect = sqlite3.connect("sensor.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen" OR type="door"');
for row in cursor:
	print(row['sensorID'],row['type'],row['zone']);
dbconnect.close();
