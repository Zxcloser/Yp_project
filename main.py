from deals import Deal
from slaves import Slave
from deps import Departament


f_s = open("Slaves.txt", 'r', encoding="utf-8")  # Открытие файла "Slaves.txt" для чтения
f_d = open("Department.txt", 'r', encoding="utf-8")  # Открытие файла "Department.txt" для чтения
lst = list()  # Создание пустого списка
lst_dep = list()  # Создание пустого списка

# Чтение данных из файла "Slaves.txt" и создание списка объектов класса Slave
for line in f_s:
    id, fio, age, speciality, salary, email, phone_num = line.split(';')
    lst.append(Slave(id, fio, age, speciality, salary, email, phone_num))

# Чтение данных из файла "Department.txt" и создание списка объектов класса Departament
for line in f_d:
    id, name, id_slave, head = line.split(';')
    lst_dep.append(Departament(id, name, id_slave, head))

lst_deals = list()
f_deals = open("Deals.txt", 'r', encoding="utf-8")
for line in f_deals:
    id, description, deadline, responsible, department_id = line.split(';')
    lst_deals.append(Deal(id, description, deadline, responsible, department_id))
f_deals.close()

f_s.close()  # Закрытие файла "Slaves.txt"
f_d.close()  # Закрытие файла "Department.txt"

# Бесконечный цикл для вывода меню и выполнения операций
while True:
    print(
        "1: Ввести сотрудника в учёт\n2: Добавить Отдел\n3: Просмотреть всех сотрудников\n4: Просмотреть все отделы\n5: Добавить сотрудника в отдел\n6: Добавить дело\n7: Просмотреть все дела\n0:Закрыть программу")
    c = input()

    if c == '1':
        # Ввод информации о сотруднике и добавление его в список lst, после чего запись в файл
        id, fio, age, speciality, salary, email, phone_num = input().split(' ')
        lst.append(Slave(id, fio, age, speciality, salary, email, phone_num))
        lst[-1].to_file()

    elif c == '2':
        # Ввод информации об отделе и добавление его в список lst_dep, после чего запись в файл
        id, name, id_slave, head = input().split(' ')
        lst_dep.append(Departament(id, name, id_slave, head))
        lst_dep[-1].to_file()

    elif c == '3':
        # Просмотр всех сотрудников
        for item in lst:
            print(item.get_inf())

    elif c == '4':
        # Просмотр всех отделов
        for item in lst_dep:
            print(item.get_inf())

    elif c == '5':
        # Добавление сотрудника в отдел
        print('Id отдела:')
        n = input()
        print('Id сотрудника:')
        i = input()
        f = open("Department", 'w')
        f.write('')
        f.close()
        with open('Department.txt', 'w', encoding="utf-8") as file:
            file.write('')
        for item in lst_dep:
            if item.id == n:
                item.id_slave += ', ' + i
            item.re_file()
    elif c == '6':  # Добавление дела
        id, description, deadline, responsible, department_id = input().split(' ')
        new_deal = Deal(id, description, deadline, responsible, department_id)
        lst_deals.append(new_deal)
        new_deal.to_file()
    elif c== '7':
        for item in lst_deals:
            print(item.get_inf())
    elif c == '0':
        # Закрытие программы (выход из бесконечного цикла)
        break
    else:
        # В случае выбора функции, отсутствующей в меню
        print('Данная функция отсутствует')