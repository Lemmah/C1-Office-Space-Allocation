# Office Space Allocator
### Intro
Office Room Allocator is an app that is designed to allocate rooms at one of Andela's facilities called the Dojo. When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. This console application digitizes and randomizes a room allocation system for one of Andela Kenya’s facilities called The Dojo.

### System requirements
- Python version 3.5 + 
- Python virtialenv

### Setup
- `git clone https://github.com/Lemmah/C1-Office-Space-Allocation.git`
- Create a virtualenv and activate it.
- In your terminal (I use ubuntu, and I don't really know how this will behave on other os), `cd` into C1-Office-Space-Allocation and run `pip install -r requirements.txt`
- To start the app's interactive shell run `python launcher.py -i`

### Usage
- `quit` : this will close the app's interactive shell
- `create_room <room_type> <room_name>` : Creates a new room
- `add_person <first_name> <last_name> <person_type> [<wants_accomodation>]` : Adds a new person and allocates them a random room.
- `print_room <room_name>`: Prints all the members of the specified room.
- `reallocate_person <name> <new_room>`: Moves a person from one room to another.
- `load_people <filename>`: Does batch addition of people using data from a `filename.txt`
- `print_allocations [<filename>]`: Prints all rooms and the people in them and optionally writes the data to `filename.txt`.
- `print_unallocated [<filename>]`: Prints all the people that haven't been allocated and optionally writes the data to `filename.txt`.
- `load_state [<filename>]`: Loads data from the SQLite db into the app
- `save_state [<db_name>]`: Saves data stored in the app to a SQLite DB
- `(-i | --interactive)`
- 	`-h --help Show this screen.`:  Shows help text
-	`-i --interactive Interactive mode.` Starts the app in interactive mode

### Tests
To run tests, run `pytest` inside the project folder.

### Contributing
This app is open-source. I do not have any exclusive rights to it. 