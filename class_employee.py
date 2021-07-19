import sys
import re
from datetime import datetime

class Employee:
    def __init__(self, first_name, last_name, join_date, gender, salary = None,
        phone_number = None, leave_date = None):
        self.first_name = first_name
        self.last_name = last_name
        self._join_date = join_date
        self._gender = gender
        self._salary = salary
        self._phone_number = phone_number
        self._leave_date = leave_date


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split(' ')
        if len(values) != 2:
            raise ValueError('Not allowed value.')

        self.first_name, self.last_name = values

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}> ' \
               f'join date - {self._join_date}, leave date-{self._leave_date} ' \
               f'gender - {self._gender}, salary - {self._salary} ' \
               f'phone number - {self._phone_number} '
    @property
    def gender(self):
        return self._gender

    @property
    def emp_salary(self):
        return self._salary

    @emp_salary.setter
    def emp_salary(self,new_salary):
        self._salary = new_salary

    def __add__(self, value):
        return Employee(self._salary + value)

    @property
    def work_email(self):
        f_name = self.first_name.lower()
        l_name = self.last_name.lower()
        return f'{f_name}.{l_name}@company.com'

    @work_email.setter
    def work_email(self, names):
        email_name = names.split(' ')
        if len(email_name) != 2:
            raise ValueError('Not allowed value.')

        self.first_name, self.last_name = email_name


    @property
    def emp_phone_number(self):
        return self._phone_number

    @emp_phone_number.setter
    def emp_phone_number(self, new_phone):
        phone = str(new_phone)
        expression = (r'0?(77|55|99|91|98)[ -]?'
        '('
            r'(\d{3}[ -]?\d{3})|'  
            r'(\d{2} \d{2} \d{2})|' 
            r'(\d{2}-\d{2}-\d{2})'  
        ')')
        if re.fullmatch(expression, phone):
            self._phone_number = new_phone
        else:
            ValueError('Not allowed value.')


    @property
    def experience(self):

        date_object_join = datetime.strptime(self._join_date, '%m/%d/%Y' )

        if self._leave_date:
            date = datetime.strptime(self._leave_date, '%m/%d/%Y')
        else:
            date = datetime.now()

        year = date.year - date_object_join.year
        month = date.month - date_object_join.month
        day = date.day - date_object_join.day

        return f'{year}-year {month}-month {day}-day'

    @property
    def trial_passed(self):
        if self._leave_date:
            return False
        return True

emp1 = Employee('Lilit', 'Nahapetyan','09/01/2020', 'F', 200, '077123456', '11/30/2025' )
print(emp1)
print(emp1.experience)
print(emp1.work_email)
print(emp1.trial_passed)
