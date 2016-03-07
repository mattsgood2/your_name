class Asking:
    my_list = []

    def __init__(self):
        self.names = input("name please > ")
        self.my_list.append(self.names)

        while True:
            self.new_name = input("next name please > ")
            self.my_list.append(self.new_name)
            if len(self.my_list) == 5:
                print(self.my_list)
                break








Asking()
