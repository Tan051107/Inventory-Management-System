#TAN YIK YANG
#TP075377

import datetime


def data_sort_out(file_name):
    result = list()
    with open(file_name, "r") as data_file:
        for data_record in data_file:
            data_record = data_record[:-1]
            user_data = data_record.split(',')
            result.append(user_data)
    return result


def table_view(headers, data, column_size, data_size):
    column = headers
    user_data = data
    title = (print(" ".join(f"{header:<{column_size}}" for header in column)))
    for row in user_data:
        record = (print(" ".join(f"{str(item):<{data_size}}" for item in row)))

    return title, record

def data_sort_out_2(file_name):
    result = list()
    result_no_split = list ()
    with open(file_name, "r") as data_file:
        for data_record in data_file:
            data_record = data_record[:-1]
            result_no_split.append(data_record)
            user_data = data_record.split(',')
            result.append(user_data)
    data_file.close()
    return result,result_no_split

def table_view_2(headers, data, colum_size, data_size):
    column = headers
    user_data = data
    title = (print(" ".join(f"{header:<{colum_size}}" for header in column)))
    for row in user_data:
        record = (print(" ".join(f"{str(item):<{data_size}}" for item in row)))
    if user_data == []:
        return title
    else:
        return title, record


def user_brief_info(user_record):
    user_list = list()
    for user in range(len(user_record)):
        approved_user = list()
        if user_record[user][-1].upper() == "APPROVED":
            approved_user.insert(0, user_record[user][0])
            approved_user.insert(1, user_record[user][1])
            approved_user.insert(2, user_record[user][-1])
            user_list.append(approved_user)
    return user_list


def user_id(user_id_number):
    id_num = list()
    for i in range(len(user_id_number)):
        id_num.append(user_id_number[i][0])
    return id_num


def login_datetime(id_num, user_type, access_type):
    import datetime
    current_datetime = datetime.datetime.now()
    Date = current_datetime.strftime("%Y-%m-%d")
    Time = current_datetime.strftime("%H:%M:%S")
    with open("Login datetime.txt", "a+") as login_record:
        login_record.writelines(id_num + "," + Date + "," +
                                Time + "," + access_type + "," + user_type + "\n")


def user_activities(user_id, identity, activities, description):
    import datetime
    current_datetime = datetime.datetime.now()
    Date = current_datetime.strftime("%Y-%m-%d")
    Time = current_datetime.strftime("%H:%M:%S")
    with open("User Activities.txt", "a+") as user_activities:
        user_activities.writelines(user_id + "," + identity + "," + Date + "," + Time + "," +
                                   activities + "," + description + "\n")

def customer_validity():
    customer_data = data_sort_out(file_name="Customer data.txt")
    for i in range(len(customer_data)):
        if customer_data[i][0] == cus_id:
            return True, i
    return False, 0


def customer_acc_validity():
    customer_data = data_sort_out(file_name="Customer data.txt")
    for index in range(len(customer_data)):
        if len(customer_data[index]) == 8:
            if customer_data[index][0] == cus_id and customer_data[index][-1].upper() == "APPROVED":
                return True, index
    return False, 0


def new_cus_validity():
    customer_data = data_sort_out(file_name="Customer data.txt")
    for i in range(len(customer_data)):
        if len(customer_data[i]) == 6:
            if customer_data[i][1] == identity_num and customer_data[i][-1].upper() == "APPROVED":
                return True, i
    return False, 0


def new_cus_register_validity():
    customer_data = data_sort_out(file_name="Customer data.txt")
    for i in range(len(customer_data)):
        if len(customer_data[i]) == 6:
            if customer_data[i][1] == identity_num:
                return True
    return False


def create_password():
    password = input("Create a strong password: ")
    confirm_password = input("Please reconfirm your password: ")
    attempt = 0
    while password != confirm_password:  # this loop continues until the user confirmed the password correctly
        if attempt < 3:
            print("Password unmatch!!!")
            confirm_password = input("Please reconfirm your password:")
        elif attempt >= 3:  # user will be asked to create another password when confirm password wrongly 3 times
            print("Password unmatch!!!")
            recreate = input("Do you want to recreate the password? (Yes/No): ")
            while recreate.upper() != "YES" and recreate.upper() != "NO":
                recreate = input("Do you want to recreate the password? (Yes/No): ")
            if recreate.upper() == "YES":
                password = input("Create a strong password: ")
                confirm_password = input("Please reconfirm your password: ")
            elif recreate.upper() == "NO":
                confirm_password = input("Please reconfirm your password: ")
        if password == confirm_password:
            break
        attempt += 1
    return password


def generate_cus_id():
    customer_acc = data_sort_out(file_name="Customer data.txt")
    id_list = list()
    for i in range(len(customer_acc)):
        if len(customer_acc[i]) == 8:
            id_list.append(customer_acc[i][0])
    max_num = 1
    record_length = str(len(id_list))
    for x in range(len(id_list)):
        id_letter = list(id_list[x])
        four_digit_num = str(id_letter[-4] + id_letter[-3] + id_letter[-2] + id_letter[-1])
        four_digit_num = int(four_digit_num)
        if four_digit_num > max_num:
            max_num = four_digit_num
        else:
            continue
    total = max_num + 1
    if len(record_length) == 1:
        id_num = "TP000" + str(total)
    elif len(record_length) == 2:
        id_num = "TP00" + str(total)
    elif len(record_length) == 3:
        id_num = "TP0" + str(total)
    elif len(record_length) == 4:
        id_num = "TP" + str(total)
    return id_num


def customer_login():
    customer_data = data_sort_out(file_name="Customer data.txt")
    if cus_validity:  # check the existence of customer
        if cus_acc_validity:  # check whether the customer has an account or not
            login_password = input("Please enter your password: ")
            while login_password != customer_data[cus_acc_index][6]:
                login_password = input("Please enter your password: ")
            print("Log in successfully!!!")
            print("Welcome to KLCCC")
            login_datetime(id_num=cus_id, user_type="Customer", access_type="Log In")
            return True
        else:  # customer account is not been approved
            print("Your account haven't been approved......Please wait for the approval")
    else:
        print("Invalid ID Number... Please proceed to sign up an account")


def first_time_customer():
    customer_data = data_sort_out(file_name="Customer data.txt")
    if new_customer:
        if ic_num_validity:
            new_password = create_password()
            id_number = generate_cus_id()
            customer_data[new_cus_index].insert(0, id_number)
            customer_data[new_cus_index].insert(6, new_password)
            with open("Customer data.txt", "w") as customer_record:
                for length in range(len(customer_data)):
                    if len(customer_data[length]) == 6:
                        customer_record.writelines(customer_data[length][0] + "," + customer_data[length][1] + ","
                                                   + customer_data[length][2] + "," + customer_data[length][3] + ","
                                                   + customer_data[length][4] + "," + customer_data[length][
                                                       5] + "\n")
                    elif len(customer_data[length]) == 8:
                        customer_record.writelines(customer_data[length][0] + "," + customer_data[length][1] + ","
                                                   + customer_data[length][2] + "," + customer_data[length][3] + ","
                                                   + customer_data[length][4] + "," + customer_data[length][5] + ","
                                                   + customer_data[length][6] + "," + customer_data[length][
                                                       7] + "\n")
            login_datetime(id_num=id_number, user_type="Customer", access_type="Activation")
            print("Account activate successfully!!!")
            print("This is your ID Number: ", id_number)
            print("Please use the ID Number for login")
        else:
            print("You account haven't been approved.... Please wait for the approval")
    else:
        print("Invalid identity number.... Please proceed to sign up an account")


def customer_register():
    import datetime
    customer_data = data_sort_out(file_name="Customer data.txt")
    ic_list = list()
    for i in range(len(customer_data)):
        if len(customer_data[i]) == 6:
           ic_list.append(customer_data[i][2])
    while True:
        print("          Customer register          ")
        print("_____________________________________")
        print("Please enter the information below: ")
        cus_name = input("Name: ")
        ic_passport_number = input("IC/Passport number: ")
        phone_number = input("Phone number: ")
        city = input("City of domicile: ")
        current_datetime = datetime.datetime.now()
        date_of_registration = current_datetime.strftime("%Y-%m-%d")
        print("Registration Date: ", date_of_registration)
        print("________________________________")
        print("Please select: ")
        print("a) '1' - Confirm registration")
        print("b) '2' - Rewrite information")
        print("________________________________")
        options = input("Please enter the number: ")
        while options != "1" and options != "2":
            print("Invalid option")
            options = input("Please enter the number: ")
        if options == "1":
            if ic_passport_number in ic_list:
                print("You have registered your account...Kindly wait for the approval")
                break
            with open("Customer data.txt", "a+") as customer_record:
                    customer_record.writelines(cus_name + "," + ic_passport_number + ","
                                               + phone_number + "," + city + "," + date_of_registration + ","
                                               + "Unapproved" + "\n")
            login_datetime(id_num=ic_passport_number, user_type="Customer", access_type="Registration")
            print("Registration has been request...Kindly wait for the approval")
            print("Returning to registration interface....")
            break
        elif options == "2":
            continue



def admin_register():
    admin_data = data_sort_out(file_name="admin data.txt")
    id_info =list()
    for index in range(len(admin_data)):
        id_info.append(admin_data[index][0])
    while True:
        print("Please enter the information below: ")
        admin_id = input("Staff ID: ")
        while (admin_id[0] + admin_id[1]) != "TP":
            print("ID Number must consist 'TP' in front")
            print("Sample: TP123456")
            admin_id = input("Please enter the staff id: ")
        while len(admin_id[2:len(admin_id)]) != 6:
            print("Number after 'TP' must have 6 numbers")
            admin_id = input("Please enter the staff id: ")
        if admin_id in id_info:
            print(f"The Staff ID ({admin_id}) has already registered an account")
            break
        elif admin_id not in id_info:
            admin_name = input("Name: ")
            print("_____________________________")
            print("Please select: ")
            print("a) '1' - Confirm Registration")
            print("b) '2' - Rewrite Information")
            print("_____________________________")
            option = input("Please enter the number: ")
            while option != "1" and option != "2":
                print("Invalid option...")
                option = input("Please enter the number: ")
            if option == "1":
                print("Sign up Successfully!!! Please wait for registration approval.....")
                login_datetime(id_num=admin_id, user_type="Admin", access_type="Registration")
                with open("admin data.txt", "a+") as admin_record:
                    admin_record.writelines(admin_id + "," + admin_name + "," + "Unapproved" + "\n")
                    admin_record.close()
                    break
            elif option == "2":
                continue


def admin_info_validity():
    admin_data = data_sort_out(file_name="admin data.txt")
    for index in range(len(admin_data)):
        if admin_data[index][0] == staff_id:
            return True, index
    return False, 0


def admin_acc_validity():
    admin_info = data_sort_out(file_name="admin data.txt")
    for i in range(len(admin_info)):
        if len(admin_info[i]) == 4:
            if admin_info[i][0] == staff_id and admin_info[i][3].upper() == "APPROVED":
                return True, i
    return False, 0


def new_admin_acc_validity():
    admin_info = data_sort_out(file_name="admin data.txt")
    for i in range(len(admin_info)):
        if len(admin_info[i]) == 3:
            if admin_info[i][0] == staff_id and admin_info[i][2].upper() == "APPROVED":
                return True, i
    return False, 0


def admin_login():
    admin_info = data_sort_out(file_name="admin data.txt")
    if user_validity:  # find the user exist in the system or not
        if user_status.upper() == "NO":
            if acc_valid:
                login_password = input("Please enter your password: ")
                while login_password != admin_info[pass_index][2]:
                    login_password = input("Please enter your password: ")
                print("Welcome to Customer Management System")
                login_datetime(id_num=staff_id, user_type="Admin", access_type="Log In")
                return True
            else:
                print("Your accoun  t haven't been approved....Please wait for the approval")
        elif user_status.upper() == "YES":
            if acc_valid:
                print("You have own an account.Kindly proceed to login")
            elif new_admin_acc:
                new_password = create_password()
                admin_info[acc_pass_index].insert(2, new_password)
                with open("admin data.txt", "w") as admin_record:
                    for length in range(len(admin_info)):
                        if len(admin_info[length]) == 3:
                            admin_record.writelines(admin_info[length][0] + "," + admin_info[length][1] + "," +
                                                    admin_info[length][2] + "\n"
                                                    )
                        elif len(admin_info[length]) == 4:
                            admin_record.writelines(admin_info[length][0] + "," + admin_info[length][1] + "," +
                                                    admin_info[length][2] + "," + admin_info[length][3] + "\n"
                                                    )
                login_datetime(id_num=staff_id, user_type="Admin", access_type="Activation")
                print("Account have successfully activated!!! Kindly proceed to login")

            elif new_admin_acc is False:
                print("Your account haven't been approved....Please wait for the approval")
    else:
        print("Staff ID has not registered yet... Please proceed to register")


def super_user():  # super user log in
    super_user_list = data_sort_out(file_name="Super User data.txt")
    while True:
        id_number = input("ID Number: ")
        password = input("Password: ")
        print("___________________________________")
        print("Please enter: " )
        print("a) '1' for continue")
        print("b) '2' for re-enter the information")
        print("___________________________________")
        option = input("Please enter the number: ")
        while option != "1" and option != "2":
            print("Invalid options...")
            option = input("Please enter the number: ")
        id_record = list()
        for i in range(len(super_user_list)):
            if super_user_list[i][0] not in id_record:
                id_record.append(super_user_list[i][0])
        if option == "1":
            if id_number not in id_record:
                print("Invalid ID Number...")
                print("Please enter valid user ID")
                continue
            elif super_user_list[id_record.index(id_number)][-1] != password:
                print("Invalid Password")
                print("Please enter valid user password")
                continue
            else:
                print("Welcome to user management system")
                login_datetime(id_num=id_number, access_type="Log In", user_type="Super User")
                return id_number
        elif options == 0:
            continue


def inventory_staff_register():
    inventory_staff_info = data_sort_out(file_name="staff info.txt")
    id_list = []
    for id in inventory_staff_info:
        id_list.append(id[0])

    info_file = open("staff info.txt", "a+")
    while True:
        ID = input("Enter your staff ID:")
        while (ID[0] + ID[1]) != "TP":
            print("ID Number must consist 'TP' in front")
            print("Sample: TP123456")
            ID = input("Please enter the staff id: ")
        while len(ID[2:len(ID)]) != 6:
            print("Number after 'TP' must have 6 numbers")
            ID = input("Please enter the staff id: ")
        if ID in id_list:
            print(f"This Staff ID ({ID}) ha"
                  f"s already registered an account.")
            break
        name = input("Enter your name:")
        line = (ID+","+name+","+"Unapproved"+"\n")
        print("______________________________")
        print("Please select: ")
        print("a) '1' - Complete Registration")
        print("b) '2' - Rewrite Information")
        print("______________________________")
        option = input("Please enter the number: ")
        while option != "1" and option != "2":
            print("Invalid option...")
            option = input("Please enter the number")
        if option == "1":
            print("You will be notified if you have successfully registered.")
            info_file.writelines(line)
            login_datetime(id_num=ID, user_type="Inventory staff", access_type="Registration")
            info_file.close()
            break

        elif option == "2":
            continue
    info_file.close()


def check_index():
    inventory_staff_info = data_sort_out(file_name="staff info.txt")

    for i in range(len(inventory_staff_info)):
        if inventory_staff_info[i][0] == login_id:
            return True, i
    return False, 0


def check_password():
    inventory_staff_acc_info = data_sort_out(file_name="staff account.txt")

    for i in range(len(inventory_staff_acc_info)):
        if inventory_staff_acc_info[i][0] == login_id:
            return True, i
    return False, 0


def inventory_staff_log_in():
    inventory_staff_acc_info = data_sort_out(file_name="staff account.txt")

    inventory_staff_info = data_sort_out(file_name="staff info.txt")

    if check:  # to check whether the user has registered or not
        if inventory_staff_info[index][2].upper() == "APPROVED":  # to check whether the user is approved
            if check_first_time.upper() == "NO":  # to check whether the user is first time user
                if check_acc:  # to check the user has activated his account
                    login_password = input("Enter your password:")
                    while login_password != inventory_staff_acc_info[acc_index][1]:  # this loop continues until user enters the correct password
                        login_password = input("Password incorrect. Please enter again:")
                    print("Welcome to Inventory Management System")
                    login_datetime(id_num=login_id, user_type="Inventory staff", access_type="Log In")
                    return True
                else:
                    print("You have not activated your account. Kindly proceed to activate your account.")

            elif check_first_time.upper() == "YES":
                if check_acc:  # to check whether user already has an account beforehand
                    print("You already own an account. Kindly proceed to login.")
                else:
                    password_create = create_password()
                    print("Congratulations! You have successfully activated your account.Kindly proceed to login.")
                    acc_info_file = open("staff account.txt", "a+")
                    line = (login_id + "," + password_create + "\n")
                    acc_info_file.writelines(line)
                    acc_info_file.close()
                login_datetime(id_num=login_id, user_type="Inventory Staff", access_type="Activation")
        else:
            print("Your account is not approved yet. Please wait patiently.")
    else:
        print("This Staff ID has not registered yet. Kindly proceed to register.")

# Customer menu
def curr_date ():
    current_date = datetime.datetime.now()
    date_str = datetime.datetime.strftime(current_date, "%d-%m-%Y")
    return date_str

def curr_time ():
    current_date = datetime.datetime.now()
    time_str = datetime.datetime.strftime(current_date,  "%H:%M:%S")
    return time_str


def id_list_stock ():
    stock_id_list = []
    for stock_id_index in range(len(stock_list)):
        stock_id_list.append(stock_list [stock_id_index] [0])
    return stock_id_list

def repair_timeline():
    initial_date = curr_date ()
    i = 0
    timeline_date_list = []
    while i<8:
        initial_date_object = datetime.datetime.strptime(initial_date,"%d-%m-%Y")
        timeline_date_list.append (initial_date)
        days_add_1 = datetime.timedelta(days=1)
        initial_date = (initial_date_object+days_add_1).strftime("%d-%m-%Y")
        i+=1
    return (timeline_date_list[1:])


def repair_date_list():
    list_no_repeat = []
    list_repeat = []
    for i in range (len(repair_order_list)):
        if repair_order_list [i][8] == "Payment Completed":
            list_repeat.append (repair_order_list [i][3])
        if repair_order_list [i][3] not in list_no_repeat and repair_order_list [i][8] == "Payment Completed":
            list_no_repeat.append (repair_order_list [i][3])
    return list_no_repeat,list_repeat




def date_available_for_repair (initial_timeline, list_no_repeat, list_repeat):
    repair_date_frequency = {}
    not_available_date_list = []
    available_date_list = []
    for dates in list_repeat:
        if dates not in repair_date_frequency:
            repair_date_frequency[dates] = 0
        repair_date_frequency[dates] +=1
    for date in list_no_repeat:
        if repair_date_frequency[date] >4:
            not_available_date_list.append(date)

    for timeline in initial_timeline:
        if timeline not in not_available_date_list:
            available_date_list.append(timeline)
    return available_date_list

def validate_value_error(no):
    while True:
        try:
            no = float(no)
            return no
        except ValueError:
            no = input("Please enter a valid number:")


stock_list,stock_list_no_split = data_sort_out_2("stock.txt")
inventory_order_list, inventory_order_list_no_split = data_sort_out_2("inventory purchase order status.txt")
order_status_list, order_status_list_no_split = data_sort_out_2("purchase order status.txt")
repair_order_list,repair_order_list_no_split = data_sort_out_2("service&repair order status.txt")



#--------------------------------------Customer Purchase Order------------------------------------------

def stock_available():
    stock_list_before_update,stock_list_no_split_before_update =  data_sort_out_2("stock.txt")
    available_stock_list = []
    for available_stock_index in range (1,len(stock_list_before_update)):
        if int(stock_list_before_update [available_stock_index][3])>0:
            available_stock_list.append (stock_list_before_update [available_stock_index][0])
    return available_stock_list

def purchase_item (stock_purchase):
    stock_id_list = id_list_stock()
    for purchase_item_index in range (len(stock_id_list)):
        if stock_id_list[purchase_item_index] == stock_purchase:
            return purchase_item_index


def check_repeat_order(login_id, stock_purchase):
    for i in range(len(order_status_list)):
        if [order_status_list[i][0], order_status_list[i][1],order_status_list[i][9]] == [login_id, stock_purchase,"Payment Incomplete"]:
            return True,i,order_status_list[i][3]
    return False,0,0

def purchase_stock_details(stock_purchase):
    for i in range (len(stock_list)):
        if stock_list[i][0]==stock_purchase:
            return stock_list[i][1],stock_list[i][2]

def print_stock_for_purchase():
    stock_list_before_update, stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    details_except_date_list = []
    for available_stock_index in range(1, len(stock_list_before_update)):
        if int(stock_list_before_update[available_stock_index][3]) > 0:
            details_except_date_list.append([stock_list_before_update[available_stock_index][0], stock_list_before_update[available_stock_index][1],stock_list_before_update[available_stock_index][2],stock_list_before_update[available_stock_index][3]])
    stock_headers = ["Stock ID", "Stock Name", "Price(RM)", "Quantity_In_Stock"]
    table_view_2(stock_headers, details_except_date_list, "20", "20")
    if details_except_date_list == []:
        return False
    else:
        return True

#--------------------------------------------View Cart(Customer)------------------------------------------------

def specific_stock_index(stock):
    for i in range (len(order_status_list)):
        if [order_status_list[i][0],order_status_list[i][1],order_status_list[i][9]]==[login_id,stock,"Payment Incomplete"]:
            return i,order_status_list[i][3]

def specific_stock_details(stock_list,stock):
    for i in range(len(stock_list)):
        if stock_list[i][0] == stock:
            return stock_list[i][0],stock_list[i][1],stock_list[i][2],stock_list[i][3],i

def print_user_cart (order_status_list):
    user_cart = []
    for user_order_index in range(len(order_status_list)):
        if [order_status_list[user_order_index][0], order_status_list[user_order_index][9]] == [login_id,"Payment Incomplete"]:
            user_cart.append([order_status_list[user_order_index][1], order_status_list[user_order_index][2],order_status_list[user_order_index][3], order_status_list[user_order_index][4],order_status_list[user_order_index][5]])
    cart_headers = ["Stock ID", "Stock Name", "Quantity Ordered", "Total Price (RM)", "Last Modified Date"]
    table_view_2(cart_headers, user_cart, "20", "20")
    if user_cart == []:
        return False,0
    else:
        return True,user_cart


def cart_stock_list (user_cart):
    user_cart_stock_list = []
    for user_cart_index in range(len(user_cart)):
        user_cart_stock_list.append (user_cart[user_cart_index][0])
    return user_cart_stock_list

def customer_remove_purchase_order(user_cart):
    remove_stock = input("Enter the ID of the stock you want to remove:")
    user_cart_stock_list = cart_stock_list(user_cart)
    while remove_stock not in user_cart_stock_list:
        remove_stock = input("""Stock ID invalid
Enter the correct ID of the stock you want to remove:""")
    removed_stock_index, remove_stock_purchase_quantity = specific_stock_index(remove_stock)
    order_status_list.remove(order_status_list[removed_stock_index])
    order_status_list_no_split.remove(order_status_list_no_split[removed_stock_index])
    order_status_file = open("purchase order status.txt", "w")
    for order in order_status_list_no_split:
        order_status_file.writelines(order + "\n")
    order_status_file.close()
    print(f"{remove_stock} is removed")
    user_activities(login_id,"Customer","Remove purchase order",f"{remove_stock} is removed")




def customer_modify_quantity(user_cart):
    modify_stock = input("Enter the ID of the stock you want to modify the quantity:")
    user_cart_stock_list = cart_stock_list(user_cart)
    while modify_stock not in user_cart_stock_list:
        modify_stock = input("""Stock ID invalid
Enter the correct ID of the stock you want to modify:""")
    stock_list_before_update,stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    modify_stock_id, modify_stock_name, modify_stock_price, modify_stock_quantity, modify_stock_index = specific_stock_details(stock_list_before_update,modify_stock)
    headers = ["Stock ID", "Stock Name", "Quantity In Stock","Price per unit"]
    modified_stock_details = [modify_stock_id, modify_stock_name, modify_stock_quantity,modify_stock_price]
    datas = modified_stock_details
    print(" ".join(f"{header:<20}" for header in headers))
    print(" ".join(f"{header:<20}" for header in datas))
    modify_quantity = input("Enter the new quantity you want to purchase:")
    modify_quantity = validate_value_error(modify_quantity)
    while modify_quantity < 1:
        modify_quantity = input("Enter a valid quantity of stock you want to purchase:")
        modify_quantity = validate_value_error(modify_quantity)
    while modify_quantity > int(modify_stock_quantity):
        modify_quantity = input("""You have exceeded the stock quantity available
Kindly reduce the quantity of stock:""")
        modify_quantity = validate_value_error(modify_quantity)
        while modify_quantity < 1:
            modify_quantity = input("Enter a valid quantity of stock you want to purchase:")
            modify_quantity = validate_value_error(modify_quantity)
    total_price = modify_quantity * float(modify_stock_price)
    total_price = str(total_price)
    modify_quantity = str(modify_quantity)
    modified_stock_index, modified_stock_quantity = specific_stock_index(modify_stock)
    order_status_list[modified_stock_index][3] = modify_quantity
    order_status_list[modified_stock_index][4] = total_price
    order_status_list[modified_stock_index][5] = curr_date()
    order_status_list[modified_stock_index][6] = curr_time()
    modify_quantity_line = (login_id + "," + modify_stock + "," + order_status_list[modified_stock_index][2] + "," + modify_quantity + "," + total_price + "," + curr_date() + "," + curr_time() + "," + "-" + "," + "-" + "," + "Payment Incomplete")
    order_status_list_no_split.remove(order_status_list_no_split[modified_stock_index])
    order_status_list_no_split.insert(modified_stock_index, modify_quantity_line)
    order_status_file = open("purchase order status.txt", "w")
    for line in order_status_list_no_split:
        order_status_file.writelines(line + "\n")
    order_status_file.close()
    print(f"The quantity of {modify_stock} is modified to {modify_quantity}")
    user_activities(login_id, "Customer", "Modify purchase order stock quantity", f"The quantity of {modify_stock} is changed to {modify_quantity}")

def customer_cart_checkout(user_cart):
    checkout_stock = input("Enter the ID of the stock you want to checkout:")
    user_cart_stock_list = cart_stock_list(user_cart)
    while checkout_stock not in user_cart_stock_list:
        checkout_stock = input("""Stock ID invalid
Enter the correct ID of the stock you want to checkout:""")
    stock_list_before_update,stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    checkout_stock_index_order_list, checkout_stock_quantity = specific_stock_index(checkout_stock)
    checkout_stock_id, checkout_stock_name, checkout_stock_price, checkout_stock_original_quantity, checkout_stock_index = specific_stock_details(stock_list_before_update,checkout_stock)
    new_available_quantity = int(checkout_stock_original_quantity) - int(checkout_stock_quantity)
    while new_available_quantity < 0:
        headers = ["Stock ID", "Stock Name", "Quantity In Stock", "Price per unit"]
        checkout_stock_details = [checkout_stock_id, checkout_stock_name, checkout_stock_original_quantity,checkout_stock_price]
        datas = checkout_stock_details
        print(" ".join(f"{header:<20}" for header in headers))
        print(" ".join(f"{header:<20}" for header in datas))
        reduced_stock_quantity = input("""The amount of stock added into the cart is currently insufficient to be checked out
Kindly reduce the quantity of stock to checkout:""")
        reduced_stock_quantity = validate_value_error(reduced_stock_quantity)
        while reduced_stock_quantity < 1:
            reduced_stock_quantity = input("Enter a valid quantity of stock you want to purchase:")
            reduced_stock_quantity = validate_value_error(reduced_stock_quantity)
        reduced_total_price = float(checkout_stock_price) * reduced_stock_quantity
        order_status_list[checkout_stock_index_order_list][3] = str(reduced_stock_quantity)
        order_status_list[checkout_stock_index_order_list][4] = str(reduced_total_price)
        new_available_quantity = int(checkout_stock_original_quantity) - reduced_stock_quantity
    payment_confirmation = input("""Purchase order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
    while payment_confirmation.upper() != "YES" and payment_confirmation.upper() != "NO":
        payment_confirmation = input("""Purchase order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
    if payment_confirmation.upper() == "YES":
        acc_no = input("Enter your bank account number:")
        acc_password = input("Enter your bank account password:")
        order_status_list[checkout_stock_index_order_list][5] = curr_date()
        order_status_list[checkout_stock_index_order_list][6] = curr_time()
        order_status_list[checkout_stock_index_order_list][7] = curr_date()
        order_status_list[checkout_stock_index_order_list][8] = curr_time()
        order_status_list[checkout_stock_index_order_list][9] = "Payment Completed"
        after_checkout_line = (login_id + "," + checkout_stock + "," + checkout_stock_name + "," +order_status_list[checkout_stock_index_order_list][3] + "," +order_status_list[checkout_stock_index_order_list][4] + "," + curr_date() + "," + curr_time() + "," + curr_date() + "," + curr_time() + "," + "Payment Completed")
        order_status_list_no_split.remove(order_status_list_no_split[checkout_stock_index_order_list])
        order_status_list_no_split.insert(checkout_stock_index_order_list, after_checkout_line)
        order_status_file = open("purchase order status.txt", "w")
        for line in order_status_list_no_split:
            order_status_file.writelines(line + "\n")
        order_status_file.close()
        stock_file = open("stock.txt", "w")
        new_available_quantity = str(new_available_quantity)
        update_stock_quantity_line = (checkout_stock_id + "," + checkout_stock_name + "," + checkout_stock_price + "," + new_available_quantity + "," + curr_date())
        stock_list[checkout_stock_index][3] = new_available_quantity
        stock_list_no_split.remove(stock_list_no_split[checkout_stock_index])
        stock_list_no_split.insert(checkout_stock_index, update_stock_quantity_line)
        for item in stock_list_no_split:
            stock_file.writelines(item + "\n")
        stock_file.close()
        print("Payment successful")
        user_activities(login_id, "Customer", "Check out stock in cart", f"{checkout_stock} is checked out")


    else:
        print("Payment unsuccessful")




#-----------------------------------------Service and repair order(customer)---------------------------------------
#------------------------------------------------Nothing-----------------------------------------------------------

#-------------------------------------------Modify service and repair order(customer)-----------------------------
def date_difference(repair_date):
    present = datetime.datetime.now()
    date_ft  = datetime.datetime.strptime(repair_date,"%d-%m-%Y")
    difference = date_ft - present
    if difference.days <0:
        return False
    return True


def order_id_():
    user_order_id = []
    user_order_id_cancel =[]
    for i in range(len(repair_order_list)):
        if repair_order_list [i][1] == login_id and repair_order_list [i][8] == "Payment Incomplete" and date_difference(repair_order_list [i][3])==True:
            user_order_id.append(repair_order_list[i][0])
        if repair_order_list[i][1] == login_id and repair_order_list[i][8] == "Payment Incomplete":
            user_order_id_cancel.append(repair_order_list[i][0])
    if user_order_id_cancel == []:
        return False,False,user_order_id,user_order_id_cancel

    else:
        if user_order_id == []:
            return True,False,user_order_id,user_order_id_cancel

    return False,True,user_order_id,user_order_id_cancel




def print_user_order (repair_order_list):
    user_service_order_list = []
    for i in range(len(repair_order_list)):
        if repair_order_list[i][1] == login_id:
            user_service_order_list.append([repair_order_list[i][0], repair_order_list[i][2], repair_order_list[i][3], repair_order_list[i][4],repair_order_list[i][8]])
    user_order_headers = ["Order ID", "Service", "Repair Date", "Last Modified Date","Payment Status"]
    table_view_2(user_order_headers, user_service_order_list, "20", "20")



def user_service_details(Order_ID):
    for i in range(len(repair_order_list)):
        if repair_order_list[i][0] == Order_ID:
            return i,repair_order_list[i][2],repair_order_list[i][3]


def modify_service(user_order_id):
        change_service_order = input("Enter the order ID for service modification:")
        while change_service_order not in user_order_id:
            change_service_order = input("""Order ID invalid for modification. Modification is not available after repair date or after payment is completed
Enter the correct order ID for service modification:""")
        service = input("""---Services Provided---
a. '1'- Desktop Repair
b. '2'- Desktop Service
c. '3'- Laptop Repair
d. '4'- Laptop Service
Please enter the service you want to change to:""")
        while service != "1" and service != "2" and service != "3" and service != "4":
            service = input("""---Services Provided---
a. '1'- Desktop Repair
b. '2'- Desktop Service
c. '3'- Laptop Repair
d. '4'- Laptop Service
Please enter the correct option:""")
        if service == "1":
            service_provided = "Desktop Repair"
        elif service == "2":
            service_provided = "Desktop Service"
        elif service == "3":
            service_provided = "Laptop Repair"
        else:
            service_provided = "Laptop Service"
        index_modify, service_modify, repair_date_modify = user_service_details(change_service_order)
        repair_order_file = open("service&repair order status.txt", "w")
        repair_order_list[index_modify][2] = service_provided
        repair_order_list[index_modify][4] = curr_date()
        repair_order_list[index_modify][5] = curr_time()
        modify_service_line = (change_service_order + "," + login_id + "," + service_provided + "," + repair_date_modify + "," + curr_date() + "," + curr_time() + "," + "-" + "," + "-" + "," + "Payment Incomplete")
        repair_order_list_no_split.remove(repair_order_list_no_split[index_modify])
        repair_order_list_no_split.insert(index_modify, modify_service_line)
        for line in repair_order_list_no_split:
            repair_order_file.writelines(line + "\n")
        repair_order_file.close()
        print(f"Service is changed to {service_provided}")
        user_activities(login_id, "Customer", "Change the service for service or repair order ", f"The service for order {change_service_order} is changed to {service_provided}")


def modify_repair_date(user_order_id):
    initial_timeline = repair_timeline()
    list_no_repeat, list_repeat = repair_date_list()
    available_date_list = date_available_for_repair(initial_timeline, list_no_repeat, list_repeat)
    change_repair_date_order = input("Enter the order ID for repair date modification:")
    while change_repair_date_order not in user_order_id:
        change_repair_date_order = input("""Order ID invalid for modification. Modification is not available after repair date or after payment is completed
Enter the correct order ID for repair date modification:""")
    print("Choose one of the dates below to send for repair or service:")
    for i in available_date_list:
        print(i)
    repair_date = input("Please enter (dd-mm-yyyy):")
    while repair_date not in available_date_list:
        for i in available_date_list:
            print(i)
        repair_date = input("Please enter the correct date (dd-mm-yyyy):")
    index_modify_repair_date, service_modify_repair_date, repair_date_modify_repair_date = user_service_details(change_repair_date_order)
    modify_repair_date_line = (change_repair_date_order + "," + login_id + "," + service_modify_repair_date + "," + repair_date + "," + curr_date() + "," + curr_time() + "," + "-" + "," + "-" + "," + "Payment Incomplete")
    repair_order_list[index_modify_repair_date][3] = repair_date
    repair_order_list[index_modify_repair_date][4] = curr_date()
    repair_order_list[index_modify_repair_date][5] = curr_time()
    repair_order_list_no_split.remove(repair_order_list_no_split[index_modify_repair_date])
    repair_order_list_no_split.insert(index_modify_repair_date, modify_repair_date_line)
    repair_order_file = open("service&repair order status.txt", "w")
    for line in repair_order_list_no_split:
        repair_order_file.writelines(line + "\n")
    repair_order_file.close()
    print(f"Repair date is changed to {repair_date}.Kindly send your device for repair or service by {repair_date}")
    user_activities(login_id, "Customer", "Change the repair date of a service or repair order ",f"The repair date for order {change_repair_date_order} is changed to {repair_date}")

def make_payment_modify(user_order_id):
    payment_order = input("Enter the order ID for payment:")
    while payment_order not in user_order_id:
        payment_order = input("""Order ID invalid for payment. Payment is no longer available after repair date
Enter the correct order ID for repair date modification:""")
    payment_confirmation = input("""Service or repair order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
    while payment_confirmation.upper() != "YES" and payment_confirmation.upper() != "NO":
        payment_confirmation = input("""Service or repair order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
    if payment_confirmation.upper() == "YES":
        account_no = input("Please enter your bank account number:")
        account_password = input("Please enter your bank account password:")
        index_make_payment, service_make_payment, repair_date_make_payment = user_service_details(payment_order)
        repair_order_file = open("service&repair order status.txt", "w")
        repair_order_list[index_make_payment][8] = "Payment Completed"
        repair_order_list[index_make_payment][4] = curr_date()
        repair_order_list[index_make_payment][5] = curr_time()
        repair_order_list[index_make_payment][6] = curr_date()
        repair_order_list[index_make_payment][7] = curr_time()
        after_payment_line = (payment_order + "," + login_id + "," + service_make_payment + "," + repair_date_make_payment + "," + curr_date() + "," + curr_time() + "," + curr_date() + "," + curr_time() + "," + "Payment Completed")
        repair_order_list_no_split.remove(repair_order_list_no_split[index_make_payment])
        repair_order_list_no_split.insert(index_make_payment, after_payment_line)
        for line in repair_order_list_no_split:
            print (line)
            repair_order_file.writelines(line + "\n")
        repair_order_file.close()
        print (f"Payment Successful. Kindly send your device for repair or service by {repair_date_make_payment}")
        user_activities(login_id, "Customer", "Make payment for a service or repair order ",f"Payment for order {payment_order} is completed")


    else:
        print("Payment Unsuccessful")




def cancel_repair_order(user_order_id_cancel):
    cancel_order = input("Enter the Order ID to cancel:")
    while cancel_order not in user_order_id_cancel:
        cancel_order = input("""Order ID invalid for cancellation. Cancellation is not available after payment is completed
Enter the correct order ID for order cancellation:""")
    index_cancel, service_cancel, repair_date_cancel = user_service_details(cancel_order)
    repair_order_list_no_split.remove(repair_order_list_no_split[index_cancel])
    repair_order_list.remove(repair_order_list[index_cancel])
    repair_order_file = open("service&repair order status.txt", "w")
    for line in repair_order_list_no_split:
        repair_order_file.writelines(line + "\n")
    print("Order is cancelled")
    user_activities(login_id, "Customer", "Cancel a service or repair order ", f"Order {cancel_order} is cancelled")

#--------------------------------------------------Main body-----------------------------------------------------------

def customer_purchase_order():
    i= 0
    while True:
        print_stock_for_purchase()
        if len(stock_list) < 2:
            print("No stock available for adjustments")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break

        else:
            available_stock_list = stock_available()
            stock_purchase = input("Enter the ID of the stock you want to purchase:")
            while stock_purchase not in available_stock_list:
                stock_purchase = input("""Stock ID invalid
Enter the correct ID of the stock you want to purchase:""")
            repeat_order, order_status_index, previous_order_quantity = check_repeat_order(login_id, stock_purchase)
            purchase_quantity = input("How many do you want to purchase:")
            purchase_quantity = validate_value_error(purchase_quantity)
            while purchase_quantity <1:
                purchase_quantity = input("Enter a valid quantity of stock you want to purchase:")
                purchase_quantity = validate_value_error(purchase_quantity)
            if i<1:
                available_stock_quantity = int(stock_list[purchase_item(stock_purchase)][3])-int(previous_order_quantity)
                i+=1
            else:
                available_stock_quantity = int(stock_list[purchase_item(stock_purchase)][3])
            new_quantity = available_stock_quantity-purchase_quantity
            while new_quantity < 0:
                purchase_quantity = input("""You have exceeded the stock quantity available
Kindly reduce the quantity of stock:""")
                purchase_quantity = validate_value_error(purchase_quantity)
                while purchase_quantity < 1:
                    purchase_quantity = input("Enter a valid quantity of stock you want to purchase:")
                    purchase_quantity = validate_value_error(purchase_quantity)
                new_quantity = available_stock_quantity - purchase_quantity
            stock_list[purchase_item(stock_purchase)][3] = new_quantity
            back = True
            while back == True:
                add_cart_or_buy = input("""a. '1'- Add to cart
b. '2'- Buy now
Please enter:""")
                while add_cart_or_buy!= "1" and add_cart_or_buy!= "2":
                    add_cart_or_buy = input("""a. '1'- Add to cart
b. '2'- Buy now
Please enter the correct option:""")
                new_quantity = str(new_quantity)
                purchase_stock_name,purchase_stock_price = purchase_stock_details(stock_purchase)
                if add_cart_or_buy == "1":
                    print ("Item is added into cart")
                    if repeat_order:
                        purchase_order_file = open("purchase order status.txt", "w")
                        new_order_quantity = int(order_status_list[order_status_index][3])+purchase_quantity
                        total_price = float(purchase_stock_price)*new_order_quantity
                        total_price = str(total_price)
                        new_order_quantity = str(new_order_quantity)
                        new_line = (login_id+","+stock_purchase+","+purchase_stock_name+","+new_order_quantity+","+total_price+","+curr_date()+","+curr_time ()+","+"-"+","+"-"+","+"Payment Incomplete")
                        order_status_list_no_split.remove(order_status_list_no_split[order_status_index])
                        order_status_list_no_split.insert(order_status_index,new_line)
                        for details in order_status_list_no_split:
                            purchase_order_file.writelines(details+ "\n")
                        purchase_order_file.close()
                        order_status_list[order_status_index][3] = new_order_quantity
                        order_status_list[order_status_index][4] = total_price
                        order_status_list[order_status_index][5] = curr_date()
                        order_status_list[order_status_index][6] = curr_time()




                    else:
                        purchase_order_file = open("purchase order status.txt", "a+")
                        total_price = purchase_quantity* float(purchase_stock_price)
                        total_price=str(total_price)
                        purchase_quantity = str(purchase_quantity)
                        line_split = [login_id,stock_purchase,purchase_stock_name,purchase_quantity,total_price,curr_date(),curr_time (),"-","-","Payment Incomplete"]
                        order_status_list.append(line_split)
                        line = (login_id+","+stock_purchase+","+purchase_stock_name+","+purchase_quantity+","+total_price+","+curr_date()+","+curr_time ()+","+"-"+","+"-"+","+"Payment Incomplete")
                        order_status_list_no_split.append(line)
                        purchase_order_file.writelines(line+"\n")
                        purchase_order_file.close()
                    back = False

                    user_activities(login_id, "Customer", "Added an item into cart", f"Added {purchase_quantity} {purchase_stock_name} into cart")



                else:
                    payment_confirmation = input("""Purchase order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
                    while payment_confirmation.upper() != "YES" and payment_confirmation.upper() != "NO":
                        payment_confirmation = input("""Purchase order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
                    if payment_confirmation.upper() == "YES":
                        acc_no = input("Enter your bank account number:")
                        acc_password = input("Enter your bank account password:")
                        print ("Payment successful")
                        total_price = purchase_quantity* float (purchase_stock_price)
                        total_price=str(total_price)
                        purchase_quantity = str(purchase_quantity)
                        purchase_order_file = open ("purchase order status.txt","a+")
                        stock_file = open ("stock.txt","w")
                        line = (login_id+","+stock_purchase+","+purchase_stock_name+","+purchase_quantity+","+total_price+","+curr_date()+","+curr_time()+","+curr_date()+","+curr_time()+","+"Payment Completed"+"\n")
                        line_split = [login_id,stock_purchase,purchase_stock_name,purchase_quantity,total_price,curr_date(),curr_time(),curr_date(),curr_time(),"Payment Completed"]
                        order_status_list.append(line_split)
                        purchase_order_file.writelines(line)
                        purchase_order_file.close()
                        update_stock_quantity = (stock_list[purchase_item (stock_purchase)][0]+","+stock_list[purchase_item (stock_purchase)][1]+","+stock_list[purchase_item (stock_purchase)][2]+","+new_quantity+","+curr_date())
                        stock_list[purchase_item (stock_purchase)][3] = new_quantity
                        stock_list[purchase_item(stock_purchase)][4] = curr_date()
                        stock_list_no_split.remove(stock_list_no_split[purchase_item (stock_purchase)])
                        stock_list_no_split.insert(purchase_item (stock_purchase),update_stock_quantity)
                        for item in stock_list_no_split:
                            stock_file.writelines(item+"\n")
                        stock_file.close()
                        user_activities(login_id, "Customer", "Placed a purchase order",f"Placed an order of {purchase_quantity} {purchase_stock_name}")
                        back = False

                    else:
                        print("Payment unsuccessful")
                        continue


            continue_purchase = input("""a. '1'- Continue purchase other items
b. '2'- Return
Please enter:""")
            while continue_purchase!="1" and continue_purchase!="2":
                continue_purchase = input("""a. '1'- Continue purchase other items
b. '2'- Return
Please enter the correct option:""")
            if continue_purchase== "2":
                break



def view_cart():
    while True:
        cart_availability, user_cart = print_user_cart(order_status_list)
        if cart_availability:
            modify_or_check_out = input("""a. '1'- Modify Purchase Order
b. '2'- Checkout
c. '3'- Return
Please enter:""")
            while modify_or_check_out != "1" and modify_or_check_out!= "2" and modify_or_check_out!= "3":
                modify_or_check_out = input("""a. '1'- Modify Purchase Order
b. '2'- Checkout
c. '3'- Return
Please enter the correct option:""")
            if modify_or_check_out == "1":
                remove_or_change_quantity = input("""a. '1'- Remove a stock
b. '2'- Modify Ordered Quantity
c. '3'- Return
Please enter:""")
                while remove_or_change_quantity !="1" and remove_or_change_quantity != "2" and remove_or_change_quantity !="3" :
                    remove_or_change_quantity = input("""a. '1'- Remove a stock
b. '2'- Modify Ordered Quantity
c. '3'- Return
Please enter the correct option:""")
                if remove_or_change_quantity == "1":
                    customer_remove_purchase_order(user_cart)



                elif remove_or_change_quantity == "2":
                    customer_modify_quantity(user_cart)


            elif modify_or_check_out == "2":
                customer_cart_checkout(user_cart)



            else:
                break

        else:
            print("No order added to cart")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break


def service_or_repair_order():
    while True:
        initial_timeline = repair_timeline()
        list_no_repeat, list_repeat = repair_date_list()
        available_date_list = date_available_for_repair(initial_timeline, list_no_repeat, list_repeat)
        service = input("""---Services Provided---
a. '1'- Desktop Repair
b. '2'- Desktop Service
c. '3'- Laptop Repair
d. '4'- Laptop Service
Please enter:""")
        while service != "1" and service != "2" and service != "3" and service != "4":
            service = input("""---Services Provided---
a. '1'- Desktop Repair
b. '2'- Desktop Service
c. '3'- Laptop Repair
d. '4'- Laptop Service
Please enter the correct option:""")
        if service == "1":
            service_provided = "Desktop Repair"
        elif service == "2":
            service_provided = "Desktop Service"
        elif service == "3":
            service_provided = "Laptop Repair"
        else:
            service_provided = "Laptop Service"

        print ("Choose one of the dates below to send for repair or service:")
        for i in available_date_list:
            print (i)
        repair_date = input("Please enter (dd-mm-yyyy):")
        while repair_date not in available_date_list:
            for i in available_date_list:
                print(i)
            repair_date = input("Please enter the correct date (dd-mm-yyyy):")
        back = True
        while back == True:
            payment_method = input("""Payment Method
a. '1'- Bank Transfer
b. '2'- Pay Upon Arrival To Shop
Please enter:""")
            while payment_method != "1" and payment_method != "2":
                payment_method = input("""Payment Method
a. '1'- Bank Transfer
b. '2'- Pay Upon Arrival To Shop
Please enter the correct option:""")
            if len(repair_order_list) < 2:
                order_id = "0001"
            else:
                maximum = 0
                for i in range(1, len(repair_order_list)):
                    if int(repair_order_list[i][0]) > maximum:
                        maximum = int(repair_order_list[i][0])
                index = maximum + 1
                if index < 10:
                    order_id = ("000" + str(index))
                elif index < 100:
                    order_id = ("00" + str(index))
                else:
                    order_id = ("0" + str(index))
            if payment_method == "1":
                payment_confirmation = input("""Service or repair order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
                while payment_confirmation.upper() != "YES" and payment_confirmation.upper() != "NO":
                    payment_confirmation = input("""Service or repair order modification is not available after payment. 
Confirm to make payment?(Yes/No): """)
                if payment_confirmation.upper() == "YES":
                    account_no = input("Please enter your bank account number:")
                    account_password = input("Please enter your bank account password:")
                    print (f"Payment Successful. Kindly send your device for repair or service by {repair_date}")
                    repair_order_file = open("service&repair order status.txt", "a+")
                    line = (order_id+","+login_id+","+service_provided+","+repair_date+","+curr_date()+","+curr_time()+","+curr_date()+","+curr_time()+","+"Payment Completed"+"\n")
                    line_split = [order_id,login_id,service_provided,repair_date,curr_date(),curr_time(),curr_date(),curr_time(),"Payment Completed"]
                    repair_order_list.append(line_split)
                    repair_order_file.writelines(line)
                    repair_order_file.close()
                    back = False
                    user_activities(login_id, "Customer", "Placed a service or repair order",f"Placed a {service_provided} order. Payment Completed")

                else:
                    print ("Payment unsuccessful")


            else:
                print(f"Kindly send your device for repair or service by {repair_date}")
                print ("""---Reminder---
Repair or Service will not be proceeded if payment is not completed """)
                repair_order_file = open("service&repair order status.txt", "a+")
                line = (order_id+","+login_id+","+service_provided+","+repair_date+","+curr_date()+","+curr_time()+","+"-"+","+"-"+","+"Payment Incomplete"+"\n")
                line_split = [order_id,login_id,service_provided,repair_date,curr_date(),curr_time(),"-","-","Payment Incomplete"]
                repair_order_list.append(line_split)
                repair_order_file.writelines(line)
                repair_order_file.close()
                user_activities(login_id, "Customer", "Placed a service or repair order",f"Placed a {service_provided} order. Payment Incomplete")
                back = False

        continue_order = input("""a. '1'- Send another device for repair or service
b. '2'- Return
Please enter:""")
        while continue_order!= "1" and  continue_order!= "2":
            continue_order = input("""a. '1'- Send another device for repair or service
b. '2'- Return
Please enter the correct option:""")

        if continue_order == "2":
            break


def modify_service_order():
    while True:
        print_user_order(repair_order_list)
        cancel_availability,modify_availability,user_order_id,user_order_id_cancel = order_id_()
        if cancel_availability:
            print("Only cancel order is available for repair date that is over")
            modification = input("""a.'1'- Cancel Order
b.'2'- Return
Please enter:""")
            while modification != "1" and modification != "2":
                modification = input("""a.'1'- Cancel Order
b.'2'- Return
Please enter the correct option:""")

            if modification == "1":
                cancel_repair_order(user_order_id_cancel)

            else:
                break

        elif modify_availability:
            modification = input("""a.'1'- Change Service
b.'2'- Change Repair Date
c.'3'- Make Payment
d.'4'- Cancel Order
e.'5'- Return
Please enter:""")
            while modification != "1" and modification != "2" and modification != "3" and modification!="4" and  modification!="5":
                modification = input("""a.'1'- Change Service
b.'2'- Change Repair Date
c. '3'- Make Payment
d. '4'- Cancel Order
e.'5'- Return
Please enter the correct option:""")

            if modification == "1":
                modify_service(user_order_id)


            elif modification == "2":
                modify_repair_date(user_order_id)


            elif modification == "3":
                make_payment_modify(user_order_id)

            elif modification == "4":
                cancel_repair_order(user_order_id_cancel)

            else:
                break

        else:
            print("No repair order available for modification")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break

#-----------------------------------------customer order status---------------------------------------------------------
def inquiry_order_status():
    from datetime import datetime
    cus_id = login_id
    repair_service_record = data_sort_out(file_name="service&repair order status.txt")
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d-%m-%Y")
    repair_record = list()
    for record in range(1, len(repair_service_record)):
        if repair_service_record[record][1] == cus_id and (repair_service_record[record][2].upper() == "DESKTOP REPAIR"
                                                           or repair_service_record[record][
                                                               2].upper() == "LAPTOP REPAIR"):
            repair_record.append(repair_service_record[record])
    print("    Repair status Interface    ")
    while True:
        print("_______________________________")
        print("Please select:")
        print("a) '1' - Current repair order")
        print("b) '2' - Upcoming repair order")
        print("_______________________________")
        print("* Please enter '3' for returning to menu")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2" and decision != "3":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            current_repair = list()
            for i in range(len(repair_record)):
                repair = list()
                record = False
                if repair_record[i][3] < current_date:
                    date = repair_record[i][3]
                    year = int(date[6:])
                    month = int(date[3:5])
                    day = int(date[0:2])
                    date1 = datetime(year, month, day)
                    current_year = int(current_date[6:])
                    current_month = int(current_date[3:5])
                    current_day = int(current_date[0:2])
                    date2 = datetime(current_year, current_month, current_day)
                    difference = date2 - date1
                    if difference.days == 3:
                        repair_status = "Repaired"
                        repair.insert(3, repair_status)
                        record = True
                    elif difference.days < 3:
                        repair_status = "Repairing"
                        repair.insert(3, repair_status)
                        record = True
                elif repair_record[i][3] == current_date:
                    repair_status = "Pending"
                    repair.insert(3, repair_status)
                    record = True
                if record:
                    repair.insert(0, repair_record[i][0])
                    repair.insert(1, repair_record[i][2])
                    repair.insert(2, repair_record[i][3])
                    repair.insert(4, repair_record[i][-1])
                    current_repair.append(repair)
            if len(current_repair) == 0:
                print("There is no current repair order...")
                continue
            print("                           Current Repair Order                               ")
            print("______________________________________________________________________________")
            title = ["Order ID", "Repair Type", "Date", "Status", "Payment Status"]
            table_view(headers=title, data=current_repair, column_size=14, data_size=14)
            print("______________________________________________________________________________")
            previous_page = input("Please enter 'Back' for returning to previous page: ")
            while previous_page != "Back":
                print("Invalid option...")
                previous_page = input("Please enter 'Back' for returning to previous page: ")
        elif decision == "2":
            upcoming_repair = list()
            for i in range(len(repair_record)):
                upcoming_record = list()
                if repair_record[i][3] > current_date:
                    date = repair_record[i][3]
                    year = int(date[6:])
                    month = int(date[3:5])
                    day = int(date[0:2])
                    upcoming_date = datetime(year, month, day)
                    print(upcoming_date)
                    upcoming_record.insert(0, repair_record[i][0])
                    upcoming_record.insert(1, repair_record[i][2])
                    upcoming_record.insert(2, upcoming_date.strftime("%Y-%m-%d"))
                    upcoming_record.insert(3, repair_record[i][-1])
                    upcoming_repair.append(upcoming_record)
                else:
                    continue
            if len(upcoming_repair) == 0:
                print("There is no upcoming repair order...")
                continue
            print("                  Upcoming Repair Record                     ")
            print("_____________________________________________________________")
            title = ["Order ID", "Repair Type", "Date", "Payment Status"]
            table_view(headers=title, data=upcoming_repair, column_size=14, data_size=14)
            print("_____________________________________________________________")
            previous_page = input("Please enter 'Back' for returning to previous page: ")
            while previous_page != "Back":
                print("Invalid option...")
                previous_page = input("Please enter 'Back' for returning to previous page: ")

        else:
            print("Returning to menu...")
            break
#-----------------------------------------Customer Report----------------------------------------------------------------
def repair_or_service(order_type, record_file, user_id, cus_info):
    order_list = list()
    for record in range(1, len(record_file)):
        if record_file[record][1] == user_id and record_file[record][-1].upper() == "PAYMENT COMPLETED" \
                and record_file[record][2].__contains__(order_type):
            record_list = list()
            record_list.insert(0, record_file[record][0])
            record_list.insert(1, record_file[record][2])
            record_list.insert(2, record_file[record][3])
            record_list.insert(3, record_file[record][4])
            order_list.append(record_list)
    print("                       Item Purchase Report                        ")
    print("_____________________________________________________________________")
    print("Name: ", cus_info[1], "           ", "IC/Passport: ", cus_info[2])
    print("ID Number: ", cus_info[0], "           ", "City of Domicile: ", cus_info[4])
    print("Phone Number: ", cus_info[3])
    print(" ")
    print("----------------------------------------------------------------------")
    title = ["Order ID", "Description", "Repair Date", "Order Date"]
    table_view(headers=title, data=order_list, column_size=15, data_size=15)
    print("----------------------------------------------------------------------")
    print("______________________________________________________________________")
    previous_page = input("Please enter 'Back' for returning to previous page: ")
    while previous_page != "Back":
        print("Invalid option...")
        previous_page = input("Please enter 'Back' for returning to previous page: ")


def cus_report():
    purchase_order = data_sort_out(file_name="purchase order status.txt")
    service_and_repair = data_sort_out(file_name="service&repair order status.txt")
    cus_data = data_sort_out(file_name="Customer data.txt")
    cus_id = login_id
    while True:
        print("Customer Report Interface")
        print("_________________________")
        print("Please select: ")
        print("a) '1' - Purchase report")
        print("b) '2' - Repair report")
        print("c) '3' - Service report")
        print("_________________________")
        print("* Please enter '4' for returning to menu")
        report_type = input("Please enter the number: ")
        while report_type != "1" and report_type != "2" and report_type != "3" and report_type != "4":
            print("Invalid option...")
            report_type = input("Please enter the number: ")
        cus_info = list()
        for info in range(len(cus_data)):
            if cus_data[info][0] == cus_id:
                cus_info.extend(cus_data[info])
        if report_type == "1":
            purchase_record = list()
            for record in range(1, len(purchase_order)):
                if purchase_order[record][0] == cus_id and purchase_order[record][-1].upper() == "PAYMENT COMPLETED":
                    purchase_list = [purchase_order[record][1],purchase_order[record][2],purchase_order[record][3],purchase_order[record][4],purchase_order[record][7]]
                    purchase_record.append(purchase_list)
            if len(purchase_record) == 0:
                print("User have no purchase order record....")
                print("Return to user menu...")
                continue

            print("                       Item Purchase Report                        ")
            print("_____________________________________________________________________")
            print("Name: ", cus_info[1], "           ", "IC/Passport: ", cus_info[2])
            print("ID Number: ", cus_info[0], "           ", "City of Domicile: ", cus_info[4])
            print("Phone Number: ", cus_info[3])
            print(" ")
            print("----------------------------------------------------------------------")
            title = ["Item ID", "Name", "Quantity", "Price", "Order Date"]
            table_view(headers=title, data=purchase_record, column_size=14, data_size=14)
            print("----------------------------------------------------------------------")
            print("______________________________________________________________________")
            previous_page = input("Please enter 'Back' for returning to previous page: ")
            while previous_page != "Back":
                print("Invalid option...")
                previous_page = input("Please enter 'Back' for returning to previous page: ")
        elif report_type == "2":
            repair_or_service(order_type="Repair", record_file=service_and_repair, user_id=cus_id, cus_info=cus_info)
        elif report_type == "3":
            repair_or_service(order_type="Service", record_file=service_and_repair, user_id=cus_id, cus_info=cus_info)
        elif report_type == "4":
            print("Returning to menu...")
            break
#-----------------------------------------Customer menu----------------------------------------------------------------

def customer_menu ():
    menu = input ("""a. '1'- Place Purchase Order
b. '2'- Place Service/Repair Order
c. '3'- Modify Purchase Order
d. '4'- Modify Service/Repair Order
e. '5'- Purchase Order Status
f. '6'- Order Report
e. '7'- Return
Please enter:""")
    while menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5" and menu != "6" and menu != "7":
        menu = input("""a. '1'- Place Purchase Order
b. '2'- Place Service/Repair Order
c. '3'- Modify Purchase Order
d. '4'- Modify Service/Repair Order
e. '5'- Return
Please enter:""")
    return menu


# Superuser inteface
def user_brief_info(user_record):
    user_list = list()
    for user in range(len(user_record)):
        approved_user = list()
        if user_record[user][-1].upper() == "APPROVED":
            approved_user.insert(0, user_record[user][0])
            approved_user.insert(1, user_record[user][1])
            approved_user.insert(2, user_record[user][-1])
            user_list.append(approved_user)
    return user_list


def user_id(user_id_number):
    id_num = list()
    for i in range(len(user_id_number)):
        id_num.append(user_id_number[i][0])
    return id_num


#  User update and registration approval
def user_update(user_data):
    register = False
    print("  User Update Interface  ")
    while True:
        user_record = data_sort_out(file_name=user_data)
        id_list = list()
        for index in range(len(user_record)):
            id_list.append(user_record[index][0])
        print("__________________________")
        user_id = input("Please enter the staff id: ")
        while len(user_id) == 0:
            user_id = input("Please enter the staff id: ")
        while (user_id[0] + user_id[1]) != "TP":
            print("ID Number must consist 'TP' in front")
            print("Sample: TP123456")
            user_id = input("Please enter the staff id: ")
        while len(user_id[2:len(user_id)]) != 6:
            print("Number after 'TP' must have 6 numbers")
            user_id = input("Please enter the staff id: ")
        if user_id in id_list:
            print(f"The staff id ({user_id}) has been registered.")
        else:
            user_name = input("Please enter the staff name: ")
            while len(user_name) == 0:
                user_name = input("Please enter the staff name: ")
            print("__________________________________")
            print("Please select:")
            print("a) '1' - Complete user update")
            print("b) '2' - Enter information again")
            print("__________________________________")
            decision = input("Please enter: ")
            while decision != "1" and decision != "2":
                print("Invalid option...")
                decision = input("Please enter: ")
            if decision == "1":
                with open(user_data, "a+") as user_information:
                    user_information.writelines(user_id + "," + user_name + "," + "Approved" + "\n")
                print("Staff update successfully!!!")
                user_activities(user_id=login_id, identity=staff_identity, activities="Update user", description=user_id)

                print("__________________________________")
                print("Do you want update another user ?: ")
                print("a) '1' - Yes")
                print("b) '2' - 'No'")
                print("__________________________________")
                continue_update = input("Please enter: ")
                while continue_update != "1" and continue_update != "2":
                    print("Invalid option...")
                    continue_update = input("Please enter: ")
                if continue_update == "1":
                    continue
                else:
                    print("Returning to main interface...")
                    register = True  # need to add an options to choose for back to previous page

            else:
                continue
        if register:
            break


def registration_approval(filename):
    while True:
        user_record = data_sort_out(file_name=filename)
        unapproved_user = list()
        for i in range(len(user_record)):
            if user_record[i][-1].upper() == "UNAPPROVED":
                unapproved_user.append(user_record[i])
        if len(unapproved_user) == 0:
            print("There is no registration request for approval.")
            print("Please return to the main interface.")
            break
        title = ["ID Number", "Name", "status"]
        print("____________________________________________________")
        table_view(headers=title, data=unapproved_user, column_size=20, data_size=20)
        print("____________________________________________________")
        print("   ")
        register_approved = False
        while True:
            staff_id = input("Please enter the staff ID for approving the registration: ")
            if len(staff_id) == 0:
                continue
            for id in range(len(user_record)):
                if staff_id == user_record[id][0]:
                    print("Registration approve!!!")
                    print("Staff will be informed for activating the account")
                    user_record[id][-1] = "Approved"
                    with open(filename, "w") as staff_record:
                        for index in range(len(user_record)):
                            if len(user_record[index]) == 3:
                                staff_record.writelines(user_record[index][0] + "," + user_record[index][1] + ","
                                                        + user_record[index][2] + "\n")
                            elif len(user_record[index]) == 4:
                                staff_record.writelines(user_record[index][0] + "," + user_record[index][1] + ","
                                                        + user_record[index][2] + "," +  user_record[index][3] + "\n")
                    register_approved = True
                    user_activities(user_id=login_id, identity=staff_identity,
                                    activities=f"Registration {user_record[id][-1].lower()}", description=staff_id)
                    break
            if register_approved:
                break
            print("Invalid staff ID!!!")
        print("_________________________________________________")
        print("Do you want to approve another registration ?:")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("_________________________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option....")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to main interface...")
            break


def add_user():
    while True:
        print("User update and registration approval")
        print("_____________________________________")
        print("Please select: ")
        print("a) '1' - User Update")
        print("b) '2' - User Registration Approval")
        print("_____________________________________")
        print("* Please enter '3' for returning to user menu.")
        options = input("Please enter the number: ")
        while options != "1" and options != "2" and options != "3":
            print("Invalid option...")
            options = input("Please enter the number: ")
        if options == "1":
            print("  User Update Interface  ")
            print("_________________________")
            print("Please select: ")
            print("a) '1' - Admin")
            print("b) '2' - Inventory staff")
            print("_________________________")
            user_type = input("Please enter the number: ")
            while user_type != "1" and user_type != "2":
                print("Invalid option....")
                user_type = input("Please enter the number: ")
            if user_type == "1":
                user_update(user_data="admin data.txt")
            else:
                user_update(user_data="staff info.txt")
        if options == "2":
            print("Registration Approval Interface")
            print("_______________________________")
            print("Please select: ")
            print("a) '1' - Admin")
            print("b) '2' - Inventory staff")
            print("_______________________________")
            user_type = input("Please enter the number: ")
            while user_type != "1" and user_type != "2":
                print("Invalid option....")
                user_type = input("Please enter the number: ")
            if user_type == "1":
                registration_approval(filename="admin data.txt")
            else:
                registration_approval(filename="staff info.txt")
        else:
            print("Returning to user menu...")
            break

# New customer verification


def new_customer_verification():
    while True:
        print("            New Customer verification          ")
        customer_record = data_sort_out(file_name="Customer data.txt")
        unapproved_customer = list()
        for data in range(len(customer_record)):
            new_customer = list()
            if customer_record[data][-1].upper() == "UNAPPROVED" and len(customer_record[data]) == 6:
                new_customer.insert(0, customer_record[data][0])
                new_customer.insert(1, customer_record[data][1])
                new_customer.insert(2, customer_record[data][-1])
                unapproved_customer.append(new_customer)
        if len(unapproved_customer) == 0:
            print("There are no new customer....")
            break
        IC_number = list()
        for ic_num in range(len(unapproved_customer)):
            IC_number.append(unapproved_customer[ic_num][1])
        title = ["Name", "IC/Passport Number", "Status"]
        print("____________________________________________________")
        table_view(headers=title, data=unapproved_customer, column_size=20, data_size=20)
        print("____________________________________________________")
        specific_customer = input("Please enter the IC/Passport number of new customer for verification: ")
        while len(specific_customer) == 0:
            print("Please enter new customer Identity number!!!")
            specific_customer = input("Please enter the IC/Passport number of new customer for verification: ")
        while specific_customer not in IC_number:
            print("Invalid Identity number!!!")
            specific_customer = input("Please enter the IC/Passport number of new customer for verification: ")
        for i in range(len(customer_record)):
            if len(customer_record[i]) == 6:
                if specific_customer == customer_record[i][1]:
                    print("   Customer Registration Information    ")
                    print("________________________________________")
                    print("Customer Name: ", customer_record[i][0])
                    print("IC/Passport Number: ", customer_record[i][1])
                    print("Phone Number: ", customer_record[i][2])
                    print("State: ", customer_record[i][3])
                    print("Date of Registration: ", customer_record[i][4])
                    print("Status: ", customer_record[i][5])
                    print("________________________________________")
                    print(" ")
                    print("________________________________________")
                    print("Approve new customer registration? :")
                    print("a) '1' - Approve")
                    print("b) '2' - Unapproved")
                    print("________________________________________")
                    approval = input("Please enter the number: ")
                    while approval != "1" and approval != "2":
                        print("Invalid option...")
                        approval = input("Please enter the number: ")
                    if approval == "1":
                        print("Customer registration approved.")
                        print("Customer will be informed for activating the account.")
                        customer_record[i][-1] = "Approved"
                        with open("Customer data.txt", "w") as customer_data:
                            for length in range(len(customer_record)):
                                if len(customer_record[length]) == 6:
                                    customer_data.writelines(
                                        customer_record[length][0] + "," + customer_record[length][1] + ","
                                        + customer_record[length][2] + "," + customer_record[length][3] + ","
                                        + customer_record[length][4] + "," + customer_record[length][5] + "\n"
                                    )
                                elif len(customer_record[length]) == 8:
                                    customer_data.writelines(
                                        customer_record[length][0] + "," + customer_record[length][1] + ","
                                        + customer_record[length][2] + "," + customer_record[length][3] + ","
                                        + customer_record[length][4] + "," + customer_record[length][5] + ","
                                        + customer_record[length][6] + "," + customer_record[length][7] + "\n"
                                    )
                        user_activities(user_id=login_id, identity=staff_identity,
                                        activities="approved customer registration", description=specific_customer)
            else:
                continue
        print("_____________________________________________")
        print("Do you want to verify another new customer? :")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("_____________________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to main interface...")
            break


# modify user personal details
def user_detail_modify():
    while True:
        print("_________________________________")
        print("User personal detail modification")
        print("_________________________________")
        customer_record = data_sort_out(file_name="Customer data.txt")
        customer_data = list()
        id_list = list()
        for user in range(len(customer_record)):
            if (customer_record[user][-1].upper() == "APPROVED" and len(customer_record[user]) == 8) \
                    or len(customer_record[user]) == 8:
                user_data = list()
                user_data.insert(0, customer_record[user][0])
                user_data.insert(1, customer_record[user][1])
                user_data.insert(2, customer_record[user][-1])
                customer_data.append(user_data)
                id_list.append(customer_record[user][0])
        print("__________________________________________________")
        title = ["ID Number", "Name", "Status"]
        table_view(headers=title, data=customer_data, column_size=20, data_size=20)
        print("__________________________________________________")
        customer_id = input("Please enter the customer ID: ")
        while len(customer_id) == 0:
            customer_id = input("Please enter the customer ID: ")
        while customer_id not in id_list:
            print("Invalid Customer ID")
            customer_id = input("Please enter the customer ID: ")
        previous_page = False
        main_interface = False
        for index in range(len(customer_record)):
            if customer_id == customer_record[index][0]:
                while True:
                    print("              Customer personal Details                  ")
                    print("______________________________________________________")
                    print("Identity Number: ", customer_record[index][0])
                    print("Name: ", customer_record[index][1])
                    print("IC/Passport Number: ", customer_record[index][2])
                    print("Phone Number: ", customer_record[index][3])
                    print("State: ", customer_record[index][4])
                    print("Registration Date: ", customer_record[index][5])
                    print("Status: ", customer_record[index][7])
                    print("______________________________________________________")

                    print("______________________________________________________")
                    print("Please select one user detail to modify: ")
                    print("a) '1' - Identity Number        b) '2' - Customer Name")
                    print("c) '3' - Phone Number           d) '4' - State")
                    print("______________________________________________________")
                    user_detail = input("Please enter the number: ")
                    while user_detail != "1" and user_detail != "2" and user_detail != "3" and user_detail != "4":
                        print("Invalid option...")
                        user_detail = input("Please enter the number: ")
                    if user_detail == "1":
                        print("Current Identity Number: ", customer_record[index][0])
                        new_id = input("Please enter the new Identity Number: ")
                        while list(new_id)[0] + list(new_id)[1] != "TP":
                            print("Please consist 'TP' for customer new ID Number")
                            new_id = input("Please enter the new Identity Number: ")
                        customer_record[index][0] = new_id
                        user_activities(user_id=login_id, identity=staff_identity,
                                        activities="modify customer ID", description=customer_id)
                        print("Customer details modified successfully!!!")
                    elif user_detail == "2":
                        print("Current Name: ", customer_record[index][1])
                        new_name = input("Please enter the new customer name: ")
                        customer_record[index][1] = new_name
                        user_activities(user_id=login_id, identity=staff_identity,
                                        activities="modify customer name", description=customer_id)
                        print("Customer details modified successfully!!!")
                    elif user_detail == "3":
                        print("Current Phone Number: ", customer_record[index][3])
                        new_phone_num = input("Please enter the new phone number: ")
                        customer_record[index][3] = new_phone_num
                        user_activities(user_id=login_id, identity=staff_identity,
                                        activities="modify customer phone number", description=customer_id)
                        print("Customer details modified successfully!!!")
                    else:
                        print("Current State: ", customer_record[index][4])
                        new_state = input("Please enter the new state: ")
                        customer_record[index][4] = new_state
                        user_activities(user_id=login_id, identity=staff_identity,
                                        activities="modify customer city", description=customer_id)
                        print("Customer details modified successfully!!!")
                    with open("Customer data.txt", "w") as customer_account:
                        for i in range(len(customer_record)):
                            if len(customer_record[i]) == 8:
                                customer_account.writelines(customer_record[i][0] + "," + customer_record[i][1] + ","
                                                            + customer_record[i][2] + "," + customer_record[i][3] + ","
                                                            + customer_record[i][4] + "," + customer_record[i][5] + ","
                                                            + customer_record[i][6] + "," + customer_record[i][7] + "\n"
                                                            )
                            elif len(customer_record[i]) == 6:
                                customer_account.writelines(customer_record[i][0] + "," + customer_record[i][1] + ","
                                                            + customer_record[i][2] + "," + customer_record[i][3] + ","
                                                            + customer_record[i][4] + "," + customer_record[i][5] + ","
                                                            + "\n"
                                                            )

                    print("_______________________________________")
                    print("Please select: ")
                    print("a) '1' - modify customer details")
                    print("b) '2' - switch customer")
                    print("c) '3' - Return back to user menu")
                    print("_______________________________________")
                    decision = input("Please enter the number: ")
                    while decision != "1" and decision != "2" and decision != "3":
                        print("Invalid option...")
                        decision = input("Please enter the number: ")
                    if decision == "1":
                        continue
                    elif decision == "2":
                        previous_page = True
                        break
                    else:
                        print("Returning to main interface")
                        main_interface = True
                        break

            else:
                continue
        if previous_page:
            continue
        elif main_interface:
            break


#  Disable user access
def cus_disable_access():
    customer_record = data_sort_out(file_name="Customer data.txt")
    customer_list = list()
    for x in range(len(customer_record)):
        if len(customer_record[x]) == 8:
            approved_user = list()
            if customer_record[x][-1].upper() == "APPROVED":
                approved_user.insert(0, customer_record[x][0])
                approved_user.insert(1, customer_record[x][1])
                approved_user.insert(2, customer_record[x][-1])
                customer_list.append(approved_user)
    customer_id = list()
    for x in range(len(customer_record)):
        if len(customer_record[x]) == 8:
            customer_id.append(customer_record[x][0])
    title = ["ID Number", "Name", "Status"]
    print("             Customer information table             ")
    print("____________________________________________________")
    table_view(headers=title, data=customer_list, column_size=20, data_size=20)
    print("____________________________________________________")
    cus_id = input("Please enter the customer id for disabling access: ")
    while cus_id not in customer_id:
        print("Invalid customer ID")
        cus_id = input("Please enter the customer id for disabling access: ")
    for i in range(len(customer_record)):
        if len(customer_record[i]) == 8:
            if customer_record[i][0] == cus_id:
                print("              Customer personal Details                  ")
                print("______________________________________________________")
                print("Identity Number: ", customer_record[i][0])
                print("Name: ", customer_record[i][1])
                print("IC/Passport Number: ", customer_record[i][2])
                print("Phone Number: ", customer_record[i][3])
                print("State: ", customer_record[i][4])
                print("Registration Date: ", customer_record[i][5])
                print("Status: ", customer_record[i][7])
                print("______________________________________________________")

                print("___________________________________________________________")
                print(f"Do you want to disable the access of this user ({customer_record[i][0]}):")
                print("a) Yes")
                print("b) No")
                print("____________________________________________________________")
                decision = input("Please enter: ")
                while decision.upper() != "YES" and decision.upper() != "NO":
                    print("Invalid option!!!")
                    decision = input("Please enter: ")
                if decision.upper() == "YES":
                    customer_record[i][-1] = "Unapproved"
                    with open("Customer data.txt", "w") as customer_data:
                        for length in range(len(customer_record)):
                            if len(customer_record[length]) == 6:
                                customer_data.writelines(
                                    customer_record[length][0] + "," + customer_record[length][1] + ","
                                    + customer_record[length][2] + "," + customer_record[length][3] + ","
                                    + customer_record[length][4] + "," + customer_record[length][5] + "\n"
                                )
                            elif len(customer_record[length]) == 8:
                                customer_data.writelines(
                                    customer_record[length][0] + "," + customer_record[length][1] + ","
                                    + customer_record[length][2] + "," + customer_record[length][3] + ","
                                    + customer_record[length][4] + "," + customer_record[length][5] + ","
                                    + customer_record[length][6] + "," + customer_record[length][7] + "\n"
                                )
                    print("Status modified successfully!!!")
                    print("User will no longer can login the account")
                    user_activities(user_id=login_id, identity=staff_identity,
                                    activities="disable customer access", description=cus_id)
                else:
                    print("Customer will continue to log in the account....")
                    break
        else:
            continue


def user_disable_access(user_data):
    user_record = data_sort_out(file_name=user_data)
    user_list = user_brief_info(user_record=user_record)
    staff_id = user_id(user_id_number=user_list)
    title = ["ID Number", "Name", "Status"]
    print("             User information table              ")
    print("__________________________________________________")
    table_view(headers=title, data=user_list, column_size=20, data_size=20)
    print("__________________________________________________")
    id_input = input("Please enter admin ID number: ")
    while id_input not in staff_id:
        print("Invalid ID")
        id_input = input("Please enter admin ID number: ")
    for i in range(len(user_record)):
        if user_record[i][0] == id_input:
            print("       staff information        ")
            print("________________________________")
            print("ID Number: ", user_record[i][0])
            print("Name: ", user_record[i][1])
            print("________________________________")
            decision = input("Are you confirm to disable this admin access? (Yes/No) :")
            while decision.upper() != "YES" and decision.upper() != "NO":
                print("Invalid option")
                decision = input("Are you confirm to disable this admin access? (Yes/No) :")
            if decision.upper() == "YES":
                user_record[i][-1] = "Unapproved"
                with open(user_data, "w") as admin_data:
                    for length in range(len(user_record)):
                        if len(user_record[length]) == 3:
                            admin_data.writelines(user_record[length][0] + "," + user_record[length][1] + ","
                                                  + user_record[length][2] + "\n")
                        elif len(user_record[length]) == 4:
                            admin_data.writelines(user_record[length][0] + "," + user_record[length][1] + ","
                                                  + user_record[length][2] + "," + user_record[length][3]+ "\n")
                print("Access disable successfully!!!")
                user_activities(user_id=login_id, identity=staff_identity,
                                activities="disable user access", description=id_input)
            else:
                print("Admin will continue to log in the account....")
                break
        else:
            continue


def user_access_disable():
    while True:
        print("User access disablement")
        print("_________________________")
        print("User type: ")
        print("a) '1' - Customer")
        print("b) '2' - Admin")
        print("c) '3' - Inventory staff")
        print("_________________________")
        user_type = input("Please enter the user type: ")
        while user_type != "1" and user_type != "2" and user_type != "3":
            print("Invalid option")
            user_type = input("Please enter the user type: ")
        while True:
            if user_type == "1":
                cus_disable_access()
            elif user_type == "2":
                user_disable_access(user_data="admin data.txt")
            else:
                user_disable_access(user_data="staff info.txt")
            print("_______________________________")
            print(" Disable another user access? :")
            print(" a) '1' - Yes")
            print(" b) '2' - No")
            print("_______________________________")
            option = input("Please enter the number: ")
            while option != "1" and option != "2":
                print("Invalid option...")
                option = input("Please enter the number: ")
            if option == "1":
                continue
            else:
                break
        print("_________________________________")
        print("Please select: ")
        print("a) '1' - Switch User")
        print("b) '2' - Return to user menu")
        print("_________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            break


# user's system usage
def login_history(filename, user_type):
    Login_data = data_sort_out(file_name=filename)
    user_login = list()
    for i in range(len(Login_data)):  # sort out the customer login data
        if Login_data[i][-1].upper() in user_type and Login_data[i][3].upper() == "LOG IN":
            user_login.append(Login_data[i])
    login_date = list()
    for x in range(len(user_login)):  # sort out available login date
        if user_login[x][-1].upper() in user_type and Login_data[x][3].upper() == "LOG IN":
            if user_login[x][1] not in login_date:
                date = user_login[x][1]
                login_date.append(date)
        else:
            continue
    for data in range(len(login_date)):  # sort out table view data
        system_inquiry = list()
        for customer in range(len(user_login)):
            cus_data = list()
            if login_date[data] == user_login[customer][1]:
                cus_data.insert(0, user_login[customer][0])
                cus_data.insert(1, user_login[customer][2])
                cus_data.insert(2, user_login[customer][-1])
                system_inquiry.append(cus_data)
        title = ["ID Number", "Time", "User Type"]
        print("Date: ", login_date[data])
        print("                       Login History                     ")
        print("_________________________________________________________")
        table_view(headers=title, data=system_inquiry, column_size=20, data_size=20)
        # display the information of user login
        print("_________________________________________________________")


def system_usage_inquiry():
    while True:
        print("Welcome to User's System usage inquiry")
        print("______________________________________")
        print("Please select the options: ")
        print("a) '1' - Customer")
        print("b) '2' - Staff")
        print("c) '3' - User Menu")
        print("______________________________________")
        options = input("Please enter the number: ")
        while options != "1" and options != "2" and options != "3":
            print("Invalid option...")
            options = input("Please enter the number: ")
        if options == "1":
            login_history(filename="Login datetime.txt", user_type=["CUSTOMER"])
            user_activities(user_id=login_id, identity=staff_identity,
                            activities="check customer login ", description="-")
        elif options == "2":
            login_history(filename="Login datetime.txt", user_type=["ADMIN", "SUPER USER", "INVENTORY STAFF"])
            user_activities(user_id=login_id, identity=staff_identity,
                            activities="check user login", description="-")
        else:
            print("Returning to main interface...")
            break
        print("  ")
        back = input("Please enter 'Back' for returning to previous page: ")
        while back == " ":
            print("Invalid option!!!")
            back = input("Please enter 'Back' for returning to previous page: ")
        while back.upper() != "BACK":
            print("Invalid option!!!")
            back = input("Please enter 'Back' for returning to previous page: ")


#  customer order status
def num_of_order(purchase_order_data, cus_data, cus_paid_id):
    order_brief_info = list()
    for i in range(len(cus_paid_id)):
        cus_order_info = list()
        order_num = 0
        for orders in range(len(purchase_order_data)):
            if cus_paid_id[i] == purchase_order_data[orders][0] \
                    and purchase_order_data[orders][-1].upper() == "PAYMENT COMPLETED":
                order_num += 1
            else:
                continue
        for name in range(len(cus_data)):
            if cus_data[name][0] == cus_paid_id[i]:
                cus_order_info.insert(1, cus_data[name][1])
            else:
                continue
        cus_order_info.insert(0, cus_paid_id[i])
        cus_order_info.insert(2, order_num)
        order_brief_info.append(cus_order_info)
    title = ["ID Number", "Customer Name", "Number of Orders"]
    print("__________________________________________________________")
    table_view(headers=title, data=order_brief_info, column_size=20, data_size=20)
    print("__________________________________________________________")


def purchase_order_info(purchase_order_data, cus_data, cus_paid_id):
    order_info = input("Please enter the ID Number for further order information: ")
    while order_info not in cus_paid_id:
        print("Invalid Customer ID....")
        order_info = input("Please enter the ID Number for further order information: ")
    while True:
        items_order = list()
        attempt = 0
        for i in range(len(purchase_order_data)):
            purchase_record = list()
            if purchase_order_data[i][0] == order_info and purchase_order_data[i][-1].upper() == "PAYMENT COMPLETED":
                attempt += 1
                purchase_record.insert(0, attempt)
                purchase_record.insert(1, purchase_order_data[i][1])
                purchase_record.insert(2, purchase_order_data[i][2])
                purchase_record.insert(3, purchase_order_data[i][3])
                unit_price = round(float(purchase_order_data[i][4]) / float(purchase_order_data[i][3]))
                purchase_record.insert(4, unit_price)
                purchase_record.insert(5, purchase_order_data[i][5])
                purchase_record.insert(6, purchase_order_data[i][-1])
                items_order.append(purchase_record)
        for name in range(len(cus_data)):
            if cus_data[name][0] == order_info:
                cus_name = cus_data[name][1]
            else:
                continue
        print("Customer Name:", cus_name)
        print("ID Number: ", order_info)
        print("__________________________________________________________________________"
            "_______________________________________")
        title = ["No.", "Item ID", "Name", "Quantity", "Price per unit", "Order Date", "Status"]
        table_view(headers=title, data=items_order, column_size=15, data_size=15)
        print("______________________________________________________________"
              "___________________________________________________")
        order_detail = int(input("Please enter the number on the 'No.' for detailed information: "))
        while order_detail > len(items_order):
            print("Invalid option....")
            order_detail = int(input("Please enter the number on the 'No.' for detailed information: "))
        print("Generating purchase order information.....")
        purchase_order_list = list()
        for x in range(1, len(purchase_order_data)):
            if purchase_order_data[x][0] == order_info and purchase_order_data[x][-1].upper() == "PAYMENT COMPLETED":
                purchase_order_list.append(purchase_order_data[x])
        print("_______________________________________________________________________________")
        print("                         Purchase Order Information                            ")
        print("Customer Name: ", cus_name, "          ", "Purchase Date: ", purchase_order_list[order_detail - 1][7])
        print("ID Number: ", order_info, "                     ", "Purchase Time: ",
              purchase_order_list[order_detail - 1][8])
        print(" ")
        print("Product ID Number: ", purchase_order_list[order_detail - 1][1])
        print("Product Name:", purchase_order_list[order_detail - 1][2])
        print("Quantity: ", purchase_order_list[order_detail - 1][3])
        print("Total Price: RM", purchase_order_list[order_detail - 1][4])
        print("Payment Status: ", purchase_order_list[order_detail - 1][-1])
        print("_______________________________________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity,
                        activities="check customer purchase order", description=order_info)
        print(" ")
        print("________________________________________")
        print("Continue for other purchase order detail? : ")
        print(" a) '1' - Yes")
        print(" b) '2' - No")
        print("________________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            break


def unpaid_order(purchase_order_data, cus_data, cus_unpaid_id):
    unpaid_order = list()
    for i in range(len(cus_unpaid_id)):
        unpaid_info = list()
        unpaid_num = 0
        for unpaid in range(len(purchase_order_data)):
            if cus_unpaid_id[i] == purchase_order_data[unpaid][0] \
                    and purchase_order_data[unpaid][-1].upper() == "PAYMENT INCOMPLETE":
                unpaid_num += 1
            else:
                continue
        for name in range(len(cus_data)):
            if cus_unpaid_id[i] == cus_data[name][0]:
                unpaid_info.insert(1, cus_data[name][1])
            else:
                continue
        unpaid_info.insert(0, cus_unpaid_id[i])
        unpaid_info.insert(2, unpaid_num)
        unpaid_order.append(unpaid_info)
    title = ["ID Number", "Customer Name", "Number of unpaid order"]
    print("________________________________________________________________")
    table_view(headers=title, data=unpaid_order, column_size=20, data_size=20)
    print("________________________________________________________________")


def unpaid_order_info(purchase_order_data, cus_data, cus_unpaid_id):
    cus_id = input("Please enter the ID Number for further unpaid order information: ")
    while cus_id not in cus_unpaid_id:
        print("Invalid ID Number....")
        cus_id = input("Please enter the ID Number for further unpaid order information: ")
    order_unpaid = list()
    attempt = 0
    for i in range(1, len(purchase_order_data)):
        unpaid_info = list()
        if purchase_order_data[i][0] == cus_id and purchase_order_data[i][-1].upper() == "PAYMENT INCOMPLETE":
            attempt += 1
            unpaid_info.insert(0, attempt)
            unpaid_info.insert(1, purchase_order_data[i][1])
            unpaid_info.insert(2, purchase_order_data[i][2])
            unpaid_info.insert(3, purchase_order_data[i][3])
            unpaid_info.insert(4, purchase_order_data[i][5])
            unpaid_info.insert(5, purchase_order_data[i][-1])
            order_unpaid.append(unpaid_info)
    for name in range(len(cus_data)):
        if cus_data[name][0] == cus_id:
            cus_name = cus_data[name][1]
        else:
            continue
    print("Customer Name: ", cus_name)
    print("ID Number: ", cus_id)
    print("___________________________________________________________________________________")
    title = ["No.", "Item ID", "Item Name", "Quantity", "Order Date", "Status"]
    table_view(headers=title, data=order_unpaid, column_size=12, data_size=12)
    print("___________________________________________________________________________________")
    user_activities(user_id=login_id, identity=staff_identity,
                    activities="check customer unpaid order", description=cus_id)


def customer_order_Status():
    while True:
        print("Customer Order status")
        print("_________________________________")
        print("Please select: ")
        print("a) '1' - Complete Payment")
        print("b) '2' - Incomplete Payment")
        print("c) '3' - Return to menu interface")
        print("_________________________________")
        options = input("Please enter the number:")
        while options != "1" and options != "2" and options != "3":
            print("Invalid option")
            options = input("Please enter the number:")
        if options == "3":
            print("Returning to menu interface")
            break
        purchase_order_data = data_sort_out(file_name="purchase order status.txt")
        cus_paid_id = list()
        cus_unpaid_id = list()
        for id in range(1, len(purchase_order_data)):
            if purchase_order_data[id][-1].upper() == "PAYMENT COMPLETED":
                if purchase_order_data[id][0] not in cus_paid_id:
                    cus_paid_id.append(purchase_order_data[id][0])
            elif purchase_order_data[id][-1].upper() == "PAYMENT INCOMPLETE":
                if purchase_order_data[id][0] not in cus_unpaid_id:
                    cus_unpaid_id.append(purchase_order_data[id][0])
            else:
                continue
        cus_data = data_sort_out(file_name="Customer data.txt")
        while True:
            if options == "1":
                num_of_order(purchase_order_data=purchase_order_data, cus_paid_id=cus_paid_id, cus_data=cus_data)
                purchase_order_info(purchase_order_data=purchase_order_data, cus_paid_id=cus_paid_id, cus_data=cus_data)
            else:
                unpaid_order(purchase_order_data=purchase_order_data, cus_unpaid_id=cus_unpaid_id, cus_data=cus_data)
                unpaid_order_info(purchase_order_data=purchase_order_data,
                              cus_unpaid_id=cus_unpaid_id, cus_data=cus_data)
            print("_________________________________________")
            print("Please select: ")
            print("a) '1' - Other customer order information")
            print("b) '2' - Return to main interface")
            print("_________________________________________")
            decision = input("Please enter the number: ")
            while decision != "1" and decision != "2":
                print("Invalid option")
                decision = input("Please enter the number: ")
            if decision == "1":
                continue
            else:
                break

# inventory purchase order approval
def purchase_order_approval(supplier, order_record, user_id):
    staff_info = data_sort_out(file_name="staff info.txt")
    purchase_order = list()
    purchase_id = list()
    for record in range(len(order_record)):
        if order_record[record][1] == user_id and order_record[record][2] == supplier:
            record_list = list()
            record_list.insert(0, order_record[record][0])
            record_list.insert(1, order_record[record][3])
            record_list.insert(2, order_record[record][4])
            record_list.insert(3, order_record[record][5])
            purchase_id.append(order_record[record][0])
            purchase_order.append(record_list)
    if len(purchase_order) == 0:
        print("There is no purchase order for this supplier...")
        disapproved_id = []
        approved_id = []
        return disapproved_id, approved_id, supplier
    specific_staff_info = list()
    for data in range(len(staff_info)):
        if staff_info[data][0] == user_id:
            specific_staff_info.extend(staff_info[data])
    print("                         Purchase Order Report                        ")
    print("______________________________________________________________________")
    print("ID Number: ", user_id, "               ", "Purchase status: Unapproved")
    print("Staff Name: ", specific_staff_info[1])
    print(" ")
    print(f"                      {supplier}              ")
    print("----------------------------------------------------------------------")
    title = ["Order ID", "Stock Name", "Quantity", "Purchase Date"]
    table_view(headers=title, data=purchase_order, column_size=18, data_size=18)
    print("----------------------------------------------------------------------")
    print("______________________________________________________________________")
    print("_____________________________")
    print("Approve all purchase order? :")
    print("'1' - Yes")
    print("'2' - No")
    print("_____________________________")
    approval = input("Please enter the number: ")
    while approval != "1" and approval != "2":
        print("Invalid option...")
        approval = input("Please enter the number")
    disapproved_id = list()
    approved_id = list()
    if approval == "1":
        print("Purchase order has been approved!!!")
        approved_id = purchase_id
    else:
        if len(purchase_order) == 1:
            disapproved_id = purchase_id
            print("Purchase order has been rejected...")
        else:
            approval_unapproved = int(input("Please enter number of order for unapproved: "))
            while approval_unapproved > len(purchase_order):
                print("number of purchase exceeded...")
                approval_unapproved = int(input("Please enter number of order for unapproved: "))

            for order in range(approval_unapproved):
                order_id = input("Please enter order ID for disapproved: ")
                while order_id not in purchase_id:
                    print("Invalid Order ID...")
                    order_id = input("Please enter order ID for disapproved: ")
                disapproved_id.append(order_id)
                del purchase_id[purchase_id.index(order_id)]
                approved_id = purchase_id
                print("Purchase order request rejected...")

    return disapproved_id, approved_id, supplier


def inventory_purchase_order_approval():
    while True:
        purchase_order = data_sort_out(file_name="inventory purchase order status.txt")
        order_list = list()
        staff_id = list()
        for record in range(1, len(purchase_order)):  # sort out unapproved purchase order
            if purchase_order[record][-1].upper() == "UNAPPROVED":  # sort out unapproved purchase order
                order_list.append(purchase_order[record])
                if purchase_order[record][1] not in staff_id:
                    staff_id.append(purchase_order[record][1])
        if len(order_list) == 0:
            print("There is no purchase order for approval....")
            print("Returning to main interface")
            break
        num_of_order = list()
        for staff in range(len(staff_id)):  # sort out purchase order number for each inventory staff
            attempt = 0
            num_record = list()
            for i in range(len(order_list)):
                if staff_id[staff] == order_list[i][1]:
                    attempt += 1
            num_record.insert(0, staff_id[staff])
            num_record.insert(1, attempt)
            num_of_order.append(num_record)
        print("Inventory staff purchase order times")
        print("____________________________________")
        title = ["ID Number", "Number of Order"]
        table_view(headers=title, data=num_of_order, column_size=15, data_size=15)
        print("____________________________________")
        id_input = input("Please enter the ID Number for purchaser order record: ")
        while id_input not in staff_id:
            print("Invalid ID Number...")
            id_input = input("Please enter the ID Number for purchaser order record: ")
        print("_________________________________")
        print("Please select the supplier: ")
        print("a) '1' - Jack Hung Tech Solutions")
        print("b) '2' - CK & Tim IT Hypermarket")
        print("_________________________________")
        supplier = input("Please enter the number: ")
        while supplier != "1" and supplier != "2":
            print("Invalid option...")
            supplier = input("Please enter the number: ")
        if supplier == "1":  # purchase order for jack hung tech solutions
            unapproved_order_id, approved_order_id, supplier_name = purchase_order_approval(
                supplier="Jack Hung Tech Solutions", order_record=order_list, user_id=id_input)
            user_activities(user_id=login_id, identity=staff_identity, activities="Inventory purchaser order approval",
                            description=id_input)
        else:  # purchase order for CK & Tim IT Hypermarket
            unapproved_order_id, approved_order_id, supplier_name = purchase_order_approval(
                supplier="CK & Tim IT Hypermarket", order_record=order_list, user_id=id_input)
            user_activities(user_id=login_id, identity=staff_identity, activities="Inventory purchaser order approval",
                            description=id_input)

        for data in range(1, len(purchase_order)):  # change the status of purchase order (rejected/approved)
            if purchase_order[data][0] in unapproved_order_id:
                purchase_order[data][-1] = "Rejected"
            elif purchase_order[data][0] in approved_order_id:
                purchase_order[data][-1] = "Approved"
            else:
                continue
        with open("inventory purchase order status.txt", "w") as inventory_order:
            for order_record in range(len(purchase_order)):  # write the new data into text file
                inventory_order.writelines(
                    purchase_order[order_record][0] + "," + purchase_order[order_record][1] + "," +
                    purchase_order[order_record][2] + "," + purchase_order[order_record][3] + "," +
                    purchase_order[order_record][4] + "," + purchase_order[order_record][5] + "," +
                    purchase_order[order_record][6] + "," + purchase_order[order_record][7] +
                    "\n")
        update_inventory_stock_quantity(approved_order_id=approved_order_id)
        print("_________________________________")
        print("Check for other purchase other? :")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("_________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option....")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to main interface...")
            break


def update_inventory_stock_quantity(approved_order_id):  # update stock of available item
    import datetime
    inventory_purchase_order = data_sort_out(file_name="inventory purchase order status.txt")
    stock_list = data_sort_out(file_name="stock.txt")
    current_datetime= datetime.datetime.now()
    Date = current_datetime.strftime("%d-%m-%Y")
    approved_order = list()
    for order in range(len(inventory_purchase_order)):
        if inventory_purchase_order[order][0] in approved_order_id:
            approved_order.append(inventory_purchase_order[order])
    available_stock_id = list()
    for record in range(len(approved_order)):
        for i in range(len(stock_list)):
            if approved_order[record][3].upper() == stock_list[i][1].upper():
                quantity_update = int(approved_order[record][4]) + int(stock_list[i][3])
                stock_list[i][3] = str(quantity_update)
                stock_list[i][-1] = Date
                available_stock_id.append(approved_order[record][0])
    for info in range(len(approved_order)):
        if approved_order[info][0] not in available_stock_id:
            with open("new stock record.txt", "a+") as new_stock_record:
                    new_stock_record.writelines(approved_order[info][0] + "," + approved_order[info][1] + "," +
                                                approved_order[info][2] + "," + approved_order[info][3] + "," +
                                                approved_order[info][4] + "," + approved_order[info][5] + "," +
                                                approved_order[info][6] + "," + approved_order[info][7] +
                                                "\n")
    with open("stock.txt", "w") as stock_record:
        for x in range(len(stock_list)):
            stock_record.writelines(stock_list[x][0] + "," + stock_list[x][1] + "," +
                                    stock_list[x][2] + "," + stock_list[x][3] + "," +
                                    stock_list[x][4] + "\n")

# user report
def cus_current_login_report(cus_access_list, cus_data, Date):
    while True:
        current_login = list()
        cus_id = list()
        for i in range(len(cus_access_list)):  # sort out current login customer info
            if cus_access_list[i][-2].upper() == "LOG IN" and cus_access_list[i][1] == Date:
                current_login.append(cus_access_list[i])
                if cus_access_list[i][0] not in cus_id:
                    cus_id.append(cus_access_list[i][0])
        cus_brief_info = list()
        for info in range(len(current_login)):  # sort out customer brief access information
            brief_info = list()
            brief_info.insert(0, current_login[info][0])
            brief_info.insert(1, current_login[info][1])
            brief_info.insert(2, current_login[info][2])
            brief_info.insert(3, current_login[info][3])
            cus_brief_info.append(brief_info)
        if len(cus_brief_info) == 0:
            print("There is no customer login record for today.....")
            break
        print("_____________________________________________________")
        title = ["ID Number", "Date", "Time", "Access type"]
        table_view(headers=title, data=cus_brief_info, column_size=13, data_size=13)
        print("______________________________________________________")
        print("Available ID Number: ", cus_id)
        id_input = input("Please enter the ID Number for detailed report: ")
        while id_input not in cus_id:
            print("Invalid ID Number...")
            id_input = input("Please enter the ID Number for detailed report: ")
        cus_data_record = list()
        for record in range(len(cus_data)):  # sort out specific customer's data
            if cus_data[record][0] == id_input:
                cus_data_record.extend(cus_data[record])
        specific_cus_info = list()
        for x in range(len(current_login)):  # sort out specific customer access record
            if id_input == current_login[x][0]:
                specific_cus_info.append(current_login[x])

        print("                    Customer Log in Report                       ")  # report display
        print("__________________________________________________________________")
        print("Customer Name: ", cus_data_record[1], "           ", "IC/ Passport: ", cus_data_record[2])
        print("ID Number: ", cus_data_record[0], "              ", "City of Domicile: ", cus_data_record[4])
        print("Phone Number: ", cus_data_record[3])
        print(" ")
        title = ["ID Number", "Date", "Time", "Access Type", "User Type"]
        table_view(headers=title, data=specific_cus_info, column_size=13, data_size=13)
        print(" ")
        print(f"Total user login on {Date}: ", len(specific_cus_info))
        print("__________________________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity,
                        activities="Check customer current login", description=id_input)
        print("_____________________________________")
        print("Check another customer login report?:")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("_____________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            break


def previous_login_record(cus_access_list, cus_data, Date):
    while True:
        previous_login = list()
        cus_id = list()
        for index in range(len(cus_access_list)):  # sort out customer info and id who log in previously
            if cus_access_list[index][-2].upper() == "LOG IN" and cus_access_list[index][1] != Date:
                previous_login.append(cus_access_list[index])
                if cus_access_list[index][0] not in cus_id:
                    cus_id.append(cus_access_list[index][0])
        cus_brief_info = list()
        cus_login_attempt = list()
        for id_info in range(len(cus_id)):  # sort out the login record and calculate user login attempt
            login_attempt = list()
            attempt = 0
            for x in range(len(previous_login)):
                brief_info = list()
                if cus_id[id_info] == previous_login[x][0]:
                    attempt += 1
                    brief_info.insert(0, previous_login[x][0])
                    brief_info.insert(1, previous_login[x][1])
                    brief_info.insert(2, previous_login[x][2])
                    brief_info.insert(3, previous_login[x][3])
                    cus_brief_info.append(brief_info)
                else:
                    continue
            if attempt == 0:
                continue
            else:
                login_attempt.insert(0, cus_id[id_info])
                login_attempt.insert(1, attempt)
                cus_login_attempt.append(login_attempt)
        title = ["ID Number", "Access attempt"]
        print("       login attempt record        ")
        print("___________________________________")
        table_view(headers=title, data=cus_login_attempt, column_size=15, data_size=15)
        print("___________________________________")
        print("Available ID Number: ", cus_id)
        id_input = input("Please enter the ID Number for customer login record: ")
        while id_input not in cus_id:  # ID Number validation
            print("Invalid ID Number...")
            id_input = input("Please enter the ID Number for customer login record: ")
        specific_login_record = list()
        for record in range(len(cus_brief_info)):  # sort out request customer record
            if cus_brief_info[record][0] == id_input:
                specific_login_record.append(cus_brief_info[record])
        cus_info = list()
        for cus_record in range(len(cus_data)):  # sort out specific customer information
            if cus_data[cus_record][0] == id_input:
                cus_info.extend(cus_data[cus_record])
        print("                Previous login record                ")
        print("______________________________________________________")
        print("Name: ", cus_info[1], "         ", "IC/Passport: ", cus_info[2])
        print("ID Number: ", cus_info[0], "         ", "City of domicile: ", cus_info[4])
        print("Phone Number: ", cus_info[3])
        print(" ")
        title = ["ID Number", "Date", "Time", "Access type"]
        table_view(headers=title, data=specific_login_record, column_size=13, data_size=13)
        print("______________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity, activities="Check customer previous login",
                        description=id_input)
        print("______________________________")
        print("Check for other login record?:")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("______________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            break


def cus_acc_activation_or_registration(access_type,id_representation, cus_access_list, cus_data, Date):
    while True:
        access_record = list()
        for x in range(len(cus_access_list)):  # sort out customer info who activate their account
            if cus_access_list[x][1] == Date and cus_access_list[x][-2].upper() == access_type:
                access_record.append(cus_access_list[x])
        acc_activate_info = list()
        cus_id = list()
        for record in range(len(access_record)):  # sort out customer acc activation record
            access_info = list()
            access_info.insert(0, access_record[record][0])
            access_info.insert(1, access_record[record][1])
            access_info.insert(2, access_record[record][2])
            access_info.insert(3, access_record[record][-1])
            acc_activate_info.append(access_info)
            cus_id.append(access_record[record][0])
        if len(acc_activate_info) == 0:
            print(f"There is no new account {access_type.lower()} record today ....")
            break
        print(f"             Account {access_type.lower()} record             ")
        print("___________________________________________________")
        title = [id_representation, "Date", "Time", "User Type"]
        table_view(headers=title, data=acc_activate_info, column_size=13, data_size=13)
        print("___________________________________________________")
        print("Available ID Number: ", cus_id)
        id_input = input("Please enter the ID Number for detail report: ")
        while id_input not in cus_id:
            print("Invalid ID Number....")
            id_input = input("Please enter the ID Number for detail report: ")
        specific_user_info = list()  # sort out specific customer acc activation info
        for info in range(len(acc_activate_info)):  # sort out specific user info
            if acc_activate_info[info][0] == id_input:
                specific_user_info.append(acc_activate_info[info])
        specific_user_data = list()  # sort out specific customer data
        for cus_info in range(len(cus_data)):
            if cus_data[cus_info][0] == id_input or cus_data[cus_info][1] == id_input or cus_data[cus_info][2] == id_input:
                specific_user_data.extend(cus_data[cus_info])
        print(f"                Account {access_type.lower()} Report                ")
        print("_________________________________________________________")
        if access_type == "ACTIVATION" or (access_type == "REGISTRATION" and len(specific_user_data) == 8):
            print("Name: ", specific_user_data[1], "            ", "IC/Passport: ", specific_user_data[2])
            print("ID Number: ", specific_user_data[0], "           ", "City of Domicile: ", specific_user_data[4])
            print("Phone Number: ", specific_user_data[3], "         ", "Access status: ", specific_user_data[-1])
        else:
            if len(specific_user_data) == 6:
                print("Name: ", specific_user_data[0], "            ", "IC/Passport: ", specific_user_data[1])
                print("ID Number: -  ", "                      ", "City of Domicile: ", specific_user_data[3])
                print("Phone Number: ", specific_user_data[2], "         ", "Access Status: ", specific_user_data[-1])
        print(" ")
        title = [id_representation, "Date", "Time", "User Type"]
        table_view(headers=title, data=specific_user_info, column_size=13, data_size=13)
        print("_________________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity,
                        activities=f"check customer account {access_type.lower()}", description=id_input)
        print("____________________________________________")
        print(f"Check other user account {access_type.lower()} report?:")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("____________________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid options...")
            decision = int(input("Please enter the number: "))
        if decision == "1":
            continue
        else:
            print("Returning to previous interface")
            break


def user_current_login(access_type, userdata, user_access_data, Date):
    while True:
        current_login = list()
        for user_record in range(len(user_access_data)):  # sort out user login record
            if user_access_data[user_record][-2].upper() == access_type and user_access_data[user_record][1] == Date:
                current_login.append(user_access_data[user_record])

        user_id = list()
        access_record = list()
        for record in range(len(current_login)):  # sort out brief login record and user id
            record_list = list()
            record_list.insert(0, current_login[record][0])
            record_list.insert(1, current_login[record][1])
            record_list.insert(2, current_login[record][2])
            record_list.insert(3, current_login[record][-1])
            access_record.append(record_list)
            if current_login[record][0] not in user_id:
                user_id.append(current_login[record][0])
            else:
                continue
        if len(access_record) == 0:
            print("There is no user login record for today....")
            break
        print("                User access record                 ")
        print("___________________________________________________")
        title = ["ID Number", "Date", "Time", "User type"]
        table_view(headers=title, data=access_record, column_size=13, data_size=13)
        print("___________________________________________________")
        print("ID Number available: ", user_id)
        id_input = input("Please enter the ID Number for detail report: ")
        while id_input not in user_id:
            print("Invalid ID Number: ")
            id_input = input("Please enter the ID Number for detail report: ")
        specific_login_record = list()
        for i in range(len(current_login)):
            if current_login[i][0] == id_input:
                specific_login = list()
                specific_login.insert(0, current_login[i][3])
                specific_login.insert(1, current_login[i][1])
                specific_login.insert(2, current_login[i][2])
                specific_login.insert(3, current_login[i][-1])
                specific_login_record.append(specific_login)
        specific_user_record = list()
        for user_record in range(len(userdata)):
            if userdata[user_record][0] == id_input:
                specific_user_record.extend(userdata[user_record])
        print("                      Current login report                       ")
        print("_________________________________________________________________")
        print("ID Number: ", specific_user_record[0])
        print("User Name: ", specific_user_record[1])
        print("Access Status: ", specific_user_record[-1].capitalize())
        print(" ")
        title = ["Access Type", "Date", "Time", "User Type"]
        table_view(headers=title, data=specific_login_record, column_size=13, data_size=13)
        print("_________________________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity, activities="check user current login",
                        description=id_input)
        print("___________________________________")
        print("Check other current login report? :")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("___________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to previous page...")
            break


def user_previous_login(access_type, userdata, user_access_data, Date):
    while True:
        previous_login = list()
        user_id = list()
        for login_record in range(len(user_access_data)):  # sort out user id and previous log in record
            if user_access_data[login_record][-2].upper() == access_type and user_access_data[login_record][1] != Date:
                previous_login.append(user_access_data[login_record])
                if user_access_data[login_record][0] not in user_id:
                    user_id.append(user_access_data[login_record][0])
        access_attempt = list()
        for record in range(len(user_id)):  # sort out user's login attempt
            attempt_record = list()
            attempt = 0
            for i in range(len(previous_login)):
                if user_id[record] == previous_login[i][0]:
                    attempt += 1
                else:
                    continue
            if attempt == 0:
                continue
            else:
                attempt_record.insert(0, user_id[record])
                attempt_record.insert(1, attempt)
                access_attempt.append(attempt_record)

        print("              User Login attempt              ")
        print("____________________________")
        title = ["ID Number", "Access attempt"]
        table_view(headers=title, data=access_attempt, column_size=13, data_size=13)
        print("____________________________")
        print("Available ID Number: ", user_id)
        id_input = input("Please enter ID Number for detail report: ")
        while id_input not in user_id:
            print("Invalid ID Number...")
            id_input = input("Please enter ID Number for detail report: ")
        specific_login_info = list()
        for login_info in range(len(previous_login)):  # sort out specific user login record
            if previous_login[login_info][0] == id_input:
                specific_login = list()
                specific_login.insert(0, previous_login[login_info][3])
                specific_login.insert(1, previous_login[login_info][1])
                specific_login.insert(2, previous_login[login_info][2])
                specific_login.insert(3, previous_login[login_info][-1])
                specific_login_info.append(specific_login)

        specific_user_info = list()
        for user_info in range(len(userdata)):  # sort out specific user information
            if userdata[user_info][0] == id_input:
                specific_user_info.extend(userdata[user_info])

        print("                           Previous login Report                           ")
        print("___________________________________________________________________________")
        print("ID Number: ", specific_user_info[0])
        print("Name: ", specific_user_info[1])
        print("Access status: ", specific_user_info[-1])
        print(" ")
        title = ["Access Type", "Date", "Time", "User Type"]
        table_view(headers=title, data=specific_login_info, column_size=13, data_size=13)
        print("___________________________________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity, activities="check user previous login",
                        description=id_input)
        print("___________________________________")
        print("Check other previous login report? :")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("___________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to previous page...")
            break


def user_access_report(access_type, userdata, user_access_data, Date):
    while True:
        access_record = list()
        user_id = list()
        for record in range(len(user_access_data)):
            if user_access_data[record][-2].upper() == access_type and user_access_data[record][1] == Date:
                access_record.append(user_access_data[record])
                if user_access_data[record][0] not in user_id:
                    user_id.append(user_access_data[record][0])

        print("                       User Access Record                        ")
        print("_________________________________________________________________")
        title = ["ID Number", "Date", "Time", "Access type", "User type"]
        table_view(headers=title, data=access_record, column_size=13, data_size=13)
        print("_________________________________________________________________")
        print("Available ID Number: ", user_id)
        id_input = input("Please enter the ID Number for detail report: ")
        while id_input not in user_id:
            print("Invalid ID Number...")
            id_input = input("Please enter the ID Number for detail report: ")
        specific_access_info = list()
        for i in range(len(access_record)):
            if access_record[i][0] == id_input:
                specific_access = list()
                specific_access.insert(0, access_record[i][3])
                specific_access.insert(1, access_record[i][1])
                specific_access.insert(2, access_record[i][2])
                specific_access.insert(3, access_record[i][-1])
                specific_access_info.append(specific_access)
        specific_user_info = list()
        for info in range(len(userdata)):
            if userdata[info][0] == id_input:
                specific_user_info.extend(userdata[info])

        print("                 User Access Report                ")
        print("___________________________________________________")
        print("ID Number: ", specific_user_info[0])
        print("Name: ", specific_user_info[1])
        print("Access status: ", specific_user_info[-1].capitalize())
        print(" ")
        title = ["Access Type", "Date", "Time", "User Type"]
        table_view(headers=title, data=specific_access_info, column_size=13, data_size=13)
        print("___________________________________________________")
        user_activities(user_id=login_id, identity=staff_identity, activities=f"check user account {access_type.lower()}",
                        description=id_input)
        print("___________________________________")
        print("Check other user access report? :")
        print("a) '1' - Yes")
        print("b) '2' - No")
        print("___________________________________")
        decision = input("Please enter the number: ")
        while decision != "1" and decision != "2":
            print("Invalid option...")
            decision = input("Please enter the number: ")
        if decision == "1":
            continue
        else:
            print("Returning to previous page...")
            break


def options_and_access_list(user_type, login_data):
    print("_________________________________")
    print("Admin report type:")
    print("a) '1' - Log in report")
    print("b) '2' - Account activation report")
    print("c) '3' - registration report")
    print("_________________________________")
    options = input("Please enter the number: ")
    while options != "1" and options != "2" and options != "3":
        print("Invalid option...")
        options = input("Please enter the number: ")
    user_access_list = list()
    for i in range(len(login_data)):
        if login_data[i][-1].upper() == user_type:
            user_access_list.append(login_data[i])
    return options, user_access_list


def decision(user_type):
    print("____________________________________")
    print("Please select: ")
    print(f"a) '1' - {user_type} report")
    print("b) '2' - User report interface")
    print("____________________________________")
    decision = input("Please enter the number: ")
    while decision != "1" and decision != "2":
        print("Invalid option...")
        decision = input("Please enter the number: ")
    if decision == "1":
        return True
    else:
        return False


def report_decision():
    print("_________________________________")
    print("login report type: ")
    print("a) '1' - Current login report")
    print("a) '2' - previous login report")
    print("_________________________________")
    report_type = input("Please enter the number: ")
    while report_type != "1" and report_type != "2":
        print("Invalid options...")
        report_type = int(input("Please enter the number: "))
    return report_type


def user_report():
    import datetime
    while True:
        print("Welcome to Reports interface")
        print("____________________________")
        print("User report: ")
        print("a) '1' - Customer")
        print("b) '2' - Admin")
        print("c) '3' - Super User")
        print("d) '4' - Inventory Staff")
        print("____________________________")
        print("* Please enter '5' for returning to user menu...")
        user_type = input("Please enter the number: ")
        if user_type == "5":  # else: continue with while function
            print("Returning to user menu")
            break
        while user_type != "1" and user_type != "2" and user_type != "3" and user_type != "4":  # validation
            print("Invalid option...")
            user_type = input("Please enter the number: ")
        login_data = data_sort_out(file_name="Login datetime.txt")
        current_datetime = datetime.datetime.now()
        Date = current_datetime.strftime("%Y-%m-%d")
        if user_type == "1":  # customer report
            cus_data = data_sort_out(file_name="Customer data.txt")
            print("Welcome to customer report interface")
            while True:
                options, cus_access_list = options_and_access_list(user_type="CUSTOMER", login_data=login_data)
                if options == "1":
                    record_type = report_decision()
                    if record_type == "1":  # current log in record
                        cus_current_login_report(cus_access_list=cus_access_list, cus_data=cus_data, Date=Date)
                    elif record_type == "2":
                        previous_login_record(cus_access_list=cus_access_list, cus_data=cus_data, Date=Date)
                elif options == "2":
                    cus_acc_activation_or_registration(access_type="ACTIVATION", id_representation="ID Number",
                                                       cus_access_list=cus_access_list, cus_data=cus_data, Date=Date)
                elif options == "3":
                    cus_acc_activation_or_registration(access_type="REGISTRATION", id_representation="IC/Passport",
                                                       cus_access_list=cus_access_list, cus_data=cus_data, Date=Date)
                check_report = decision(user_type="customer")
                if check_report:
                    continue
                else:
                    print("Returning to user report interface")
                    break
        if user_type == "2":  # admin report
            admin_data = data_sort_out(file_name="admin data.txt")
            print("Welcome to Admin report interface")
            while True:
                options, admin_access_list = options_and_access_list(user_type="ADMIN", login_data=login_data)
                if options == "1":
                    report_type = report_decision()
                    if report_type == "1":
                        user_current_login(access_type="LOG IN", userdata=admin_data,
                                           user_access_data=admin_access_list, Date=Date)
                    else:
                        user_previous_login(access_type="LOG IN", userdata=admin_data,
                                            user_access_data=admin_access_list, Date=Date)

                elif options == "2":
                    user_access_report(access_type="ACTIVATION", userdata=admin_data,
                                       user_access_data=admin_access_list, Date=Date)
                elif options == "3":
                    user_access_report(access_type="REGISTRATION", userdata=admin_data,
                                       user_access_data=admin_access_list, Date=Date)
                check_report = decision(user_type="admin")
                if check_report:
                    continue
                else:
                    print("Returning to user report interface")
                    break
        if user_type == "3":  # superuser report
            super_user_data = data_sort_out(file_name="Super User data.txt")
            print("Welcome to Super user report interface: ")
            super_user_access_data = list()
            for i in range(len(login_data)):
                if login_data[i][-1].upper() == "SUPER USER":
                    super_user_access_data.append(login_data[i])
            while True:
                report_type = report_decision()
                if report_type == "1":
                    user_current_login(access_type="LOG IN", userdata=super_user_data,
                                       user_access_data=super_user_access_data, Date=Date)
                if report_type == "2":
                    user_previous_login(access_type="LOG IN", userdata=super_user_data,
                                        user_access_data=super_user_access_data, Date=Date)
                check_report = decision(user_type="super user")
                if check_report:
                    continue
                else:
                    print("Returning to user report interface")
                    break
        if user_type == "4":  # inventory staff report
            inventory_staff_data = data_sort_out(file_name="staff info.txt")
            print("Welcome to inventory staff report interface")
            while True:
                options, inventory_staff_access_list = options_and_access_list(user_type="INVENTORY STAFF",
                                                                               login_data=login_data)
                if options == "1":
                    report_type = report_decision()
                    if report_type == "1":
                        user_current_login(access_type="LOG IN", userdata=inventory_staff_data,
                                           user_access_data=inventory_staff_access_list, Date=Date)
                    else:
                        user_previous_login(access_type="LOG IN", userdata=inventory_staff_data,
                                            user_access_data=inventory_staff_access_list, Date=Date)
                elif options == "2":
                    user_access_report(access_type="ACTIVATION", userdata=inventory_staff_data,
                                       user_access_data=inventory_staff_access_list, Date=Date)
                elif options == "3":
                    user_access_report(access_type="REGISTRATION", userdata=inventory_staff_data,
                                       user_access_data=inventory_staff_access_list, Date=Date)
                check_report = decision(user_type="inventory staff")
                if check_report:
                    continue
                else:
                    print("Returning to user report interface")
                    break


def super_user_menu():
    while True:
        print("          Welcome to admin interface          ")
        print("______________________________________________")
        print("Please select:")
        print("a) '1' - User Update and Registration Approval")
        print("b) '2' - New Customer Verification")
        print("c) '3' - User Personal Detail")
        print("d) '4' - User Access Disable")
        print("e) '5' - Inquiry of User's system usage")
        print("f) '6' - Customer Order Status")
        print("g) '7' - inventory purchase order approval")
        print("h) '8' - Report")
        print("______________________________________________")
        print("Please enter '9' for log out.")
        menu_selection = input("Please enter the number: ")
        selection = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while menu_selection not in selection:
            print("Invalid option...")
            menu_selection = input("Please enter the number: ")
        if menu_selection == "1":
            add_user()
        elif menu_selection == "2":
            new_customer_verification()
        elif menu_selection == "3":
            user_detail_modify()
        elif menu_selection == "4":
            user_access_disable()
        elif menu_selection == "5":
            system_usage_inquiry()
        elif menu_selection == "6":
            customer_order_Status()
        elif menu_selection == "7":
            inventory_purchase_order_approval()
        elif menu_selection == "8":
            user_report()
        else:
            break


# admin menu
def admin_menu():
    while True:
        print("Admin Interface")
        print("__________________________________")
        print("Please select: ")
        print("a) '1' - New Customer Verification")
        print("b) '2' - Customer Order Status")
        print("c) '3' - User Report")
        print("d) '4' - Log out")
        print("__________________________________")
        options = input("Please enter the number: ")
        while options != "1" and options != "2" and options != "3" and options != "4":
            print("Invalid option...")
            options = input("Please enter the number: ")
        if options == "1":
            new_customer_verification()
        elif options == "2":
            customer_order_Status()
        elif options == "3":
            user_report()
        else:
            break

# inventory staff menu

new_stock_record_list,new_stock_record_list_no_split = data_sort_out_2("new stock record.txt")

def id_list_stock ():
    stock_id_list = []
    for stock_id_index in range(len(stock_list)):
        stock_id_list.append(stock_list [stock_id_index] [0])
    return stock_id_list

def validate_value_error(no):
    while True:
        try:
            no = int(no)
            return no
        except ValueError:
            no = input("Please enter a valid number:")

def validate_price_error(no):
    while True:
        try:
            no = float(no)
            return no
        except ValueError:
            no = input("Please enter a valid price(RM):")



#-----------------------Purchase order for spare part(inventory)-----------------------------------------------------

def print_supplier():
    supplier_headers = ["Supplier ID", "Supplier Name", "Stock Supplied"]
    supplier_list = [["001", "Jack Hung Tech Solutions", "Computer and Laptop"],["002", "CK & Tim IT Hypermarket", "Computer Hardware"]]
    table_view_2(supplier_headers, supplier_list, "30", "30")
    return supplier_list

def purchase_from_supplier ():
    supplier_list = print_supplier()
    supplier = input("Enter the ID of the supplier to purchase stock:")
    while supplier != supplier_list[0][0] and supplier != supplier_list[1][0]:
        supplier = input("""Invalid Supplier ID
Enter the correct ID of the supplier you want to purchase stock from:""")
    stock_purchase = input("Enter the stock you want to purchase:")
    stock_purchase_quantity = input("Enter the quantity of stock you want to purchase:")
    stock_purchase_quantity = validate_value_error(stock_purchase_quantity)
    while stock_purchase_quantity <1:
        stock_purchase_quantity = input("Enter a valid quantity of stock you want to purchase:")
        stock_purchase_quantity = validate_value_error(stock_purchase_quantity)
    stock_purchase_quantity = str(stock_purchase_quantity)
    print(f"Purchase of {stock_purchase} for {stock_purchase_quantity} will be processed.")
    for i in range (2):
        if supplier_list[i][0]==supplier:
            supplier_name = supplier_list[i][1]
    if len (inventory_order_list) <2:
        order_id = "0001"
    else:
        maximum = 0
        for i in range(1, len(inventory_order_list)):
            if int(inventory_order_list[i][0]) > maximum:
                maximum = int(inventory_order_list[i][0])
        index = maximum + 1
        if index < 10:
            order_id = ("000" + str(index))
        elif index < 100:
            order_id = ("00" + str(index))
        else:
            order_id = ("0" + str(index))

    inventory_purchase_file = open("inventory purchase order status.txt","a+")
    line = (order_id+","+login_id+","+supplier_name+","+stock_purchase+","+stock_purchase_quantity+","+curr_date()+","+curr_time()+","+"Unapproved")
    line_split = [order_id,login_id,supplier_name,stock_purchase,stock_purchase_quantity,curr_date(),curr_time(),"Unapproved"]
    inventory_order_list.append(line_split)
    inventory_order_list_no_split.append(line)
    inventory_purchase_file.writelines(line+"\n")
    inventory_purchase_file.close()
    user_activities(login_id, "Inventory Staff", "Request to purchase stock from supplier", f"Requested for a purchase order of {stock_purchase_quantity} {stock_purchase} from {supplier_name}")

def purchased_item_index(spare_part):
    stock_list_before_update,stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    stock_id_list = id_list_stock()
    for i in range (len(stock_id_list)):
        if stock_id_list[i] == spare_part:
            return i,stock_list_before_update[i][3]

def print_inventory_purchase_stock():
    stock_list_before_update,stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    details_except_price_list = []
    for details_except_price in range(1, len(stock_list_before_update)):
        if int(stock_list_before_update[details_except_price][3]) > 0:
            details_except_price_list.append([stock_list_before_update[details_except_price][0], stock_list_before_update[details_except_price][1],stock_list_before_update[details_except_price][3]])
    stock_list_headers = ["Stock ID", "Stock Name","Quantity_In_Stock"]
    table_view_2(stock_list_headers, details_except_price_list, "20", "20")
    if details_except_price_list == []:
        return False
    else:
        return True



def stock_list_available():
    available_stock_list = []
    for details_except_price in range (1,len(stock_list)):
        if int(stock_list [details_except_price][3])>0:
            available_stock_list.append (stock_list [details_except_price][0])
    return available_stock_list


#-----------------------stock check and adjustments(inventory)-----------------------------------------------------

def check_stock ():
    stock_id_list = id_list_stock()
    adjust_stock = input("Enter the ID of the stock you want to adjust:")
    while adjust_stock not in stock_id_list:
        adjust_stock = input("""Stock ID not found
Please enter the correct stock ID:""")
    for i in range (len(stock_list)):
        if stock_list [i][0] == adjust_stock:
            return i,adjust_stock


def view_specific_stock ():
    stock_id_list = id_list_stock()
    specific_stock_id = input("Enter the ID of the stock you want to view:")
    while specific_stock_id not in stock_id_list:
        specific_stock_id = input("""Stock ID not found
Please enter the correct ID of the stock you want to view:""")
    for i in range (len(stock_list)):
        if stock_list [i][0] == specific_stock_id:
            return i

def remove_stock ():
    stock_id_list = id_list_stock()
    remove_id = input("Enter the stock ID for remove:")
    while remove_id not in stock_id_list:
        remove_id = input("""Stock ID not found
Please enter the correct ID of the stock to cancel:""")
    for i in range (len(stock_list)):
        if stock_list [i][0] == remove_id:
            return i, remove_id

def print_stock():
    stock_list_before_update,stock_list_no_split_before_update = data_sort_out_2("stock.txt")
    stock_list_headers = ["Stock ID", "Stock Name", "Price (RM)", "Quantity In Stock", "Last Modified Date"]
    table_view_2(stock_list_headers, stock_list_before_update[1:], "30", "30")

def print_stock_to_set_price():
    new_stock_list = []
    new_stock_order_id_list = []
    for i in range(len(new_stock_record_list)):
        new_stock_list.append([new_stock_record_list[i][0],new_stock_record_list[i][2],new_stock_record_list[i][3]])
        new_stock_order_id_list.append(new_stock_record_list[i][0])
    new_stock_list_header = ["Order ID","Supplier Name","Stock Ordered"]
    table_view_2(new_stock_list_header, new_stock_list, "30", "30")
    if new_stock_list == []:
        return False,new_stock_order_id_list
    else:
        return True,new_stock_order_id_list

def set_stock_price_index(set_price_stock):
    for i in range(len(new_stock_record_list)):
        if new_stock_record_list[i][0] == set_price_stock:
            return i,new_stock_record_list[i][3],new_stock_record_list[i][4]


def view_stock():
    while True:
        if len(stock_list) < 2:
            print_stock()
            print("No stock is in the stock list")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break
        specific_or_whole = input("""a. '1'- View the details of every stock
b. '2' - View the details of a specific stock
Please enter:""")
        while specific_or_whole != "1" and specific_or_whole != "2":
            specific_or_whole = input("""a. '1'- View the details of every stock
b. '2' - View the details of a specific stock
Please enter the correct option:""")

        if specific_or_whole == "1":
            print_stock()
            user_activities(login_id, "Inventory Staff", "Stock Check","View the details of all stocks")

        else:
            print_stock()
            stock_list_before_update, stock_list_no_split_before_update = data_sort_out_2("stock.txt")
            specific_stock_index = view_specific_stock()
            headers = ["Stock ID", "Stock Name", "Price (RM)", "Quantity In Stock", "Last Modified Date"]
            datas = stock_list_before_update[specific_stock_index]
            print(" ".join(f"{header:<30}" for header in headers))
            print(" ".join(f"{str(data):<30}" for data in datas))
            user_activities(login_id, "Inventory Staff", "Stock Check", "View the details of specific stocks")

        continue_check = input("""a. '1'- Continue stock check
b. '2'- Return
Please enter:""")
        while continue_check != "1" and continue_check != "2":
                continue_check = input("""a. '1'- Continue stock check
b. '2'- Return
Please enter the correct option:""")
        if continue_check == "2":
            break

def set_new_stock_price():
        new_stock_availability,new_stock_order_id_list = print_stock_to_set_price()
        if new_stock_availability:
            set_price_stock = input("Enter the order ID to set price for a stock:")
            while set_price_stock not in new_stock_order_id_list:
                set_price_stock = input("""Invalid Order ID
Enter the correct order ID to set price for a stock:""")
            new_stock_price = input("Enter the price per unit of the stock (RM):")
            new_stock_price = validate_price_error(new_stock_price)
            while new_stock_price < 1:
                new_stock_price = input("Please enter a valid selling price for the stock (RM):")
                new_stock_price = validate_price_error(new_stock_price)
            new_stock_price = str(new_stock_price)
            new_stock_record_index,new_stock_name,new_stock_quantity = set_stock_price_index(set_price_stock)
            new_stock_name = new_stock_name.upper()
            if len(stock_list) < 2:
                stock_id = "0001"
            else:
                maximum = 0
                for i in range(1, len(stock_list)):
                    if int(stock_list[i][0]) > maximum:
                        maximum = int(stock_list[i][0])
                index = maximum + 1
                if index < 10:
                    stock_id = ("000" + str(index))
                elif index < 100:
                    stock_id = ("00" + str(index))
                else:
                    stock_id = ("0" + str(index))
            stock_file = open("stock.txt","a+")
            line = (stock_id+","+new_stock_name+","+new_stock_price+","+new_stock_quantity+","+curr_date()+"\n")
            line_split = [stock_id,new_stock_name,new_stock_price,new_stock_quantity,curr_date()]
            stock_list.append(line_split)
            stock_file.writelines(line)
            stock_file.close()
            new_stock_record_list_no_split.remove(new_stock_record_list_no_split[new_stock_record_index])
            new_stock_record_list.remove(new_stock_record_list[new_stock_record_index])
            new_stock_record_file = open("new stock record.txt","w")
            for line in new_stock_record_list_no_split:
                new_stock_record_file.writelines(line)
            new_stock_record_file.close()
            print_stock()
            print(f"{new_stock_name} is added into stock list with RM {new_stock_price} per unit ")
            user_activities(login_id, "Inventory Staff", "Set price for new stock",f"{new_stock_name} is added into stock list with RM {new_stock_price} per unit ")


        else:
            print("No new purchased stock to set price")


def adjust_stock():
    while True:
        add_or_edit = input("""a. '1' - Add New Stock
b. '2' - Adjust Current Stock
c. '3'- Remove Stock
d. '4'- Set Price For New Purchased Stock
Please enter:""")
        while add_or_edit != "1" and add_or_edit != "2" and add_or_edit != "3" and add_or_edit != "4":
            add_or_edit = input("""a. '1' - Add New Stock
b. '2' - Adjust Current Stock
c. '3'- Remove Stock
d. '4'- Set Price For New Purchased Stock
Please enter the correct option:""")
        if add_or_edit == "1":
            stock_name = input("Enter the stock name:")
            stock_name = stock_name.upper()
            stock_price = input("Enter the selling price per unit of the stock (RM):")
            stock_price = validate_price_error(stock_price)
            while stock_price < 1:
                stock_price = input("Please enter a valid selling price for the stock (RM):")
                stock_price = validate_price_error(stock_price)
            validated_price = str(stock_price)
            amount = input("Enter the total quantity of the stock:")
            validated_amount = validate_value_error(amount)
            validated_amount = str(validated_amount)
            if len(stock_list) < 2:
                stock_id = "0001"
            else:
                maximum = 0
                for i in range(1, len(stock_list)):
                    if int(stock_list[i][0]) > maximum:
                        maximum = int(stock_list[i][0])
                index = maximum + 1
                if index < 10:
                    stock_id = ("000" + str(index))
                elif index < 100:
                    stock_id = ("00" + str(index))
                else:
                    stock_id = ("0" + str(index))
            stock_file = open("stock.txt", "a+")
            line = (stock_id + "," + stock_name + "," + validated_price + "," + validated_amount + "," + curr_date() + "\n")
            line_split = [stock_id, stock_name, validated_price, validated_amount, curr_date()]
            stock_file.writelines(line)
            stock_file.close()
            stock_list.append(line_split)
            stock_list_no_split.append(line)
            print_stock()
            print("New stock is added")
            user_activities(login_id, "Inventory Staff", "Add new stocks", f"Added {stock_name} into stock file")


        elif add_or_edit == "2" :
            print_stock()
            if len(stock_list) <2:
                print("No stock available for adjustments")
                back = input("Press '2' to return:")
                while back != "2":
                    back = input("Press '2' to return:")
                if back == "2":
                    break

            else:
                stock_index,modify_stock_id = check_stock()
                change_details = input("""a. '1'- Adjust Stock Name
b. '2'- Adjust Stock Price
c. '3'- Adjust Quantity of Stock
Please enter:""")
                while change_details != "1" and change_details != "2" and change_details != "3":
                    change_details = input("""a. '1'- Adjust Stock Name
b. '2'- Adjust Stock Price
c. '3'- Adjust Quantity of Stock
Please enter the correct option:""")

                if change_details == "1":
                    new_name = input("Enter the new stock name for the stock ID:")
                    new_name = new_name.upper()
                    stock_list[stock_index][1] = new_name
                    user_activities(login_id, "Inventory Staff", "Modify stock name",f"The stock name of {modify_stock_id} is changed to {new_name}")


                elif change_details == "2":
                    new_price = input("Enter the new price for the stock ID (RM):")
                    new_price= validate_price_error(new_price)
                    while new_price < 1:
                        new_price = input("Please enter a valid selling price for the stock (RM):")
                        new_price = validate_price_error(new_price)
                    stock_list[stock_index][2] = str(new_price)
                    user_activities(login_id, "Inventory Staff", "Modify stock price",f"The stock price of {modify_stock_id} is changed to RM {new_price}")

                else:
                    new_quantity = input("Enter the total quantity of stock for the stock ID:")
                    validated_new_quantity = validate_value_error(new_quantity)
                    stock_list[stock_index][3] = str(validated_new_quantity)
                    user_activities(login_id, "Inventory Staff", "Modify stock quantity",f"The stock quantity of {modify_stock_id} is changed to {validated_new_quantity}")

                stock_list[stock_index][4] = curr_date()
                new_line = ((stock_list[stock_index][0]) + "," + (stock_list[stock_index][1]) + "," + (stock_list[stock_index][2]) + "," + (stock_list[stock_index][3]) + "," + stock_list[stock_index][4])
                stock_list_no_split.remove(stock_list_no_split[stock_index])
                stock_list_no_split.insert(stock_index, new_line)
                stock_file = open("stock.txt", "w")
                for line in stock_list_no_split:
                    stock_file.writelines(line + "\n")
                stock_file.close()
                print_stock()
                print("Changes has been made")


        elif add_or_edit == "3":
            print_stock()
            if len(stock_list) <2:
                print("No stock available for removal")
                back = input("Press '2' to return:")
                while back != "2":
                    back = input("Press '2' to return:")
                if back == "2":
                    break

            else:
                remove_stock_index,remove_stock_id = remove_stock()
                stock_list.remove(stock_list[remove_stock_index])
                stock_list_no_split.remove(stock_list_no_split[remove_stock_index])
                stock_file = open("stock.txt", "w")
                for line in stock_list_no_split:
                    stock_file.writelines(line+"\n")
                stock_file.close()
                print_stock()
                print("Stock is removed")
                user_activities(login_id, "Inventory Staff", "Remove stock",f"{remove_stock_id} is removed from stock file")


        else:
            set_new_stock_price()





        continue_adjust = input("""a. '1'- Continue stock adjustments
b. '2'- Return
Please enter:""")
        while continue_adjust != "1" and continue_adjust != "2":
            continue_adjust = input("""a. '1'- Continue stock adjustments
b. '2'- Return
Please enter the correct option:""")
        if continue_adjust == "2":
            break






#-----------------------check purchase order status(inventory)-----------------------------------------------------

def order_status(specific_order):
    for i in range (len(inventory_order_list)):
        if inventory_order_list[i][0]== specific_order:
            order_date = inventory_order_list[i][5]
            approve_status = inventory_order_list[i][7]
    order_date_ft = datetime.datetime.strptime(order_date, "%d-%m-%Y")
    current_date = datetime.datetime.strptime(curr_date(), "%d-%m-%Y")
    date_difference = current_date - order_date_ft
    days_difference = date_difference.days
    if approve_status == "Approved":
        if days_difference <3:
            status = "Ordered Placed"
        elif days_difference <=5 :
            status = "Preparing to ship"
        elif days_difference <=7:
            status = "Shipped"
        else:
            status = "Delivered"
    elif approve_status == "Rejected":
        status = "Order Rejected"
    else:
        status = "Waiting for approval"
    return status


def print_order_list():
    display_order_list =[]
    order_id_list = []
    for i in range (1,len(inventory_order_list)):
        if login_id == inventory_order_list[i][1]:
            display_order_list.append([inventory_order_list[i][0],inventory_order_list[i][1],inventory_order_list[i][3],inventory_order_list[i][5]])
            order_id_list.append(inventory_order_list[i][0])
    staff_purchase_order_headers = ["Order ID","Staff ID", "Stock Ordered","Ordered Date"]
    table_view_2(staff_purchase_order_headers, display_order_list, "30", "30")
    if display_order_list == []:
        return False,0
    else:
        return True, order_id_list

def specific_order_details(specific_order):
    for i in range (len(inventory_order_list)):
        if inventory_order_list[i][0]== specific_order:
            return inventory_order_list[i]


#----------------------- cancel purchase order(inventory)-----------------------------------------------------

def staff_order_to_cancel():
    staff_order_id_list = []
    staff_order_details = []
    for i in range (len(inventory_order_list)):
        if login_id == inventory_order_list[i][1]:
            staff_order_details.append([inventory_order_list [i][0],inventory_order_list [i][2],inventory_order_list [i][3],inventory_order_list [i][4],inventory_order_list [i][5]])
            staff_order_id_list.append(inventory_order_list [i][0])
    order_header = ["Order ID", "Supplier Name", "Stock Purchased", "Quantity Ordered", "Date Ordered"]
    table_view_2(order_header, staff_order_details, "30", "30")
    if staff_order_details == []:
        return False,0
    else:
        return True,staff_order_id_list

def cancel_modify_inventory_order_index(order_id):
    for i in range(len(inventory_order_list)):
        if inventory_order_list [i][0] == order_id:
            return i

#----------------------------------modify purchase order(inventory)--------------------------------------------------------------
def staff_order_to_modify():
    staff_order_id_list = []
    staff_order_details = []
    for i in range (len(inventory_order_list)):
        if [inventory_order_list [i][1],inventory_order_list [i][7]]==[login_id,"Unapproved"] :
            staff_order_details.append([inventory_order_list [i][0],inventory_order_list [i][2],inventory_order_list [i][3],inventory_order_list [i][4],inventory_order_list [i][5]])
            staff_order_id_list.append(inventory_order_list [i][0])
    order_header = ["Order ID", "Supplier Name", "Stock Purchased", "Quantity Ordered", "Date Ordered"]
    table_view_2(order_header, staff_order_details, "30", "30")
    if staff_order_details == []:
        return False, 0
    else:
        return True,staff_order_id_list
#-----------------------reports(inventory)-----------------------------------------------------


def print_specific_cus_list(cus_id,purchase_list):
    specific_cus_purchase_list = []
    stock_purchase_list = []
    for i in range(len(purchase_list)):
        if purchase_list[i][0] == cus_id:
            specific_cus_purchase_list.append(purchase_list[i])
            stock_purchase_list.append(purchase_list[i][1])
    specific_cus_headers = ["Customer ID","Stock ID", "Stock Name","Last Ordered Date"]
    table_view_2(specific_cus_headers, specific_cus_purchase_list, "30", "30")
    return stock_purchase_list


def print_customer_purchase_list():
    purchase_list = []
    cus_id_list = []
    customer_purchase_list_header = ["Customer ID", "Stock ID", "Stock Name", "Last Ordered Date"]
    for i in range(1, len(order_status_list)):
        purchase_list.append([order_status_list[i][0], order_status_list[i][1], order_status_list[i][2], order_status_list[i][5]])
        cus_id_list.append (order_status_list[i][0])
    table_view_2(customer_purchase_list_header, purchase_list, "30", "30")
    if purchase_list == []:
        return False, purchase_list, cus_id_list
    else:
        return True, purchase_list, cus_id_list


def print_customer_repair_list():
    repair_list_header = ["Order ID", "Customer ID", "Service", "Repair Date"]
    repair_list = []
    repair_id_list = []
    for i in range (1,len(repair_order_list)):
        repair_list.append([repair_order_list[i][0],repair_order_list[i][1],repair_order_list[i][2],repair_order_list[i][3]])
        repair_id_list.append(repair_order_list[i][0])
    table_view_2(repair_list_header, repair_list , "30", "30")
    if repair_list == []:
        return False,repair_list,repair_id_list
    else:
        return True, repair_list,repair_id_list


def specific_cus_order_details (cus_id,stock_id):
    cus_order_details = []
    for i in range (len(order_status_list)):
        if [order_status_list[i][0],order_status_list[i][1]]==[cus_id,stock_id]:
            cus_order_details.append(order_status_list[i])
    return cus_order_details


def specific_order_date_list(cus_order_details):
    date_list = []
    for i in range (len(cus_order_details)):
        date_list.append(cus_order_details[i][5])
    return date_list


def specific_date_order_details(cus_order_details,specific_date):
    specific_date_order_list = []
    for i in range (len(cus_order_details)):
        if cus_order_details[i][5] == specific_date:
            specific_date_order_list.append(cus_order_details[i])
    return specific_date_order_list

def specific_repair_order_details(order_id):
    for i in range(len(repair_order_list)):
        if repair_order_list[i][0]==order_id:
            specific_order_details = repair_order_list[i]
            return specific_order_details

def repair_order_status(repair_date,payment_status):
    order_date_ft = datetime.datetime.strptime(repair_date, "%d-%m-%Y")
    current_dates = datetime.datetime.strptime(curr_date(), "%d-%m-%Y")
    date_difference = current_dates - order_date_ft
    days_difference = date_difference.days
    if payment_status == "Payment Completed":
        if days_difference <3:
            status = "Repairing"
        else:
            status = "Repair Completed"
    else:
        status = "Pending"
    return status


def view_purchase_order_status():
    while True:
        purchase_list_availability, purchase_list, cus_id_list = print_customer_purchase_list()
        if purchase_list_availability:
            view_specific = input("""a. '1'- View specific customer detailed purchase order status
b. '2'- Return
Please enter:""")
            while view_specific != "1" and view_specific != "2":
                view_specific = input("""a. '1'- View specific customer detailed purchase order status
b. '2'- Return
Please enter the correct option:""")
            if view_specific == "1":
                cus_id = input("Enter the ID of the customer for viewing:")
                while cus_id not in cus_id_list:
                    cus_id = input("""Invalid Customer ID
Enter the correct ID of the customer for viewing:""")
                stock_purchase_list = print_specific_cus_list(cus_id,purchase_list)
                stock_id = input("Enter the ID of the stock for viewing:")
                while stock_id not in stock_purchase_list:
                    stock_id = input("""Invalid Stock ID
Enter the correct ID of the stock for viewing:""")
                cus_order_details = specific_cus_order_details(cus_id, stock_id)
                for i in range(len(cus_order_details)):
                    print("---------------------------------------------------------------------")
                    print("                        Purchase Order Information          ")
                    print(
                    f"Customer ID: {cus_order_details[i][0]}                       Ordered Date: {cus_order_details[i][5]}")
                    print(
                    f"Payment Status: {cus_order_details[i][9]}        Ordered Time: {cus_order_details[i][6]}" + "\n")
                    print(f"""Stock Ordered: {cus_order_details[i][2]}
Quantity Ordered: {cus_order_details[i][3]}
Total Price: {cus_order_details[i][4]}""")
                    print("---------------------------------------------------------------------")



                if len(cus_order_details) > 1:
                    while True:
                        view_specific_date = input("""a. '1'- View purchase order information of a specific date from the list
b. '2'- Return
Please enter:""")
                        while view_specific_date != "1" and view_specific_date != "2":
                            view_specific_date = input("""a. '1'- View purchase order information of a specific date from the list
b. '2'- Return
Please enter the correct option:""")
                        if view_specific_date == "1":
                            specific_date = input("Enter the date you want to view (dd-mm-yyyy):")
                            date_list = specific_order_date_list(cus_order_details)
                            while specific_date not in date_list:
                                specific_date = input("Enter the correct date you want to view (dd-mm-yyyy):")
                            specific_date_order_list = specific_date_order_details(cus_order_details, specific_date)
                            for i in range(len(specific_date_order_list)):
                                print("---------------------------------------------------------------------")
                                print("                        Purchase Order Information          ")
                                print(
                            f"Customer ID: {specific_date_order_list[i][0]}                       Ordered Date: {specific_date_order_list[i][5]}")
                                print(
                            f"Payment Status: {specific_date_order_list[i][9]}        Ordered Time: {specific_date_order_list[i][6]}" + "\n")
                                print(f"""Stock Ordered: {specific_date_order_list[i][2]}
Quantity Ordered: {specific_date_order_list[i][3]}
Total Price: {specific_date_order_list[i][4]}""")
                                print("---------------------------------------------------------------------")




                        else:
                            break

                user_activities(login_id, "Inventory Staff", "View customer purchase order status",f"View purchase order information of customer ID {cus_id}")


            else:
                break

        else:
            print("No purchase order available for viewing")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break

def view_repair_order_status():
    while True:
        repair_list_availability, repair_list, repair_id_list = print_customer_repair_list()
        if repair_list_availability:
            view_specific = input("""a. '1'- View specific repair or service order status
b. '2'- Return
Please enter:""")
            while view_specific != "1" and view_specific != "2":
                view_specific = input("""a. '1'- View specific repair or service order status
b. '2'- Return
Please enter the correct option:""")
            if view_specific == "1":
                order_id = input("Enter the repair ID for viewing:")
                while order_id not in repair_id_list:
                    order_id = input("""Invalid Repair ID
Enter the correct repair ID for viewing:""")
                repair_order_details = specific_repair_order_details(order_id)
                repair_status = repair_order_status(repair_order_details[3], repair_order_details[8])
                print("---------------------------------------------------------------------")
                print("                  Repair/Service Order Information          ")
                print(f"Order ID: {repair_order_details[0]}                        Ordered Date: {repair_order_details[4]}")
                print(f"Customer ID: {repair_order_details[1]}                    Ordered Time: {repair_order_details[5]}" + "\n")
                print(f"""Service Provided: {repair_order_details[2]}
Repair Date: {repair_order_details[3]}
Payment Status: {repair_order_details[8]}
Repair Status: {repair_status}""")
                print("---------------------------------------------------------------------")
                user_activities(login_id, "Inventory Staff", "View customer repair or service order status",f"View repair or service order information of order ID {order_id}")

            else:
                break

        else:
            print("No repair order available for viewing")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break

#-------------------------------------------------menu--------------------------------------------------------------------------------------------------------------------------------------------------------------
def inventory_menu ():
    menu = input ("""a. '1'- Purchase Order for New Computers/Spare Parts
b. '2'- Stock Check/Adjustments 
c. '3'- Check Purchase Order Status
d. '4'- Cancel Inventory Purchase Order
e. '5'- Modify Inventory Purchase Order
f. '6'- Reports
g. '7'- Log Out
Please enter:""")
    while menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5" and menu != "6" and menu != "7":
        menu = input("""a. '1'- "Purchase Order for New Computers/Spare Parts
b. '2'- Stock Check/Adjustments 
c. '3'- Check Purchase Order Status
d. '4'- Cancel Inventory Purchase Order
e. '5'- Modify Inventory Purchase Order
f. '6'- Reports
g. '7'- Log Out
Please enter the correct option:""")
    return menu
#-----------------------------------------------------------main body-----------------------------------------------------------------------------------------------------------------

def purchase_spare_part():
    while True:
        available_stock_list = stock_list_available()
        stock_availability = print_inventory_purchase_stock()
        if stock_availability:
            success_purchase = True
            spare_part_availability = input("Do you find the stock you want to purchase? (Yes/No):")
            while spare_part_availability.upper()!="YES" and spare_part_availability.upper() !="NO":
                spare_part_availability = input("Do you find the stock you want to purchase? (Yes/No):")
            if spare_part_availability.upper() == "YES":
                spare_part = input("Enter the ID of the stock you want to purchase:")
                while spare_part not in available_stock_list:
                    spare_part = input("""Stock ID invalid
PLease enter the correct ID of the stock you want to purchase:""")
                purchase_quantity = input("Enter the quantity of stock you need:")
                purchase_quantity = validate_value_error(purchase_quantity)
                while purchase_quantity < 1:
                    purchase_quantity = input("Enter a valid quantity of stock you want to purchase:")
                    purchase_quantity = validate_value_error(purchase_quantity)
                purchase_item_index, available_quantity = purchased_item_index(spare_part)
                new_quantity = int(available_quantity)- purchase_quantity
                available_quantity = new_quantity
                while available_quantity < 0:
                    request_reduce = input("""You have exceeded the stock quantity available.
a. '1'- Reduce the quantity 
b. '2'- Request for purchase
Please enter:""")
                    while request_reduce != "1" and request_reduce != "2":
                        request_reduce = input("""You have exceeded the stock quantity available.
a. '1'- Reduce the quantity 
b. '2'- Request for purchase
Please enter:""")
                    if request_reduce == "1":
                        available_quantity = int(stock_list[purchase_item_index][3])
                        purchase_quantity = input("Enter the quantity of stock:")
                        purchase_quantity = validate_value_error(purchase_quantity)
                        while purchase_quantity < 1:
                            purchase_quantity = input("Enter a valid quantity of stock you want to purchase:")
                            purchase_quantity = validate_value_error(purchase_quantity)
                        available_quantity = int(available_quantity) - int(purchase_quantity)

                    else:
                        purchase_from_supplier()
                        available_quantity = 1
                        success_purchase = False
            else:
                purchase_from_supplier()
                success_purchase = False


            if success_purchase == True:
                available_quantity = str(available_quantity)
                stock_list[purchase_item_index][3] = available_quantity
                new_line = ((stock_list[purchase_item_index][0]) + "," + (stock_list[purchase_item_index][1]) + "," + (stock_list[purchase_item_index][2]) + "," + available_quantity + "," + curr_date())
                stock_list_no_split.remove(stock_list_no_split[purchase_item_index])
                stock_list_no_split.insert(purchase_item_index, new_line)
                stock_file = open("stock.txt", "w")
                for line in stock_list_no_split:
                    stock_file.writelines(line + "\n")
                stock_file.close()
                print_inventory_purchase_stock()
                print(f"{spare_part} is purchased")
                user_activities(login_id, "Inventory Staff", "Purchase stock from company",f"Place a purchase order of {purchase_quantity} {stock_list[purchase_item_index][1]} from company")



            continue_purchase = input("""a.'1'- Continue purchase other stocks
b.'2'- Return
Please enter:""")
            while continue_purchase!="1" and continue_purchase!="2":
                continue_purchase = input("""a.'1'- Continue purchase other stocks
b.'2'- Return
Please enter:""")
            if continue_purchase == "2":
                break

        else:
            print("No stock available for purchase")
            while True:
                supplier_purchase = input("""a. '1'- Purchase from supplier
b. '2'- Return
Please enter:""")
                while supplier_purchase != "1" and supplier_purchase != "2":
                    supplier_purchase = input("""a. '1'- Purchase from supplier
b. '2'- Return
Please enter the correct option""")

                if supplier_purchase == "1":
                    purchase_from_supplier()

                else:
                    break
            break




def stock_check_adjustment ():
    while True:
        option = (input("""a. '1'- Stock Check
b. '2'- Stock Adjustments
c. '3'- Return
Please enter:"""))
        while option != "1" and option != "2" and option != "3":
            option = input("""a. '1'- Stock Check
b. '2'- Stock Adjustments
c. '3'- Return
Please enter the correct option:""")
        if option == "1":
            view_stock()


        elif option == "2":
            adjust_stock()

        else:
            break



def inventory_check_order():
    while True:
        inventory_order_availability,order_id_list = print_order_list()
        if inventory_order_availability:
            view_or_return = input("""a. '1'- View specific order information
b. '2'- Return
Please enter:""")
            while view_or_return!="1" and view_or_return!="2":
                view_or_return = input("""a. '1'- View specific order information
b. '2'- Return
Please enter the correct option:""")
            if view_or_return == "1":
                specific_order = input("Enter the order ID for viewing:")
                while specific_order not in order_id_list:
                    specific_order = input("""Invalid Order ID
Enter the correct order ID for viewing:""")
                order_details = specific_order_details(specific_order)
                status = order_status(specific_order)
                print("-------------------------------------------------")
                print("           Purchase Order Information          ")
                print (f"Order ID: {order_details[0]}         Ordered Date: {order_details[5]}")
                print(f"Staff ID: {order_details[1]}        Ordered Time: {order_details[6]}"+"\n")
                print(f"""Supplier Name: {order_details[2]}
Stock Ordered: {order_details[3]} 
Quantity Ordered: {order_details[4]}
Order Status: {status}""")
                print("-------------------------------------------------")
                user_activities(login_id, "Inventory Staff", "View inventory staff purchase order status from supplier",f"View the purchase order of order ID {specific_order} ")
            else:
                break

        else:
            print("No purchase order for viewing")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break





def cancel_inventory_order():
    while True:
        staff_order_availability, staff_order_id_list = staff_order_to_cancel()
        if staff_order_availability:
            order_to_cancel = input("Enter the order ID for cancel:")
            while order_to_cancel not in staff_order_id_list:
                order_to_cancel = input("""Invalid Order ID
Please enter the correct order ID for cancel:""")
            cancel_order_index = cancel_modify_inventory_order_index(order_to_cancel)
            inventory_order_file = open("inventory purchase order status.txt","w")
            inventory_order_list_no_split.remove(inventory_order_list_no_split[cancel_order_index])
            inventory_order_list.remove(inventory_order_list[cancel_order_index])
            for line in inventory_order_list_no_split:
                inventory_order_file.writelines(line+"\n")
            inventory_order_file.close()
            staff_order_to_cancel()
            print(f"Order {order_to_cancel} is cancelled")
            user_activities(login_id, "Inventory Staff", "Cancel purchase order from supplier",f"Cancelled the purchase order of order ID {order_to_cancel}")

            continue_cancel = input("""a. '1'- Cancel another purchase order
b.'2'- Return
Please enter:""")
            while continue_cancel != "1" and continue_cancel != "2":
                continue_cancel = input("""a. '1'- Cancel another purchase order
b.'2'- Return
Please enter the correct option:""")
            if continue_cancel == "2":
                break

        else:
            print("No purchase order available for cancellation")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break



def modify_inventory_order():
    while True:
        staff_order_availability, staff_order_id_list = staff_order_to_modify()
        if staff_order_availability:
            modify_option = input("""a. '1'- Change Supplier
b. '2'- Change stock to purchase
c. '3'- Modify purchase quantity
Please enter: """)
            while modify_option != "1" and modify_option != "2" and modify_option != "3":
                modify_option = input("""a. '1'- Change supplier
b. '2'- Change stock to purchase
c. '3'- Modify purchase quantity
Please enter the correct option: """)
            order_to_modify = input("Enter the order ID to modify:")
            while order_to_modify not in staff_order_id_list:
                order_to_modify = input("""Invalid Order ID
Enter the correct order ID to modify:""")
            modify_index = cancel_modify_inventory_order_index(order_to_modify)
            if modify_option == "1":
                supplier_list = print_supplier()
                new_supplier = input("Enter the new supplier ID to change:")
                while new_supplier != supplier_list [0][0] and new_supplier != supplier_list [1][0]:
                    new_supplier = input("""Invalid Supplier ID
Enter the correct new supplier ID to change:""")
                for i in range(2):
                    if supplier_list [i][0] == new_supplier:
                        new_supplier_name = supplier_list [i][1]
                inventory_order_list [modify_index][2] = new_supplier_name
                print (f"Supplier is changed to {new_supplier_name}")
                user_activities(login_id, "Inventory Staff", "Change supplier for inventory staff purchase order",f"The supplier for order ID {order_to_modify} is changed to {new_supplier_name} ")


            elif modify_option == "2":
                change_stock = input("Enter the new stock to change:")
                inventory_order_list [modify_index][3] = change_stock
                print(f"Stock is changed to {change_stock}")
                user_activities(login_id, "Inventory Staff", "Change stock to purchase for inventory staff purchase order",f"The stock to be purchased for order ID {order_to_modify} is changed to {change_stock} ")

            elif modify_option == "3":
                change_quantity = input("Enter the quantity of stock to change:")
                change_quantity = validate_value_error(change_quantity)
                while change_quantity < 1:
                    change_quantity = input("Enter a valid quantity of stock you want to purchase:")
                    change_quantity = validate_value_error(change_quantity)
                inventory_order_list [modify_index][4] = str(change_quantity)
                print (f"The quantity of stock is changed to {change_quantity}")
                user_activities(login_id, "Inventory Staff","Change stock quantity to purchase for inventory staff purchase order",f"The stock quantity to be purchased for order ID {order_to_modify} is changed to {change_quantity} ")



            inventory_order_list[modify_index][5] = curr_date()
            inventory_order_file = open("inventory purchase order status.txt","w")
            modify_inventory_order_line = (order_to_modify+","+login_id+","+inventory_order_list [modify_index][2]+","+inventory_order_list [modify_index][3]+","+inventory_order_list [modify_index][4]+","+curr_date()+","+curr_time()+","+"Unapproved")
            inventory_order_list_no_split.remove(inventory_order_list_no_split[modify_index])
            inventory_order_list_no_split.insert(modify_index,modify_inventory_order_line)
            for line in inventory_order_list_no_split:
                inventory_order_file.writelines(line+"\n")
            inventory_order_file.close()
            staff_order_to_modify()



            continue_modify = input("""a. '1'- Modify another purchase order
b.'2'- Return
Please enter:""")
            while continue_modify != "1" and continue_modify != "2":
                continue_modify = input("""a. '1'- Modify another purchase order
b.'2'- Return
Please enter the correct option:""")
            if continue_modify == "2":
                break



        else:
            print("No purchase order available for modification")
            back = input("Press '2' to return:")
            while back != "2":
                back = input("Press '2' to return:")
            if back == "2":
                break






def inventory_report ():
    while True:
        view_report = input("""a. '1'- View customer purchase order status
b. '2' - View customer repair or service order status
c. '3'- Return
Please enter:""")
        while view_report!="1" and view_report!="2" and view_report!="3":
            view_report = input("""a. '1'- View customer purchase order status
b. '2' - View customer repair or service order status
c. '3'- Return
Please enter the correct option:""")

        if view_report == "1":
            view_purchase_order_status()


        elif view_report == "2":
            view_repair_order_status()

        else:
            break

#---------------------------------------------------------Full flow------------------------------------------------------------------------


while True:
    print('   Kl Central Computer Company   ')
    print("_________________________________")
    print('Please select the options below: ')
    print("1. Log in")
    print("2. Sign up")
    print("3. Quit")
    print("_________________________________")
    options = input("Please enter the number: ")  # choose for sign up or log in
    while options != "1" and options != "2" and options != "3":
        print("Invalid option....")
        options = input("Please enter the number: ")

    previous_page = False
    if options == "1":  # log in interface # user log in and sign up interface
        print("    Log in Interface    ")
        print("________________________")
        print("User Type:")
        print("a) '1' - Customer")
        print("b) '2' - Admin")
        print("c) '3' - Inventory staff")
        print("d) '4' - Super user")
        print("________________________")
        print("Please enter '5' for returning to previous page.")
        identity = input("Please enter the number: ")
        while identity != "1" and identity != "2" and identity != "3" and identity != "4" and identity != "5":
            print("Invalid option...")
            identity = input("Please enter the number: ")
        if identity == "1":  # customer login
            customer_status = input("Are you first time user? (Yes/No): ")
            while customer_status.upper() != "YES" and customer_status.upper() != "NO":
                customer_status = input("Are you first time user? (Yes/No): ")

            cus_menu = False
            if customer_status.upper() == "NO":  # Customer is not a new user
                cus_id = input("Please enter your ID Number: ")
                customer_validity()
                cus_validity, id_index = customer_validity()
                customer_acc_validity()
                cus_acc_validity, cus_acc_index = customer_acc_validity()
                cus_menu = customer_login()
                if cus_menu:
                    login_id = cus_id
                    while True:
                        cus_menu = customer_menu()
                        if cus_menu == "1":
                            customer_purchase_order()
                        elif cus_menu == "2":
                            service_or_repair_order()
                        elif cus_menu == "3":
                            view_cart()
                        elif cus_menu == "4":
                            modify_service_order()
                        elif cus_menu == "5":
                            inquiry_order_status()
                        elif cus_menu == "6":
                            cus_report()
                        else:
                            break
            if customer_status.upper() == "YES":
                identity_num = input("Please enter your IC/Passport number: ")
                new_cus_validity()
                ic_num_validity, new_cus_index = new_cus_validity()
                new_cus_register_validity()
                new_customer = new_cus_register_validity()
                first_time_customer()
            previous_page = True

        elif identity == "2":  # admin login
            user_status = input("Are you first time user? (Yes/No): ")
            while user_status.upper() != "YES" and user_status.upper() != "NO":
                user_status = input("Are you first time user? (Yes/No): ")
            staff_id = input("Enter your staff ID: ")
            login_id = staff_id

            admin_info_validity()
            user_validity, index = admin_info_validity()
            admin_acc_validity()
            acc_valid, pass_index = admin_acc_validity()
            new_admin_acc_validity()
            new_admin_acc, acc_pass_index = new_admin_acc_validity()
            admin_access = admin_login()
            staff_identity = "Admin"
            if admin_access:
                admin_menu()
            previous_page = True
        elif identity == "3":  # inventory staff login
            check_first_time = input("Are you first time user? (Yes/No):")
            while check_first_time.upper() != "YES" and check_first_time.upper() != "NO":
                check_first_time = input("Are you first time user? (Yes/No):")
            login_id = input("Enter your staff ID:")

            check_index()
            check, index = check_index()
            check_password()
            check_acc, acc_index = check_password()
            staff_menu = inventory_staff_log_in()
            if staff_menu:
                while True:
                    inv_menu = inventory_menu()
                    if inv_menu == "1":
                        purchase_spare_part()
                    elif inv_menu == "2":
                        stock_check_adjustment()
                    elif inv_menu == "3":
                        inventory_check_order()
                    elif inv_menu == "4":
                        cancel_inventory_order()
                    elif inv_menu == "5":
                        modify_inventory_order()
                    elif inv_menu == "6":
                        inventory_report()
                    else:
                        break
            previous_page = True
        elif identity == "4":  # super user login
            login_id = super_user()
            staff_identity = "Super User"
            super_user_menu()
            previous_page = True
        elif identity == "5":  # back to previous page
            previous_page = True
    elif options == "2":  # sign up interface
        while True:
            print("     Registration Interface     ")
            print("________________________________")
            print("User type:")
            print("a) '1' - Customer")
            print("b) '2' - Admin")
            print("c) '3' - Inventory staff")
            print("________________________________")
            print("* Please enter '4' for returning to previous page.")
            identity = int(input("Please enter number of your identity: "))
            if identity == 1:  # customer sign up
                customer_register()
                continue
            elif identity == 2:
                admin_register()
                continue
            elif identity == 3:
                inventory_staff_register()
                continue
            elif identity == 4:
                previous_page = True
                break
    else:
        break
    if previous_page:
        continue

