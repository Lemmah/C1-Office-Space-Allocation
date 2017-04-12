from class_person import Person


class Staff(Person):
    def __init__(
            self, first_name,
            second_name, person_type):

        super().__init__(first_name, second_name, person_type)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type

    def fellow_details(self):
        self.full_name = self.full_name()
        return self.full_name
