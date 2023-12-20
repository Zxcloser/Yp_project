class Slave:
    def __init__(self, id, fio, age, specialty, salary, email, phone_num):
        # Инициализация атрибутов объекта класса Slave
        self.id = id
        self.fio = fio
        self.age = age
        self.specialty = specialty
        self.salary = salary
        self.email = email
        self.phone_num = phone_num

    def get_inf(self):
        # Метод возвращает кортеж значений атрибутов объекта
        return tuple(self.__dict__.values())

    def to_file(self):
        # Метод записывает атрибуты объекта в файл "Slaves.txt"
        with open('Slaves.txt', 'a', encoding="utf-8") as file:
            file.write(
                f'\n{self.id};{self.fio};{self.age};{self.specialty};{self.salary};{self.email};{self.phone_num}')