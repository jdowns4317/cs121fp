"""
Thorsen Kristufek and James Downs
tkristuf@caltech.edu, jdowns@caltech.edu
-- Our application will have information about colleges and universities
-- so that prospective college students can easily find institutions that meet
-- their desired criteria. Colleges will also be able to interact with the
-- database to keep their information updated.

This file specified the client user interface.
"""
import sys  # to print error messages to sys.stderr
import mysql.connector
# To get error codes from the connector, useful for user-friendly
# error-handling
import mysql.connector.errorcode as errorcode

# Debugging flag to print errors when debugging that shouldn't be visible
# to an actual client. ***Set to False when done testing.***
DEBUG = False


sport_dict = {'MFB': "Men's Football", "MBB": "Men's Basketball", 
              "WBB": "Women's Basketball", "MBA": "Men's Baseball", 
              "MTR": "Men's Track and Field", "WTR": "Women's Track and Field"}

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
          user='educlient',
          # Find port in MAMP or MySQL Workbench GUI or with
          # SHOW VARIABLES WHERE variable_name LIKE 'port';
          port='3306',  # this may change!
          password='clientpw',
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
def show_options():
    """
    Displays options users can choose in the application, such as
    viewing <x>, filtering results with a flag (e.g. -s to sort),
    sending a request to do <x>, etc.
    """
    while True:
        print('What would you like to view? ')
        print('  (x) - Top 10 Colleges Ranked by Lowest Admission Rate')
        print("  (y) - Men's Only Colleges")
        print("  (z) - Women's Only Colleges")
        print('  (k) - Colleges with Sports programs in (input) Acceptance Rate:')
        print('  (j) - City Population Range (input):')
        print('  (i) - Detailed Sports Info by College (input)')
        print('  (q) - quit')
        print()
        ans = input('Enter an option: ').lower()
        if ans == 'q':
            quit_ui()
        elif ans == 'x':
            low_admission_rate_colleges()
        elif ans == 'y':
            mens_only_colleges()
        elif ans == 'z':
            womens_only_colleges()
        elif ans == 'k':  
            colleges_with_sports_in_acceptance()
        elif ans == 'j':
            colleges_within_pop()
        elif ans == 'i': 
            detailed_sports_info()

def low_admission_rate_colleges():
    """
    Outputs the 10 Colleges/Universities with
    Lowest Admission Rate
    """
    
    sql = """
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE admission_rate IS NOT NULL AND admission_rate <> 0
ORDER BY admission_rate
LIMIT 10;
"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's the Top 10 Colleges Ranked by Lowest Admission Rate")
        for row in rows:
            (cn, up, ar, c, s) = row
            print(f"College Name: {cn}, Undergrad Population: {up}, Admission Rate: {ar}, City: {c}, State: {s}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def mens_only_colleges():
    """
    Outputs Men's only colleges
    """
    sql = """
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE men_only = 1
ORDER BY college_name;
"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's all of the mens's only colleges")
        for row in rows:
            (cn, up, ar, c, s) = row
            print(f"College Name: {cn}, Undergrad Population: {up}, Admission Rate: {ar}, City: {c}, State: {s}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def womens_only_colleges():
    """
    Outputs women's only colleges
    """
    sql = """
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE women_only = 1
ORDER BY college_name;
"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's all of the women's only colleges")
        for row in rows:
            (cn, up, ar, c, s) = row
            print(f"College Name: {cn}, Undergrad Population: {up}, Admission Rate: {ar}, City: {c}, State: {s}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def colleges_with_sports_in_acceptance():
    """
    Colleges with Sports programs in a user
    input Acceptance Rate range
    """
    while True:
        lb = input('Please enter a lower bound on the Acceptance Rate (between 0 and 1): ')
        try:
            lower_bound = float(lb)
            if 0 <= lower_bound <= 1:
                break
            else:
                print("Invalid input, please enter a decimal between 0 and 1")
        except ValueError:
            print("Invalid input, please enter a decimal between 0 and 1")
    while True:
        ub = input('Please enter a upper bound on the Acceptance Rate (between the lower bound and 1): ')
        try:
            upper_bound = float(ub)
            if lower_bound <= upper_bound <= 1:
                break
            else:
                print("Invalid input, please enter a decimal between the lower bound and 1")
        except ValueError:
            print("Invalid input, please enter a decimal between the lower bound and 1")

    sql = """
SELECT college_name, ug_pop, admission_rate, city, state_abbr, count_sports(u_id)
FROM basic_college_info
WHERE count_sports(u_id) > 0 AND admission_rate BETWEEN '%s' AND '%s'
ORDER BY college_name;
""" % (lower_bound, upper_bound)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's the colleges with sports programs in your provided acceptance rate range")
        for row in rows:
            (cn, up, ar, c, s, ns) = row
            print(f"College Name: {cn}, Undergrad Population: {up}, Admission Rate: {ar}, City: {c}, State: {s}, Number of Sports: {ns}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')



def colleges_within_pop():
    while True:
        lb = input('Please enter a lower bound on the city population: ')
        try:
            lower_bound = int(lb)
            break
        except ValueError:
            print("Invalid input, please enter a decimal between 0 and 1")
    while True:
        ub = input('Please enter an upper bound on the city population: ')
        try:
            upper_bound = float(ub)
            break
        except ValueError:
            print("Invalid input, please enter a decimal between the lower bound and 1")

    sql = """
SELECT b.college_name, b.ug_pop, b.admission_rate, b.city, b.state_abbr, 
c.population
FROM basic_college_info b
JOIN city_pop c ON b.city = c.city AND b.state_abbr = c.state_abbr
WHERE c.population BETWEEN '%s' AND '%s'
ORDER BY c.population;
""" % (lower_bound, upper_bound)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's the colleges that exist in cities between your provided population range")
        for row in rows:
            (cn, up, ar, c, s, cp) = row
            print(f"College Name: {cn}, Undergrad Population: {up}, Admission Rate: {ar}, City: {c}, State: {s}, City Population: {cp}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')

def detailed_sports_info():
    """
    Outputs detailed sports info
    about a user input college
    """
    college_name = input("Please provide the name of a college: ")
    sql = """
SELECT sp.sport, sgr.fed_grad_rate
FROM sports_programs sp
JOIN basic_college_info bci ON sp.u_id = bci.u_id
JOIN sports_grad_rate sgr ON sp.sport = sgr.sport
WHERE bci.college_name = '%s';
""" % (college_name)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("Here's the colleges that exist in cities between your provided population range:")
        for row in rows:
            (sp, sgr) = row
            print(f"Sports Program: {sport_dict[sp]}, D1 Sport Federal Graduation Rate: {sgr}")
    except mysql.connector.Error as err:
        # If you're testing, it's helpful to see more details printed.
        if DEBUG:
            sys.stderr(err)
            sys.exit(1)
        else:
            sys.stderr('An SQL error occurred, please retry')
    pass

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
    show_options()


if __name__ == '__main__':
    # This conn is a global object that other functions can access.
    # You'll need to use cursor = conn.cursor() each time you are
    # about to execute a query with cursor.execute(<sqlquery>)
    conn = get_conn()
    main()
