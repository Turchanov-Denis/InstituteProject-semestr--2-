// Turchanov Denis 4PM
// или на плюсах
#include <iostream>
#include <vector>
#include <algorithm>

enum class Gender { Male, Female };

class User {
public:
    int mId;
    std::string mName;
    std::string mEmail;
    std::string mPhone;
    std::string mCity;
    Gender mGender;

    // Геттеры и сеттеры

    int getId() const {
        return mId;
    }

    std::string getName() const {
        return mName;
    }

    std::string getEmail() const {
        return mEmail;
    }

    std::string getPhone() const {
        return mPhone;
    }

    std::string getCity() const {
        return mCity;
    }

    Gender getGender() const {
        return mGender;
    }

    void setId(int id) {
        mId = id;
    }

    void setName(const std::string& name) {
        mName = name;
    }

    void setEmail(const std::string& email) {
        mEmail = email;
    }

    void setPhone(const std::string& phone) {
        mPhone = phone;
    }

    void setCity(const std::string& city) {
        mCity = city;
    }

    void setGender(Gender gender) {
        mGender = gender;
    }
};

class IRepository {
public:
    virtual void add(User* item) = 0;
    virtual void update(User* item) = 0;
    virtual void remove(User* item) = 0;
    virtual std::vector<User> get(const std::string& where, const std::string& orderBy) = 0;
};

class IUserRepository : public IRepository {
public:
    virtual User getById(int id) = 0;
    virtual User getByName(const std::string& name) = 0;
    virtual User getByEmail(const std::string& email) = 0;
    virtual std::vector<User> getByCity(const std::string& city) = 0;
    virtual std::vector<User> getByGender(Gender gender) = 0;
};

class MemoryRepository : public IRepository {
protected:
    std::vector<User*> items;

public:
    virtual void add(User* item) override {
        items.push_back(item);
    }

    virtual void update(User* item) override {
        // Реализация обновления объекта
        // Найдем пользователя по ID и обновим его данные
        auto it = std::find_if(items.begin(), items.end(), [item](const User* u) {
            return u->getId() == item->getId();
        });

        if (it != items.end()) {
            // Обновим данные
            (*it)->setName(item->getName());
            (*it)->setEmail(item->getEmail());
            (*it)->setPhone(item->getPhone());
            (*it)->setCity(item->getCity());
            (*it)->setGender(item->getGender());
        }
    }

    virtual void remove(User* item) override {
        items.erase(std::remove(items.begin(), items.end(), item), items.end());
        delete item;
    }

    virtual std::vector<User> get(const std::string& where, const std::string& orderBy) override {
        // Реализация получения объектов с учетом условия и сортировки
        std::vector<User> result;
        for (auto item : items) {
            result.push_back(*item);
        }
        return result;
    }
};

class MemoryUserRepository : public MemoryRepository, public IUserRepository {
public:
    virtual User getById(int id) override {
        for (auto user : items) {
            if (user->getId() == id) {
                return *user;
            }
        }
        return User{};
    }

    virtual User getByName(const std::string& name) override {
        for (auto user : items) {
            if (user->getName() == name) {
                return *user;
            }
        }
        return User{};
    }

    virtual User getByEmail(const std::string& email) override {
        for (auto user : items) {
            if (user->getEmail() == email) {
                return *user;
            }
        }
        return User{};
    }

    virtual std::vector<User> getByCity(const std::string& city) override {
        std::vector<User> result;
        for (auto user : items) {
            if (user->getCity() == city) {
                result.push_back(*user);
            }
        }
        return result;
    }

    virtual std::vector<User> getByGender(Gender gender) override {
        std::vector<User> result;
        for (auto user : items) {
            if (user->getGender() == gender) {
                result.push_back(*user);
            }
        }
        return result;
    }
};

int main() {
    MemoryUserRepository userRepository;

    // Добавление пользователя
    User* newUser = new User{1, "John Doe", "john@example.com", "123-456-7890", "City", Gender::Male};
    userRepository.add(newUser);

    // Изменение пользователя
    User updatedUser{1, "John Doe Updated", "john@example.com", "123-456-7890", "City", Gender::Male};
    userRepository.update(&updatedUser);

    // Удаление пользователя
    userRepository.remove(&updatedUser);

    // Получение пользователей по различным условиям
    std::vector<User> usersInCity = userRepository.getByCity("City");
    std::vector<User> femaleUsers = userRepository.getByGender(Gender::Female);

    return 0;
}
