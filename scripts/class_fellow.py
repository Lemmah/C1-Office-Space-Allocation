from scripts.class_person import Person
'''

This fellow class inherits from Person.
Simple, it only enables fellows get living spaces
since staff should not have living spaces.

'''


class Fellow(Person):
    def __init__(
            self, first_name,
            second_name, person_type,
            living_space=None):

        super().__init__(first_name, second_name, person_type)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type
        self.living_space = living_space
        self.availble_living_spaces = ['Python', 'Ruby', 'JavaScript', 'Java']
        self.allocated_living_space = random.choice(
            self.availble_living_spaces)

    def allocate_living_space(self):
        if self.living_space is None:
            pass
        else:
            return '{} has been allocated the livingplace {}.'.format(
                self.first_name, self.allocated_living_space)
