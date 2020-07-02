# AirBnB Clone
![HBnB](./img/hbnb.png)

### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Acknowledgements](#Acknowledgements)

## Description
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Environment
The console was developed in Ubuntu 14.04LTS using python3(version 3.4.3).

### Further information
For further information on python version, and documentation visit[python.org](https: // www.python.org /) .

## Requirements
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 14.04, python3 and pep8 style corrector.

## Repo Contents
This repository constains the following files:

| **File** | **Description** |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py) | Defines subclass City |
|[place.py](./models/place.py) | Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[tests_base_model.py](./tests/tests_models/test_base_model.py) | unittests for base_model |
|[tests_user.py](./tests/test_models/tests_user.py) | unittests for user |
|[tests_amenity.py](./tests/test_models/tests_amenity.py) | unittests for amenity |
|[tests_city.py](./tests/test_models/tests_city.py) | unittests for city |
|[tests_place.py](./tests/test_models/tests_place.py) | unittests for place |
|[tests_review.py](./tests/test_models/tests_review.py) | unittests for review |
|[tests_state.py](./tests/test_models/tests_state.py) | unittests for state |
|[tests_file_storage.py](./tests/tests_models/tests_engine/tests_file_storage.py) | unittests for file_storage |
|[tests_console.py](./tests/tests_console.py) | unittests for console |

## Installation
Clone the repository and run the console.py
```
$ git clone https://github.com/21Insight/AirBnB_clone.git
```

## Usage

| **Method** | **Description** |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute(save the change into the JSON file) |
|[destroy](./console.py) | Deletes an instance based on the class name and id(save the change into the JSON file) |
|[count](./console.py) | Retrieve the number of instances of a class |
|[help](./console.py) | Prints information about specific command |
|[quit / EOF](./console.py) | Exit the program |

###### Example No.1
```
$ ./console.py
(hbnb) create User
61289a07-189d-491f-9712-537611d019e4
(hbnb) show User 61289a07-189d-491f-9712-537611d019e4
[User](61289a07-189d-491f-9712-537611d019e4) {'created_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981336), 'updated_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981525), 'id': '61289a07-189d-491f-9712-537611d019e4'}
(hbnb) all User
["[User] (61289a07-189d-491f-9712-537611d019e4) {'created_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981336), 'updated_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981525), 'id': '61289a07-189d-491f-9712-537611d019e4'}"]
(hbnb) update User 61289a07-189d-491f-9712-537611d019e4 name Andres
(hbnb) all User
["[User] (61289a07-189d-491f-9712-537611d019e4) {'name': 'Andres', 'created_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981336), 'updated_at': datetime.datetime(2020, 7, 2, 4, 6, 1, 981525), 'id': '61289a07-189d-491f-9712-537611d019e4'}"]
(hbnb) destroy User 61289a07-189d-491f-9712-537611d019e4
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb) EOF
```

###### Example No.2
```
$ ./console.py
(hbnb) User.create
** * Unknown syntax: User.create
(hbnb) User.create()
ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1
(hbnb) User.all()
["[User] (ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1) {'updated_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11539), 'id': 'ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1', 'created_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11414)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1)
[User](ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1) {'updated_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11539), 'id': 'ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1', 'created_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11414)}
(hbnb) User.update("ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1", "name", "Johanna")
(hbnb) User.all()
["[User] (ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1) {'updated_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11539), 'name': 'Johanna', 'created_at': datetime.datetime(2020, 7, 2, 3, 54, 18, 11414), 'id': 'ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1'}"]
(hbnb) User.destroy(ee226e2b-fc4a-4b16-a16f-3e3e358a4ee1)
(hbnb) User.all()
[]
(hbnb) quit
```

## Built with
python3(3.4.3)
### Version
HBnB - version 1.20

### Acknowledgements
To all the peers that contribuited with their knowledge

### Authors
* Jose Cuervo - @21Insight
* Victor Paz - @VMP1312
