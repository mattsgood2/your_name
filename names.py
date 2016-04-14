class Asking:

    def __init__(self):
        """asks for your name then stores name in a list"""
        self.my_list = []

        while True:
            self.names = input("Name please > ")
            if len(self.names) != 1:
                print("Longer Name Please")
                return self.names
            if self.names is not str:
                print("Please enter a Name")




            if self.names in self.my_list:
                print("Name Has Been Taken Already Try Again")

            elif self.names not in self.my_list:
                self.my_list.append(self.names)

                if len(self.my_list) == 2:
                    print(self.my_list)
                    break



    # add a name checking if name in my_list print info on them
    # add age checking
    # add info page to then check info on

Asking()
