from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
if __name__ == '__main__':
    print(datetime.now().date())
    get_employees()
    calculate_salary()