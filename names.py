class Asking:
    my_list = []

    def __init__(self):
        self.names = input("Name please > ")
        self.my_list.append(self.names)

        while True:
            self.new_name = input("Next name please > ")
            self.my_list.append(self.new_name)
            if len(self.my_list) == 5:
                print(self.my_list)
                break

    # add a name checking if name in my_list print info on them
    # add age checking
    # add info page to then check info on







Asking()
