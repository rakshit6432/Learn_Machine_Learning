class Flower:
    def __init__(self):
        self._name = self._petals = self._price = None

    def set_name(self, name):
        try:
            self._name = str(name)
        except ValueError:
            print("Invalid Input for Name, Input must be string")

    def get_name(self):
        return self._name

    def set_petals(self, petals):
        try:
            self._petals = int(petals)
        except ValueError:
            print("Invalid Input for Petals, Input must be integer")

    def get_petals(self):
        return self._petals

    def set_price(self, price):
        try:
            self._price = float(price)
        except ValueError:
            print("Invalid Input for Price, Input must be float")

    def get_price(self):
        return self._price


if __name__ == '__main__':
    Tulips = Flower()
    Tulips.set_name('Tulips')
    Tulips.set_petals(50)
    Tulips.set_price(20)
    print("Name: {:>18}\nNumber of Petals: {}\nPrice: {:>15}".format(Tulips.get_name(),
                                                                     Tulips.get_petals(),
                                                                     Tulips.get_price()))
