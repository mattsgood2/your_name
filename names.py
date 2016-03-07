class Asking:
    my_list = [

    'matthew',
    'pim',
    'jessica',
    'leo',
    'lillie'

    ]

    def __init__(self):

        while True:
            self.names = input("Name please > ")
            if len(self.names) <= 1:
                print("longer name")

            if self.names in self.my_list:
                print("Name Has Been Taken Alread Try Again")

            elif self.names not in self.my_list:
                self.my_list.append(self.names)

                if len(self.my_list) == 10:
                    print(self.my_list)
                    break



    # add a name checking if name in my_list print info on them
    # add age checking
    # add info page to then check info on

Asking()
