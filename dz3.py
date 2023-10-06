# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

from csv import DictReader, DictWriter
from os.path import exists

def create_file():
    if not exists('Phone.csv'):
        with open('Phone.csv', "w", encoding="utf-8", newline="") as data:
            f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_writer.writeheader()

def get_info():
    info = ['Иванов', 'Иван', '12-16-18']
    return info

def read_file(file_name):
    if exists(file_name):
        with open(file_name, encoding="utf-8") as data:
            f_reader = DictReader(data)
            res = list(f_reader)
        return res
    else:
        print("Файл не существует.")

def write_file(file_name, lst):
    if exists(file_name):
        with open(file_name, "a+", encoding="utf-8", newline="") as data:
            f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
            f_writer.writerow(obj)
    else:
        print("Файл не существует.")

def change_data(file_name, field_to_change, old_value, new_value):
    data = read_file(file_name)
    if data:
        updated = False
        for entry in data:
            if entry[field_to_change] == old_value:
                entry[field_to_change] = new_value
                updated = True
        if updated:
            with open(file_name, "w", encoding="utf-8", newline="") as data_file:
                fieldnames = ['Фамилия', 'Имя', 'Номер']
                f_writer = DictWriter(data_file, fieldnames=fieldnames)
                f_writer.writeheader()
                f_writer.writerows(data)
            print(f"Данные обновлены для {field_to_change} '{old_value}'")
        else:
            print(f"{field_to_change} '{old_value}' не найден в справочнике.")
    else:
        print("Файл не существует.")

def delete_data(file_name, field_to_delete, value_to_delete):
    data = read_file(file_name)
    if data:
        removed = False
        new_data = []
        for entry in data:
            if entry[field_to_delete] == value_to_delete:
                removed = True
            else:
                new_data.append(entry)
        if removed:
            with open(file_name, "w", encoding="utf-8", newline="") as data_file:
                fieldnames = ['Фамилия', 'Имя', 'Номер']
                f_writer = DictWriter(data_file, fieldnames=fieldnames)
                f_writer.writeheader()
                f_writer.writerows(new_data)
            print(f"Данные удалены для {field_to_delete} '{value_to_delete}'")
        else:
            print(f"{field_to_delete} '{value_to_delete}' не найден в справочнике.")
    else:
        print("Файл не существует.")

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "r":
            data = read_file('Phone.csv')
            if data:
                print(*data)
        elif command == "w":
            create_file()
            write_file('Phone.csv', get_info())
        elif command == "e":
            field_to_change = input("Введите поле для изменения (Фамилия, Имя, Номер): ")
            old_value = input("Введите старое значение: ")
            new_value = input("Введите новое значение: ")
            change_data('Phone.csv', field_to_change, old_value, new_value)
        elif command == "d":
            field_to_delete = input("Введите поле для удаления (Фамилия, Имя, Номер): ")
            value_to_delete = input("Введите значение для удаления: ")
            delete_data('Phone.csv', field_to_delete, value_to_delete)


main()
