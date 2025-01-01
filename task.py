from collections import UserDict
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value        

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if value:
            super().__init__(value)
        else:
            print("Name is compulsory")
    

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        digits = re.findall(r"\d", value)        
        if len(value) == 10 and len(digits) == 10:
            super().__init__(value)            
        else:
            raise print("Phone number must have 10 digits")       

class Birthday(Field):
    def __init__(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(birthday_date)
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    def __str__(self):        
        return datetime.strftime(self.value, "%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday=Birthday(birthday)

    def remove_phone(self, phone):                
        phone_found = False
        for phone_num in self.phones:            
            if phone_num.value == phone:                
                self.phones.remove(phone_num)
                phone_found = True        

        if not phone_found:
            print(f"Phone number {phone} does not exist")

    def edit_phone(self, phone, new_phone):                
        phone_found = False
        for phone_num in self.phones:            
            if phone_num.value == phone:                
                self.phones.remove(phone_num)
                self.phones.append(Phone(new_phone))
                phone_found = True            

        if not phone_found:
            print('Such phone number does not exist')     

    def __str__(self):        
        return f"Contact name: {self.name.value}, Birthday: {self.birthday}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):    
        self.data = {}
    
    def add_record(self, record):        
        self.data[record.name.value] = record        
    def find(self, name):                
        return(self.data[name])
    def delete(self, name):
        self.data.pop(name)

    def __str__(self):        
        rec='Your address book:\n'
        for name, record in self.items():
            rec = rec + str(record) + '; \n'
        return rec
    
    def get_upcoming_birthdays(users):
        current_date = datetime.today().date()
        # current_date = datetime(year=2024, month=12, day=30).date()    
        congratulation_dates = []
        for user in users:
            user_birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            user_birthday_this_year = datetime(year=current_date.year, month=user_birthday.month, day=user_birthday.day)
            user_birthday_this_year = user_birthday_this_year.date()
            if (current_date.month == 12 and user_birthday_this_year.month == 1):            
                if (current_date.year % 4 == 0):
                    diff_dates = user_birthday_this_year - current_date + timedelta(days = 366)
                else: 
                    diff_dates = user_birthday_this_year - current_date + timedelta(days = 365)
            else:
                diff_dates = user_birthday_this_year - current_date
            diff_dates = diff_dates.days        
            if (diff_dates >= 0) and (diff_dates <= 7):            
                congratulation_date = user_birthday_this_year
                if(user_birthday_this_year.weekday() == 5):
                    congratulation_date = user_birthday_this_year + timedelta(days = 2)
                elif(user_birthday_this_year.weekday() == 6):
                    congratulation_date = user_birthday_this_year + timedelta(days = 1)                                        
                congratulation_date = congratulation_date.strftime("%Y.%m.%d")
                congratulation_dates.append({"name": user["name"], "congratulation_date":congratulation_date})        
        return(congratulation_dates)

# birthday = Birthday('2.21.1973')
# print(birthday)
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
# john_record.add_birthday("12.01.1987")
john_record.add_phone("5555555555")
book.add_record(john_record)
# jane_record = Record("Jane")
# jane_record.add_phone("9879547210")
# book.add_record(jane_record)
# jan_record = Record("Jan")
# jan_record.add_phone("9876543219")
# book.add_record(jan_record)
john = book.find("John")
print(john)
# john.edit_phone("1234567890", "1112223333")
# john.add_phone("5555555585")
# john.remove_phone("5555555555")
# print(john)
# print(book)
# book.delete("Jane")
# print(book)