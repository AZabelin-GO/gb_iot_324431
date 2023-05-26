#!/usr/bin/env python

# Task 38
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import os
import csv
import uuid
from copy import deepcopy
from dataclasses import dataclass, field


@dataclass
class Person:
    uuid: str = str(uuid.uuid4())
    name: str = ''
    surname: str = ''
    patronymic: str = ''
    phone: str = ''

    def updateName(self, name):
        if name != '' and name is not None:
            self.name = name

    def updateSurname(self, surname):
        if surname != '' and surname is not None:
            self.surname = surname

    def updatePatronymic(self, patronymic):
        if patronymic != '' and patronymic is not None:
            self.patronymic = patronymic

    def updatePhone(self, phone):
        if phone != '' and phone is not None:
            self.phone = phone

    def pprint(self):
        print(f'UUID: {self.uuid}')
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Patronymic: {self.patronymic}')
        print(f'Phone: {self.phone}')


@dataclass
class Database:
    phone_db_csv_file: str
    csv_headers: list = field(default_factory=list)
    data: list = field(default_factory=list)

    def __init__(self, phone_db_csv_file='phone_db.csv'):
        self.phone_db_csv_file = phone_db_csv_file
        self.data = list()
        if os.path.exists(self.phone_db_csv_file):
            with open(self.phone_db_csv_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                self.csv_headers = csv_reader.fieldnames
                for row in csv_reader:
                    self.data.append(
                        Person(
                            row['uuid'],
                            row['name'],
                            row['surname'],
                            row['patronymic'],
                            row['phone']
                        )
                    )
        else:
            with open(self.phone_db_csv_file, mode='w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, list(Person().__dict__.keys()))
                csv_writer.writeheader()
                self.csv_headers = csv_writer.fieldnames

    def save(self):
        with open(self.phone_db_csv_file, mode='w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, list(Person().__dict__.keys()))
            csv_writer.writeheader()
            for person in self.data:
                csv_writer.writerow(person.__dict__)

    def pprint(self):
        for person in self.data:
            person.pprint()
            print('---------')

    def addPerson(self, person: Person):
        if self.findPersonByUUID(person) is None:
            self.data.append(deepcopy(person))
            self.save()
        else:
            raise Exception(f'Person with uuid {person.uuid} already exists')

    def updatePerson(self, person: Person):
        p = self.findPersonByUUID(person)
        if p is not None:
            for item in self.data:
                if item.uuid == person.uuid:
                    item.updateName(person.name)
                    item.updateSurname(person.surname)
                    item.updatePatronymic(person.patronymic)
                    item.updatePhone(person.phone)

                    self.save()

                    break
        else:
            raise Exception(f'Person with uuid {person.uuid} not found')

    def deletePerson(self, person: Person):
        if person in self.data:
            self.data.remove(person)
            self.save()

    def findPersonByUUID(self, person: Person):
        for item in self.data:
            if item.uuid == person.uuid:
                return deepcopy(item)

        return None

    def findPersonsByName(self, person: Person):
        return [deepcopy(item) for item in self.data if item.name == person.name]

    def findPersonsBySurname(self, person: Person):
        return [deepcopy(item) for item in self.data if item.surname == person.surname]

    def findPersonsByPatronymic(self, person: Person):
        return [deepcopy(item) for item in self.data if item.patronymic == person.patronymic]

    def findPersonsByPhone(self, person: Person):
        return [deepcopy(item) for item in self.data if item.phone == person.phone]


DB = Database()


def printMainMenu():
    print()
    print('Main menu:')
    print('1 - List database')
    print('2 - Search person')
    print('3 - Add person')
    print('4 - Update person')
    print('5 - Delete person')
    print('0 - Exit')


def printSearchMenu():
    print()
    print('Search menu:')
    print('1 - Search person by UUID')
    print('2 - Search persons by Name')
    print('3 - Search persons by Surname')
    print('4 - Search persons by Patronymic')
    print('5 - Search persons by Phone')
    print('0 - Go back')


def commandSearchPersonByUUID():
    p_uuid = str(input(f'Enter a UUID:\t')).strip()
    res = DB.findPersonByUUID(
        Person(
            uuid=p_uuid
        )
    )
    if res is not None:
        print('Result:')
        res.pprint()
        print('---------')
    else:
        print(f'Person with UUID "{p_uuid}" not found')


def commandSearchPersonsByName():
    name = str(input(f'Enter a Name:\t')).strip()

    res = DB.findPersonsByName(
        Person(
            name=name
        )
    )

    if len(res) != 0:
        print('Result:')
        for item in res:
            item.pprint()
            print('---------')
    else:
        print(f'Person with Name "{name}" not found')


def commandSearchPersonsBySurname():
    surname = str(input(f'Enter a Surname:\t')).strip()

    res = DB.findPersonsBySurname(
        Person(
            surname=surname
        )
    )

    if len(res) != 0:
        print('Result:')
        for item in res:
            item.pprint()
            print('---------')
    else:
        print(f'Person with Surname "{surname}" not found')


def commandSearchPersonsByPatronymic():
    patronymic = str(input(f'Enter a Patronymic:\t')).strip()
    res = DB.findPersonsByPatronymic(
        Person(
            patronymic=patronymic
        )
    )

    if len(res) != 0:
        print('Result:')
        for item in res:
            item.pprint()
            print('---------')
    else:
        print(f'Person with Patronymic "{patronymic}" not found')


def commandSearchPersonsByPhone():
    phone = str(input(f'Enter a Phone:\t')).strip()

    res = DB.findPersonsByPhone(
        Person(
            phone=phone
        )
    )

    if len(res) != 0:
        print('Result:')
        for item in res:
            item.pprint()
            print('---------')
    else:
        print(f'Person with Phone "{phone}" not found')


def enterSearchPersonMenu():
    while True:
        printSearchMenu()

        choice = int(input(f'Enter a command:\t'))
        if choice == 1:
            commandSearchPersonByUUID()
        elif choice == 2:
            commandSearchPersonsByName()
        elif choice == 3:
            commandSearchPersonsBySurname()
        elif choice == 4:
            commandSearchPersonsByPatronymic()
        elif choice == 5:
            commandSearchPersonsByPhone()
        elif choice == 0:
            break


def commandAddNewPerson():
    name = str(input(f'Enter a Name:\t')).strip()
    surname = str(input(f'Enter a Surname:\t')).strip()
    patronymic = str(input(f'Enter a Patronymic:\t')).strip()
    phone = str(input(f'Enter a Phone:\t')).strip()

    try:
        DB.addPerson(
            Person(
                uuid=str(uuid.uuid4()),
                name=name,
                surname=surname,
                patronymic=patronymic,
                phone=phone
            )
        )
    except Exception as e:
        print(f'Failed to add new person: {e}')


def enterAddPersonMenu():
    commandAddNewPerson()


def commandUpdatePersonByUUID():
    p_uuid = str(input(f'Enter a UUID:\t')).strip()
    if len(p_uuid) == 0:
        print('UUID could not be empty')

        return

    name = str(input(f'Enter a new Name (leave empty if not needed to change):\t')).strip()
    surname = str(input(f'Enter a new Surname (leave empty if not needed to change):\t')).strip()
    patronymic = str(input(f'Enter a new Patronymic (leave empty if not needed to change):\t')).strip()
    phone = str(input(f'Enter a new Phone (leave empty if not needed to change):\t')).strip()

    try:
        DB.updatePerson(
            Person(
                uuid=p_uuid,
                name=name,
                surname=surname,
                patronymic=patronymic,
                phone=phone
            )
        )
        print('Person updated')
    except Exception as e:
        print(f'Failed to update person: {e}')


def enterUpdatePersonMenu():
    commandUpdatePersonByUUID()


def commandDeletePersonByUUID():
    p_uuid = str(input(f'Enter a UUID:\t')).strip()
    if len(p_uuid) == 0:
        print('UUID could not be empty')

        return

    res = DB.findPersonByUUID(
        Person(
            uuid=p_uuid
        )
    )

    if res is not None:
        DB.deletePerson(res)
        print('Person delete')
    else:
        print(f'Person with UUID "{p_uuid}" not found')


def enterDeletePersonMenu():
    commandDeletePersonByUUID()


def main():
    while True:
        printMainMenu()

        choice = int(input(f'Enter a command:\t'))

        if choice == 1:
            DB.pprint()
        elif choice == 2:
            enterSearchPersonMenu()
        elif choice == 3:
            enterAddPersonMenu()
        elif choice == 4:
            enterUpdatePersonMenu()
        elif choice == 5:
            enterDeletePersonMenu()
        elif choice == 0:
            break


if __name__ == '__main__':
    main()
