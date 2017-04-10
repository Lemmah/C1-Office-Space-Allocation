"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    note add_note <note>
    note (-i | --interactive)
    note (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from scripts.class_dojo import *
from scripts.class_fellow import *
from scripts.class_living_space import *
from scripts.class_person import *
from scripts.class_room import *
from scripts.class_staff import *


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

            print('Invalid Command!')
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

    prompt = '>>> '
    file = None

    @docopt_cmd
    def do_add_note(self, args):
        """Usage: add_note <note>"""

        print(noteTaking().take_note(args))

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Hope I made your work easier. Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
