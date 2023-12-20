class Departament:
    def __init__(self, id, name, id_slave, head):
        # Инициализация атрибутов объекта класса Departament
        self.id = id
        self.name = name
        self.id_slave = id_slave
        self.head = head

    def get_inf(self):
        # Метод возвращает кортеж значений атрибутов объекта
        return tuple(self.__dict__.values())

    def to_file(self):
        # Метод записывает атрибуты объекта в файл "Department.txt"
        with open('Department.txt', 'a', encoding="utf-8") as file:
            file.write(f'\n{self.id};{self.name};{self.id_slave};{self.head}')

    def re_file(self):
        # Метод обновляет информацию в файле "Department.txt"
        with open('Department.txt', 'a', encoding="utf-8") as file:
            file.write(f'{self.id};{self.name};{self.id_slave};{self.head}')