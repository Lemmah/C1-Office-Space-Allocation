from scripts.class_fellow import Fellow


class Dojo:
    def __init__(self):
        self.allocations = {}

    def room_allocations(self):
        fellow = Fellow('James', 'Lemayian', 'Fellow',
                        'Blue').allocate_living_space()
        # Appending values to the dictionary
        self.allocations['{}'.format(fellow[2])] = fellow[1]
        return self.allocations
