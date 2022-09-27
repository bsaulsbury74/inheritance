import PersonClass as pc

def main():
    name ='John'
    address='1234 Main st'
    phone= '123-456-7890'
    cust_number=1234
    mail_list=True

    person1= pc.Person(name,address,phone)


    customer1= pc.Customer(name,address,phone,cust_number,mail_list)

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()

main()


