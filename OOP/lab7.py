# Turchanov Denis 4PM
"""Задание паттерн Repository
1. Создать шаблонный интерфейс IRepository<T>:
void Add(T* item)
• void Update(T" item)
void Delete(T* item)
std::vector<T> Get(const std::string& where, const std::string& orderBy)
2. Создать класс User.
• int mld;
⚫ std::string mName
• std::string mEmail
• std::string mPhone
• std::string mCity
• Gender (Male, Female) mGender Добавить геттеры и сеттеры
3. Создать интерфейс UserRepository: public IRepository<User>:
•T getById(int id);
• T getByname(const std::string& name)
T getByEmail(const std::string& email)
• std::vector<T> getByCity (const std::string& city)
• std::vector<T> getByGender(Gender gender)
4. Создать класс Memory Repository<T>: public IRepository<Т», который реализует работу с объектами в оперативной памяти
5. Создать класс Memory UserRepository: public MemoryRepository<T>, public IUserRepository который реализует работу с объектами User в оперативной памяти
6. Продемонстрировать работу приложения при помощи добавления. изменения, удаления и получения объектов User из репозитория Memory UserRepository"""

from enum import Enum

class Gender(Enum):
    Male = "Male"
    Female = "Female"

class User:
    def __init__(self, user_id, name, email, phone, city, gender):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.gender = gender

class IRepository:
    def add(self, item):
        pass

    def update(self, item):
        pass

    def remove(self, item):
        pass

    def get(self, where, order_by):
        pass

class IUserRepository(IRepository):
    def get_by_id(self, user_id):
        pass

    def get_by_name(self, name):
        pass

    def get_by_email(self, email):
        pass

    def get_by_city(self, city):
        pass

    def get_by_gender(self, gender):
        pass

class MemoryRepository(IRepository):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"Added: {item.__dict__}")

    def update(self, item):
        for i, existing_item in enumerate(self.items):
            if existing_item.user_id == item.user_id:
                self.items[i] = item
                print(f"Updated: {item.__dict__}")
                break

    def remove(self, item):
        self.items.remove(item)
        print(f"Removed: {item.__dict__}")

    def get(self, where, order_by):
        return self.items

class MemoryUserRepository(MemoryRepository, IUserRepository):
    def get(self):
        users = []
        for user in self.items:
            users.append(user)
        return users

    def get_by_id(self, user_id):
        for user in self.items:
            if user.user_id == user_id:
                return user
        return None

    def get_by_name(self, name):
        for user in self.items:
            if user.name == name:
                return user
        return None

    def get_by_email(self, email):
        for user in self.items:
            if user.email == email:
                return user
        return None

    def get_by_city(self, city):
        return [user for user in self.items if user.city == city]

    def get_by_gender(self, gender):
        return [user for user in self.items if user.gender == gender]

# Пример использования
user_repository = MemoryUserRepository()

# Добавление пользователя
new_user = User(1, "John Doe", "john@example.com", "123-456-7890", "City", Gender.Male)
user_repository.add(new_user)

new_user1 = User(2, "John Doe1", "john@example.com1", "123-456-7890", "City", Gender.Male)
user_repository.add(new_user1)
# Изменение пользователя
updated_user = User(1, "John Doe Updated", "john@example.com", "123-456-7890", "City", Gender.Male)
user_repository.update(updated_user)

# Удаление пользователя
user_repository.remove(updated_user)

# Получение пользователей по различным условиям
users_in_city = user_repository.get_by_city("City")
print(f"Users in City: {users_in_city}")

female_users = user_repository.get_by_gender(Gender.Female)
print(f"Female Users: {female_users}")
