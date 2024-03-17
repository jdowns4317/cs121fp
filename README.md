Constributors: James Downs, Thorsen Kristufek

This application is an interactive college database containing information on all of the colleges in the United States. Some of the information includes their admission rate, undergraduate enrollemnt, city's population, and sports programs offered.

The data for our application comes from the following links: https://collegescorecard.ed.gov/data/  https://nces.ed.gov/ipeds/datacenter/datafiles.aspx?sid=e17cda03-f05c-41db-898a-687ee2694b6f&rtid=1 https://www.ncaa.org/sports/2016/12/14/shared-ncaa-research-data.aspx      https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-cities-and-towns.html

NOTE that this program was tested in MySQL 8.3.0.

Run the commands from the final project spec: 

$ cd our-downloaded-files

$ mysql

mysql> source setup.sql;

mysql> source load-data.sql;

mysql> source setup-passwords.sql;

mysql> source setup-routines.sql;

mysql> source grant-permissions.sql;

mysql> source queries.sql; 

mysql> quit;

python3 app-client.py OR python3 app-admin.py 
to run the application (without any command line arguments)
There are no files written to the user's system.

Some unfinished features we have include: Extra checking code to ensure some of the command line user input doesn't throw SQL errors, like providing a non-existant college name; adding more comprehensive sports data (potentially through webscrapting); and more extensive query options to give more search functionality to the client users.
