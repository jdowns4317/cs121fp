"""
Thorsen Kristufek and James Downs
tkristuf@caltech.edu, jdowns@caltech.edu
-- Our application will have information about colleges and universities
-- so that prospective college students can easily find institutions that meet
-- their desired criteria. Colleges will also be able to interact with the
-- database to keep their information updated.

This file specifies the admin user interface.
"""
import sys  # to print error messages to sys.stderr
import mysql.connector
# To get error codes from the connector, useful for user-friendly
# error-handling
import mysql.connector.errorcode as errorcode

# Debugging flag to print errors when debugging that shouldn't be visible
# to an actual client. ***Set to False when done testing.***
DEBUG = False

# ----------------------------------------------------------------------
# SQL Utility Functions
# ----------------------------------------------------------------------
def get_conn():
    """"
    Returns a connected MySQL connector instance, if connection is successful.
    If unsuccessful, exits.
    """
    try:
        conn = mysql.connector.connect(
          host='localhost',
          user='eduadmin',
          # Find port in MAMP or MySQL Workbench GUI or with
          # SHOW VARIABLES WHERE variable_name LIKE 'port';
          port='3306',  # this may change!
          password='adminpw',
          database='finaldb' # replace this with your database name
        )
        print('Successfully connected.')
        return conn
    except mysql.connector.Error as err:
        # Remember that this is specific to _database_ users, not
        # application users. So is probably irrelevant to a client in your
        # simulated program. Their user information would be in a users table
        # specific to your database; hence the DEBUG use.
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR and DEBUG:
            sys.stderr('Incorrect username or password when connecting to DB.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR and DEBUG:
            sys.stderr('Database does not exist.')
        elif DEBUG:
            sys.stderr(err)
        else:
            # A fine catchall client-facing message.
            sys.stderr('An error occurred, please contact the administrator.')
        sys.exit(1)


# ----------------------------------------------------------------------
# Command-Line Functionality
# ----------------------------------------------------------------------

def show_admin_options():
    """
    Displays options specific for admins, such as adding new data <x>,
    modifying <x> based on a given id, removing <x>, etc.
    """
    while True:
        print('What would you like to do? ')
        print('  (p) - Add/Update College Mission')
        print('  (e) - Update All Information')
        print('  (a) - Update Admission Rate')
        print('  (q) - quit')
        print()
        ans = input('Enter an option: ').lower()
        if ans == 'q':
            quit_ui()
        elif ans == 'p':
            update_college_mission()
        elif ans == 'e':
            update_all_info()
        elif ans == 'a':
            update_admission_rate()

def update_college_mission():
    """
    Update College Mission Statements
    """
    u_id = input("Please give the u_id of your college: ")
    while True:
        mission = input("Please give the mission of your colllege (< 500 characters): ")
        if len(mission) < 500:
            break
    
    sql = """
UPDATE basic_college_info
SET mission = '%s'
WHERE u_id = '%s'
""" % (mission, u_id)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(f"Updated the mission for {u_id}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def update_all_info():
    u_id = input("College u_id: ")
    ug_pop = input("Undergraduate population: ")
    hbcu = input("HBCU flag: ")
    men_only = input("Men only flag: ")
    women_only = input("Women only flag: ")
    highest_deg = input("Highest degree offered code: ")
    admission_rate = input("Admission rate: ")
    sql = """
CALL update_all_info('%s', '%s', '%s', '%s', '%s', '%s', '%s')
""" % (u_id, ug_pop, hbcu, men_only, women_only, highest_deg, admission_rate)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Updated all of the information for your college")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def update_admission_rate():
    u_id = input("Please give the u_id of your college: ")
    while True:
        ar = input('Please enter a lower bound on the Acceptance Rate (between 0 and 1): ')
        try:
            lower_bound = float(ar)
            break
        except ValueError:
            print("Invalid input, please enter a decimal between 0 and 1")
    sql = """
UPDATE basic_college_info
SET admission_rate = '%s'
WHERE u_id = '%s'
""" % (ar, u_id)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(f"Updated the admission rate for {u_id}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')


def quit_ui():
    """
    Quits the program, printing a good bye message to the user.
    """
    print('Good bye!')
    exit()


def main():
    """
    Main function for starting things up.
    """
    show_admin_options()


if __name__ == '__main__':
    # This conn is a global object that other functions can access.
    # You'll need to use cursor = conn.cursor() each time you are
    # about to execute a query with cursor.execute(<sqlquery>)
    conn = get_conn()
    main()
