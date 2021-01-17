import mysql.connector
sqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chalbe@123",
    database="tables",
    auth_plugin="mysql_native_password"
)
cursorr = sqldb.cursor()

class DbHelper:
    def get_maximum_salary(self):
        cursorr.execute("select max(Salary)from employees")
        result = cursorr.fetchone()
        return result

    def get_minimum_salary(self):
        cursorr.execute("select min(Salary)from employees")
        result = cursorr.fetchone()
        return result

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)