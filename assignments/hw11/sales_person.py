class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if quota <= self.total_sales():
            return True
        else:
            return False

    def compare_to(self, other):
        first_person = self.total_sales()
        second_person = other.total_sales()
        if first_person > second_person:
            return 1
        elif first_person < second_person:
            return -1
        elif first_person == second_person:
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
