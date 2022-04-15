from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file_data = open(file_name, 'r').readlines()
        for line in file_data:
            line = line.strip()
            line = line.split(', ')
            person = SalesPerson(eval(line[0]), line[1])
            sales = list(line[2].split(' '))
            for amount in sales:
                person.enter_sale(eval(amount))
            self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            individual = []
            individual.append(SalesPerson.get_id(person))
            individual.append(SalesPerson.get_name(person))
            individual.append(SalesPerson.total_sales(person))
            individual.append(SalesPerson.met_quota(person, quota))
            report.append(individual)
        return report

    def top_seller(self):
        seller = []
        top = 0
        for person in self.sales_people:
            current = person.total_sales()
            if current > top:
                top = current
                seller.clear()
                seller.append(person)
            elif current == top:
                seller.append(person)
        return seller

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if employee_id == SalesPerson.get_id(person):
                return person
        return None

    def get_sale_frequencies(self):
        frequencies = {}
        sales = []
        for person in self.sales_people:
            sale = person.total_sales()
            sales.append(sale)
            for amount in sales:
                frequencies[amount] = frequencies.get(amount, 0) + 1
        return frequencies
