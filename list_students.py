
import sqlite3
from os.path import exists
import sys

#academic_year_input = int(sys.argv[1])

if exists('cs_course_scheduling.sqlite'):
    conn = sqlite3.connect('cs_course_scheduling.sqlite')

    cursor = conn.execute("SELECT first_name, last_name, academic_year FROM students ORDER BY last_name")

    html_head = "<head><title>Student List</title></head>\n"
    html_header = "<h1> Student List</h1>\n"
    html_table = "<table border='1'><tr><th>first name</th><th>last name</th><th>year</th></tr>\n"
    for row in cursor:
        html_table += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n"
    html_table += "</table>"

        #print ("First Name = ", row[0])
        #print ("Last Name = ", row[1])
        #print ("Academic Year = ", row[2])
        #print ("----------------------------------------")
         
    conn.close()
    print("Database was accessed and closed")        

else:
    print('Database file cs_course_scheduling.sqlite not found in current working directory.')

with open('list_student.html','w') as html:
    html.write("<html>" + html_head + html_header + "<body>" +html_table +"</body></html>")
print("Successfully created list_student.html")

