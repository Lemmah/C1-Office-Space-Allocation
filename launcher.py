"""

This commandline interface uses docopt with the built in cmd module.

Usage:
    mra add_person <first_name> <last_name> <person_type> [<wants_accomodation>]
    mra create_room <room_type> <room_name>...
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

dojo_instance = Dojo()


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
    print('\n' + '*' * 32 + '[ WELCOME! ]' + '*' * 34 + '\n')
    print('\n' + '~' * 30 + '{ ANDELA KENYA }' + '~' * 32 + '\n')
    print('-' * 26 + '< MyRoomAllocator: Dojo >' + '-' * 27 + '\n')
    print('\n' + '*' * 78 + '\n')

    prompt = 'mra >>> '
    file = None

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accomodation>]"""
        first_name = args['<first_name>']
        last_name = args['<last_name>']
        person_type = args['<person_type>']
        wants_accomodation = args['<wants_accomodation>']

        if person_type.upper() in ['FELLOW', 'STAFF']:
            if wants_accomodation and person_type.upper() == 'FELLOW':
                print('\n' + '*' * 34 + '[ Success ]' + '*' * 35 + '\n')
                fellow_with_living = dojo_instance.add_person(
                    first_name, last_name, person_type, wants_accomodation)
                print('\t' + fellow_with_living[0])
                print('\t' + fellow_with_living[1])
                incase_allocated = fellow_with_living[2]
                if incase_allocated != 0:
                    print('\t' + incase_allocated)
                else:
                    pass
            elif wants_accomodation and person_type.upper() == 'STAFF':
                print('\n' + '*' * 35 + '[ ERROR! ]' + '*' * 35 + '\n')
                print(
                    '\tOOPSIE! Accomodation is available to Fellows only.')
            else:
                print('\n' + '*' * 34 + '[ Success ]' + '*' * 35 + '\n')
                staff_details = dojo_instance.add_person(
                    first_name, last_name, person_type)
                print('\t' + staff_details[0])
                if staff_details[1] != 0:
                    print('\t' + staff_details[1])
                else:
                    pass

        else:
            print('\n' + '*' * 35 + '[ ERROR! ]' + '*' * 35 + '\n')
            print(
                '\tAt the moment, we\'re working with either staff or fellows.\nPlease input a valid person_type.')
        print('\n' + '*' * 80 + '\n')

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""

        room_type = args['<room_type>']
        if room_type.upper() == 'LIVINGSPACE' or room_type.upper() == 'OFFICE':
            print('\n' + '*' * 34 + '[ Success ]' + '*' * 35 + '\n')
            for item in args['<room_name>']:
                room_name = item
                room_created = dojo_instance.create_room(
                    room_name, room_type)
                print('\t' + room_created)
        else:
            print('\n' + '*' * 35 + '[ ERROR! ]' + '*' * 35 + '\n')
            print('\t<room_type> type must either be Office or LivingSpace')

        print('\n' + '*' * 80 + '\n')

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('\n\tHope I made your work easier. Bye!\n')
        exit()


opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
