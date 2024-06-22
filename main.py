from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from collections import defaultdict

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# Создаем словарь для хранения контактов
contacts_dict = defaultdict(list)

# Обрабатываем каждый контакт в списке
for contact in contacts_list[1:]:
    # Разделяем имя на фамилию, имя и отчество
    name_parts = " ".join(contact[:3]).split(" ")
    lastname, firstname, surname = name_parts[:3] + [""] * (3 - len(name_parts))

    # Форматируем телефонный номер
    phone = contact[5]
    phone = re.sub(r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*\(?(\w+.\s\d+)\)?)?",
                   r"+7(\2)\3-\4-\5 \7", phone)

    # Добавляем контакт в словарь
    key = (lastname, firstname)
    contacts_dict[key].append([lastname, firstname, surname, contact[3], contact[4], phone, contact[6]])

# Объединяем дублирующиеся записи о человеке в одну
merged_contacts = []
for key, contacts in contacts_dict.items():
    merged_contact = contacts[0]
    for contact in contacts[1:]:
        merged_contact = [x or y for x, y in zip(merged_contact, contact)]
    merged_contacts.append(merged_contact)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows([contacts_list[0]] + merged_contacts)