"""

This commandline interface uses docopt with the built in cmd module.

Usage:
    mra add_person <first_name> <last_name> <person_type> [<wants_accomodation>]
    mra create_room <room_type> <room_name>
    mra (-i | --interactive)
    mra (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from scripts.class_dojo import Dojo
from scripts.class_fellow import Fellow
from scripts.class_living_space import LivingSpace
from scripts.class_person import Person
from scripts.class_room import Room
from scripts.class_staff import Staff


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid command usage!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):

    prompt = 'mra >>> '
    file = None

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accomodation>]"""
        first_name = args['<first_name>']
        last_name = args['<last_name>']
        person_type = args['<person_type>']
        wants_accomodation = args['<wants_accomodation>']

        if person_type.upper() == 'FELLOW' or person_type.upper() == 'STAFF':
            print('\n' + '*' * 25 + ' Success ' + '*' * 26)
            print(Person(person_type, first_name, last_name).new_person())
            print(Person(person_type, first_name, last_name).allocate_office())
        else:
            print('\n' + '*' * 26 + ' ERROR! ' + '*' * 26)
            print(
                'At the moment, we\'re working with either staff or fellows.\nPlease input a valid person_type.')
        if wants_accomodation and person_type.upper() == 'FELLOW':
            print(Fellow(
                first_name, last_name,
                person_type, wants_accomodation).allocate_living_space())
        elif wants_accomodation and person_type.upper() == 'STAFF':
            print('\n' + '*' * 26 + ' ERROR! ' + '*' * 26)
            print(
                'OOPSIE! Accomodation is available to Fellows only.')
        print('*' * 60)

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = args['<room_type>']
        print('\n' + '*' * 25 + ' Success ' + '*' * 26)
        for item in args['<room_name>']:
            room_name = item
            if room_type.upper() == 'LIVINGSPACE' or room_type.upper() == 'OFFICE':
                print(Room(room_type, room_name).add_new_room()[0])
            else:
                print('\n' + '*' * 26 + ' ERROR! ' + '*' * 26)
                print('<room_type> type must either be Office or LivingSpace')

        print('\n' + '*' * 60)

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('\n\tHope I made your work easier. Bye!\n')
        exit()


opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
