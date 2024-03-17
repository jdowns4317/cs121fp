The data for our application comes from the following links: https://collegescorecard.ed.gov/data/  https://nces.ed.gov/ipeds/datacenter/datafiles.aspx?sid=e17cda03-f05c-41db-898a-687ee2694b6f&rtid=1 https://www.ncaa.org/sports/2016/12/14/shared-ncaa-research-data.aspx      https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-cities-and-towns.html

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

Use the source queries.sql to load data and python3 app-client.py or app-admin.py commands to access the application.

There are no unfinished features, but definitely room to include more in the future!
