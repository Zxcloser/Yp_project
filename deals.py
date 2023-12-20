class Deal:
    def __init__(self, id, description, deadline, responsible, department_id):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.responsible = responsible
        self.department_id = department_id

    def get_inf(self):
        return tuple(self.__dict__.values())

    def to_file(self):
        with open('Deals.txt', 'a', encoding="utf-8") as file:
            file.write(f'\n{self.id};{self.description};{self.deadline};{self.responsible};{self.department_id}')

