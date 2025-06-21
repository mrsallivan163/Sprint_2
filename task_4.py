class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours == 0 or hours is None:
            hours = (7 - rest_days) * 8 
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if not email or email=='':
            email = f"{name.lower().replace(' ','_')}@email.com"
            return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment