class Person:
    def __init__(self,name,address, phone):
        self.__name=name
        self.__address=address
        self.__phone=phone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__name

    def print_person(self):
        print('Name:',self.__name)
        print('Adress:',self.__address)
        print('Phone:', self.__phone)

class Customer(Person):

    def __init__(self,name,address,phone,cust_num,mail_list):
        Person.__init__(self,name,address,phone)

        self.__cust_num=cust_num
        self.__mail_list= mail_list
    def print_person(self):
        print('Method 1')
        print('Name:',Person.get_name(self))
        print('Adress:',Person.get_address(self))
        print('Phone:',Person.get_phone(self))

        print()
        print()

        print('Method #2')
        Person.print_person(self)


        print('Customer Number:', self.__cust_number)
        if self.__mail_list:
            print('On Mailing List: Yes:')

        else:
            print('On mailing list: No')



