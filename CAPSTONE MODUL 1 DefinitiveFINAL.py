
#TIBAN INDAH HOSPITAL

#Password for superadmin =123
#Password for doctor =abc
#Fungsi utama dari line 583 sampai 921

#DATA DUMMY ===========================================================================================================================================
# print('\nno    |ID\t|name\t\t\t\t|age\t|height\t|weight\t|previous_treatment\t\t\t|current_treatment\t\t\tEntry Date    |Out Date    |category')

patients = [
#   ['                                       ', nn, nnn, nnn,'last illness                     current treatment               yyyy/mm/dd  , 'yyyy/mm/dd'  ,'category']           
    [2023001,'Asep Sulaiman                  ', 25, 182, 73, 'Cardiac Arrest                ','Chronic blood deprivation     ','2023/4/11' , '2023/4/23' ,'UGD'],
    [2023002,'Tatang Iskandar                ', 42, 172, 55, 'harmstring                    ','Acute Crucial Ligament        ','2023/3/12'  , '2023/3/23' ,'SPL LR'],
    [2023003,'Cecep Delacroix                ', 18, 166, 81, 'poisoning                     ','Vertigo                       ','2023/6/2' , '2023/6/2' ,'UMUM'],   
    [2023004,'Michael Smither                ', 33, 184, 110,'Severe Bleeding               ','Anemia                        ','2023/6/3' , '2023/6/6'   ,'SPL DLM'],
    [2023005,'Elizabeth Iskandar             ', 27, 162, 48, 'Vertigo                       ','Influenza                     ','2023/7/5' , '2023/7/5'  ,'UMUM'],
    [2023006,'Don Roe                        ', 23, 172, 61, '                              ','Common Cold                   ','2023/2/22' , '2023/2/22'  ,'UMUM'],
    [2023007,'Ali Alban                      ', 29, 175, 68, 'Influenza                     ','blurry eyes                   ','2023/3/14' , '2023/3/4'  ,'UGD'],
    [2023008,'Septian Firdaus                ', 15, 145, 48, '                              ','Respiratory Distress          ','2023/4/3' , '2023/4/9'  ,'UGD'],
    [2023009,'Romero Dresden                 ', 28, 180, 56, 'Asthma                        ','Chronic Asthma                ','2023/5/22' , '2023/5/25'  ,'UGD'],
    [2023010,'Melanie Cunning                ', 25, 158, 55, 'Vertigo                       ','Sinusitis                     ','2023/4/21' , '2023/4/21'  ,'THT'],
    [2023011,'Iyet Sudrajat                  ', 44, 162, 70, 'Pneumonia                     ','Respiratory Distress          ','2023/7/1' , '2023/7/12'  ,'UGD'],
    [2023012,'Suichi Tomoru                  ', 35, 167, 53, '                              ','Neck Injury                   ','2023/7/8' , '2023/7/12'  ,'SPL LR'],
    [2023013,'Rochelle                       ', 36, 159, 62, 'Anemia                        ','blurry eyes                   ','2023/5/30' , '2023/5/30'  ,'THT'],
    [2023014,'Javier Rodriguez               ', 20, 180, 80, 'Hepatisis A                   ','Hepatisis B                   ','2023/4/18' , '2023/4/21'  ,'SPL DLM'],
    [2023015,'Budi Abdul                     ', 68, 172, 61, 'Minor Cuts                    ','Diabetest                     ','2023/6/6' , '2023/6/7'  ,'SPL DLM'],
    [2023016,'Mukhlis Salim                  ', 50, 170, 60, 'Common Cold                   ','Common Cold                   ','2023/6/22' , '2023/6/22'  ,'UMUM'],
    [2023017,'Leandro Santos                 ', 31, 182, 91, 'poisoning                     ','Severe Bleeding               ','2023/5/6' , '2023/5/8'  ,'UGD'],    
    [2023018,'Hana Irnanta                   ', 28, 162, 49, '                              ','Anemia                        ','2023/4/25' , '2023/4/28'  ,'SPL DLM'],
    [2023019,'Clemenza                       ', 56, 162, 88, 'Influenza                     ','Influenza                     ','2023/4/26' , '2023/4/26'  ,'UMUM'],
    [2023020,'Selena Lopez                   ', 12, 136, 36, '                              ','Ear infection                 ','2023/5/28' , '2023/5/28'  ,'THT'],
    [2023021,'Mira Nabilla                   ', 40, 162, 73, 'Vertigo                       ','Minor Cuts                    ','2023/7/1' , '2023/7/1'  ,'SPL LR']
]

doctor_category = {
    '1' : {'name': 'dokter umum', 'init':'UMUM'},
    '2' : {'name': 'dokter UGD', 'init':'UGD'},
    '3' : {'name': 'spesialis THT', 'init':'THT'},
    '4' : {'name': 'spesialis penyakit dalam', 'init':'SPL DLM'},
    '5' : {'name': 'spesialis penyakit luar', 'init':'SPL LR'}
    }



# ===================================================================================================

#=====FUNCTION Display TABLE AND PRINT=====
def menu(): 
    print('''
    ================================================================================
    ===================welcome to TIBAN INDAH Hospital============================== 
    This is our database, please choose the menus:
    1. Display database
    2. Add patient data
    3. delete patient data
    4. update patient data
    5. authority access
    6. exit
    ================================================================================
            
''')

def display_table():
    print('\nno    |ID\t|name\t\t\t\t|age\t|height\t|weight\t|previous_treatment\t\t|current_treatment\t\t|entry_date    |out_date       |category')
    print(200*'-')

def display_table2():
    print('''
    column name:
    - ID
    - name
    - age 
    - height
    - weight
    - previous_treatment
    - current_treatment
    - entry_date
    - out_date
    - category
     ''')     
          
          
def update_sub_menu():
    print('''
    ======= Edit Data =======
        1. Edit data
        2. Go back to main menu
     ''')

def save_in_update():
    while True:
        saving_update = input('save the update? y/n: ')
        if saving_update == 'y' or saving_update == 'yes':
            display_table()
            break
        elif saving_update == 'n' or saving_update == 'no':
            break
        else:
            print('invalid input')
    return saving_update



#=====FUNCTION ADD Data=====
def input_unique_ID():
    matching_id = True
    while matching_id:
        id1 = input("input your id (must 3 digits): ")
        while len(id1) != 3 or not id1.isnumeric():
            print("invalid input")
            id1 = input("input your id (must 3 digit): ")
        id1 = '2023' + id1
        unique_id = int(id1)

        for id_data in patients:
            if id_data[0] == unique_id:
                print('id already exists!')
                break
        else: 
            matching_id = False
    return(unique_id)
    

def input_name():
    first_name = input("input patient's first name (max 15 characters): ")
    maxchar = 15

    while len(first_name) > maxchar or first_name.isspace() or not first_name.isalpha() or first_name == '':
        if len(first_name) > maxchar:
            print('first name exceeded 15 characters!')
        else:
            print('name must consists of alphabet character!')
        first_name = input("input patient's first name (max 15 characters): ")

    last_name = input("input patient's last name (max 15 characters): ")

    while len(last_name) > maxchar or last_name.isspace() or not last_name.isalpha() or last_name == '':
        if len(last_name) > maxchar:
            print('last name exceeded 15 characters!')
        elif last_name == '':
            break
        else:
            print('name must consists of alphabet character!')
        last_name = input("input patient's first name (max 15 characters): ")

    full_name = first_name.capitalize() + ' ' + last_name.capitalize() 
    count_name = full_name+(maxchar*2 - len(full_name))*' '

    return count_name

def input_age():
    age = input("input patient's age: ")

    while not age.isnumeric():
        print('age must a numeric')
        age = input("input patient's age: ")
    
    return age

def input_height():
    height = input("input patient's height in CM: ")
    while not height.isnumeric() or int(height) >= 300:
        if not height.isnumeric():
            print('height must be a numeric')
        else:
            print('height must be below 300 CM limit')
        height = input("input patient's height in CM: ")
    
    return height

def input_weight():
    weight = input("input patient's Weight in KG: ")
    while not weight.isnumeric() or int(weight) >= 1000:
        if not weight.isnumeric():
            print('height must be a numeric')
        else:
            print('height must be below 1000 KG limit')
        weight = input("input patient's Weight IN KG: ")
    
    return weight

def input_last_treatment():
    last_treatment = input("input patient's last treatment if any (max 30 characters), if not leave blank: ")
    maxchar_l_t = 30

    while len(last_treatment) > maxchar_l_t:
        print('cannot exceeded 30 characters!')
        last_treatment = input("input patient's last treatment if any (max 30 characters), if not leave blank: ")
        if len(last_treatment) <= maxchar_l_t:
            break
    
    last_treatment_count = last_treatment+(maxchar_l_t - len(last_treatment))*' '
    return last_treatment_count


def input_current_treatment():
    current_treatment = input("input patient's current treatment(max 30 characters): ")
    maxchar_ct = 30

    while len(current_treatment) > maxchar_ct:
        print('name exceeded 30 characters!')
        current_treatment = input("input patient's current treatment(max 30 characters): ")
        if len(current_treatment) <= maxchar_ct:
            break
    
    current_treatment_count = current_treatment+(maxchar_ct - len(current_treatment))*' '
    return current_treatment_count

def input_date_last_visit():
    date_last_visit = input("input patient's visit DATE(format: yyyy/mm/dd): ")
    format_d = date_last_visit.split('/')

    while not (len(format_d) == 3 and len(format_d[0]) == 4 and (len(format_d[1]) <= 2 and int(format_d[1]) >= 1 and int(format_d[1]) <= 12) and (len(format_d[2]) <= 2 and int(format_d[2]) >= 1 and int(format_d[2]) <= 31)):
        print('invalid date format')
        date_last_visit = input("input patient's visit DATE(format: yyyy/mm/dd): ")
        format_d = date_last_visit.split('/')
    
    return date_last_visit

def input_date_discharged(previous_date):
    format_d = previous_date.split('/')
    date_discharged = input("input patient's discharged DATE(format: yyyy/mm/dd): ")
    format_o = date_discharged.split('/')

    while not (len(format_o) == 3 and len(format_o[0]) == 4 and (len(format_o[1]) <= 2 and int(format_o[1]) >= 1 and int(format_o[1]) <= 12) and (len(format_o[2]) <= 2 and int(format_o[2]) >= 1 and int(format_o[2]) <= 31)):
        print('invalid date format')
        date_discharged = input("input patient's out DATE(format: yyyy/mm/dd): ")
        format_o = date_discharged.split('/')

    year_e, month_e, day_e = int(format_d[0]), int(format_d[1]), int(format_d[2])
    year_o, month_o, day_o = int(format_o[0]), int(format_o[1]), int(format_o[2])

    valid_entry = 10000 * year_e + 100 * month_e + 1 * day_e
    valid_out = 10000 * year_o + 100 * month_o + 1 * day_o

    while valid_entry > valid_out:
        print('out date must be after/equal entry date!')
        date_discharged = input("input patient's out DATE(format: yyyy/mm/dd): ")
        format_o = date_discharged.split('/')
        
        while not (len(format_o) == 3 and len(format_o[0]) == 4 and (len(format_o[1]) <= 2 and int(format_o[1]) >= 1 and int(format_o[1]) <= 12) and (len(format_o[2]) <= 2 and int(format_o[2]) >= 1 and int(format_o[2]) <= 31)):
            print('invalid date format')
            date_discharged = input("input patient's out DATE(format: yyyy/mm/dd): ")
            format_o = date_discharged.split('/')

        year_o, month_o, day_o = int(format_o[0]), int(format_o[1]), int(format_o[2])
        valid_out = 10000 * year_o + 100 * month_o + 1 * day_o

    return date_discharged

def input_category():

    for xx,val in doctor_category.items():
        print(f"{xx}.   {val['name']} ({val['init']})")

    category = input("input patient's category's code: ")
    while category not in doctor_category or not category.isnumeric:
        print('code is not found in the category')
        category = input("input patient's category's code: ")
        
    return(doctor_category[category]['init'])


# #=====FUNCTION CAPTCHA IN AUTHORITY SUPERADMIN Data=====

def captcha():
    import random
    code1 = random.randint(0,9)
    code2 = random.choice('abcdefghijklmnopqrstuvwxyz')
    code3 = random.randint(0,9)
    code4 = random.choice('abcdefghijklmnopqrstuvwxyz')

    print()
    print('verification box:\n///////======////=[',code1,']///////=====|||===[',code2,']/////====\n///=====[',code3,']==|||||///////////[',code4,']//======//')
    print()

    code_main = str(code1) + code2 + str(code3) + code4
    input_code = input('input 4 letter/number from verification box: ')

    if code_main == input_code:
        return True
    else:
        return False


#=====FUNCTION EDIT CATEGORY DOCTOR FOR SUPERADMIN=====
def edit_category():
    print()
    for xx,val in doctor_category.items():
        print(f"{xx}.   {val['name']} ({val['init']})")
    print()

    edit_category_choice = input("choose 1 to add, choose 2 to remove, choose any to go back: ")
    if edit_category_choice == '1':
        categoryint = len(doctor_category) + 1
        category_number = str(categoryint)
        category_name = input('Enter word: ')

        while not category_name.strip() or not category_name.replace(' ', '').isalpha():
            if not category_name.strip():
                pass
            else:
                print('invalid input, must have alphabet')
            category_name = input('Enter word: ')

        category_code = input('input initial (max 7 char): ')
        while len(category_code) > 7 or not category_code.strip():
            if len(category_code) > 7:
                print('exceed 7 characters!')
            else:
                print('invalid input, must be alpha or numeric')
            category_code = input('input initial (max 7 char): ')
            
        revert = True
        for xx, val in doctor_category.items():
            if val['init'].lower() == category_code.lower():
                print('initial cannot be same')
                revert = False
                break

        if revert:
            doctor_category[category_number] = {'name': category_name, 'init': category_code}
            for xx, val in doctor_category.items():
                print(f"{xx}.   {val['name']} ({val['init']})")
        else:
            pass
    elif edit_category_choice == '2':
        id_delete_category = input("delete category's number: ")
        while not id_delete_category.isnumeric():
            print('invalid, input must only be numeric')
            id_delete_category = input("delete category's number: ")
        
        is_used = False
        for patient in patients: 
            if patient[9] == doctor_category[id_delete_category]['init']:
                is_used = True
                break
        if is_used:    
            print('cannot be deleted since the category is used in database, you must delete/update the category first in delete/update feature')
        else:
            del doctor_category[id_delete_category]
            print('category deleted!')

##=====FUNCTION MONTHLY REPORTING SUPERADMIN=====
def reporting():
    which_month = input('enter month in number (eg, march is "3"): ')
    while not which_month.isnumeric() or int(which_month) < 1 or int(which_month)>12:
        print('invalid format')
        which_month = input('enter month in number (eg, march is "3"): ')

    month_name = ''
    if which_month == '1':
        month_name = 'January'
    elif which_month == '2':
        month_name = 'February'
    elif which_month == '3':
        month_name = 'March'
    elif which_month == '4':
        month_name = 'April'
    elif which_month == '5':
        month_name = 'May'
    elif which_month == '6':
        month_name = 'June'
    elif which_month == '7':
        month_name = 'July'
    elif which_month == '8':
        month_name = 'August'
    elif which_month == '9':
        month_name = 'September'
    elif which_month == '10':
        month_name = 'October'
    elif which_month == '11':
        month_name = 'November'
    elif which_month == '12':
        month_name = 'December'


    daily_ebox = []
    months_e = []  
    for monthly in patients:
        report_date_e = monthly[7] 
        single_month_e = report_date_e.split('/')[1]
        if single_month_e == which_month:  
            months_e.append(single_month_e)  
            daily_e = report_date_e.split('/')[2]
            daily_ebox.append(daily_e)


    count_month_entry = len(months_e)  

    daily_obox = []
    months_o = []
    for monthly in patients:
        report_date_o = monthly[8] 
        single_month_o = report_date_o.split('/')[1]  
        if single_month_o == which_month:
            months_o.append(single_month_o)
            daily_o = report_date_o.split('/')[2]
            daily_obox.append(daily_o)

    count_month_discharged= len(months_o)  

    not_stay = 0
    stay = 0

    for i in range(len(daily_ebox)):
        if daily_ebox[i] == daily_obox[i]:
            not_stay += 1
        else:
            stay += 1

    category_counts = {}
    for cate9 in patients:
        date_entry_month = int(cate9[7].split('/')[1])
        category = cate9[9]

        if date_entry_month == int(which_month):
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1

    print()
    print('=============== Monthly report for',month_name,'======================')
    print()
    print('- TOTAL PATIENT ADMISSION:              \t',count_month_entry,'Patient')
    print('- TOTAL PATIENT DISCHARGED:              \t',count_month_discharged,'Patient')
    print('- BED USAGE:                             \t',stay,'UNIT')

    if count_month_entry == 0:
        pass
    else:
        print('CATEGORY')
        for category, counting in category_counts.items():
            print('- ',category,':\t\t\t\t\t',counting, 'patients')


#=====FUNCTION AUTHORITY ACCESS: FOR DOCTOR/MEDICAL LETTER=====
def medical_letter():
    find_id = input('input 7 digits patient id: ')    
    while not find_id.isnumeric():
        print('invalid, input must only be numeric')
        find_id = input('input 7 digits patient id: ')

    find_ids = int(find_id)
    search_one = False
    for find in range(len(patients)):
        if patients[find][0] == find_ids:
            print('found!')
            search_one = True
            break

    if search_one == False:
            print('Data does not exist')
    else:
        print('data found! name = ',patients[find][1])
        save = input("do you want to proceed to print doctor's letter?(y/n): ")
        while save != 'y' and save != 'n':
            print('invalid input')
            save = input("do you want to proceed to print doctor's letter?(y/n): ")
        if save == 'n':
            pass
        else:
            print(f'''
            ========================================================================================================     
                                                    ///MEDICAL DOCTOR LETTER///
                                                    -TIBAN INDAH HOSPITAL-
            
            patient's name = {patients[find][1]}
            age = {patients[find][2]}
            illness = {patients[find][6]}

            we hereby declare that the patient is currently on sick leave as of the date from {patients[find][7]} until
            date of {patients[find][8]}. 
            
            Thus this letter is made to be known and used properly.

            Sincerely, checked and signed by,                                                     
            doctor category of {patients[find][9]}     \t\t\t\t\t\t\tTIBAN INDAH HOSPITAL
            =========================================================================================================
            ''') 

#=====MAIN FUNCTION AUTHORITY ACCESS=====

def authority_access():
    print('You are entering authority access,\npress 1 for superadmin account\npress 2 for doctor account\npress 3 to go back\nplease sign in based on your role ')
    authority1 = input('your input: ')
    if authority1 == '1':
        word = input('input your password as superadmin: ')
        if word != '123':
            print('Access denied, you will be directed to the main menu!')
        else:
            print ('Access GRANTED! Welcome Superadmin')
            print()
            superadmin()
    elif authority1 == '2':
        word = input('input your password as doctor: ')
        if word != 'abc':
            print('Access denied, you will be directed to the main menu!')
        else:
            print ('Access GRANTED! Welcome Doctor')
            print()
            doctor_access()
    elif authority1 == '0':
        pass
    else:
        print('invalid input, you will be directed to the main menu!')    

def superadmin():
    print('''
    ================
    As SUPERADMIN YOU CAN DO:
          1. Delete All Data(requires authentication)
          2. Update doctor's category in category column
          3. print monthly report
          0. exit to main menu
      ''')
    
    super_choice = input('input choice: ')
    if super_choice == '1':
        all_delete = input('are you sure you want to delete WHOLE data? (press y to continue, press anything to cancel): ')
        if all_delete == 'y':
            if captcha():
                print('code accepted!, delete in progress...\ndeleted!')
                patients.clear()
            else:
                print('verification input is wrong')
        else:
            pass
    
    elif super_choice == '2':
        print('add or replace category: ')
        edit_category()
    
    elif super_choice == '3':
        print('monthly report proceed')
        reporting()

def superadmin():
    print('''
    ================
    As SUPERADMIN YOU CAN DO:
          1. Delete All Data(requires authentication)
          2. Update doctor's category in category column
          3. print monthly report
          0. exit to main menu
      ''')
    
    super_choice = input('input choice: ')
    if super_choice == '1':
        all_delete = input('are you sure you want to delete WHOLE data? (press y to continue, press anything to cancel): ')
        if all_delete == 'y':
            if captcha():
                print('code accepted!, delete in progress...\ndeleted!')
                patients.clear()
            else:
                print('verification input is wrong')
        else:
            pass
    
    elif super_choice == '2':
        print('add or replace category: ')
        edit_category()
    
    elif super_choice == '3':
        print('monthly report proceed')
        reporting()

def doctor_access():
    print('''
    ================
    As DOCTOR YOU CAN DO:
          1. Print medical letter
          0. exit to main menu
      ''')
    
    doc_choice = input('input choice: ')
    if doc_choice == '1':
        print('medical letter')
        medical_letter()
    else:
        pass


#=====FUNCTION MAIN DISPLAY=====

def display_data():
    if len(patients) == 0:
        print('Data does not exist')
    else:
        display_table()
        idx = 1
        for idx, patient in enumerate(patients,start=1):
            print(f'{idx}\t{patient[0]}\t{patient[1]}\t{patient[2]}\t{patient[3]}\t{patient[4]}\t{patient[5]}\t{patient[6]}\t{patient[7]}\t{patient[8]}\t{patient[9]}')
        
def display_data_single():
    find_id = input('input 7 digits patient id: ')    
    while not find_id.isnumeric():
        print('invalid, input must only be numeric')
        find_id = input('input 7 digits patient id: ')
    find_idx = int(find_id)
    search_one = False
    for find in range(len(patients)):
        if patients[find][0] == find_idx:
            print('found!')
            search_one = True
            break
    if search_one == False:
        print('Data does not exist')
    else:
        display_table()
        print(f'     {patients[find][0]}\t{patients[find][1]}\t{patients[find][2]}\t{patients[find][3]}\t{patients[find][4]}\t{patients[find][5]}\t{patients[find][6]}\t{patients[find][7]}\t{patients[find][8]}\t{patients[find][9]}')

def main_display_data():
    print('''
          Press 1 for showing all data table.
          Press 2 for searching single patient's data
          Press 0 for go back to the main menu
          '''
    )
    display_advance = input('what data?')
    if display_advance == '1':
        display_data()
    elif display_advance == '2':
        display_data_single()
    elif display_advance == '0':
        pass
    else:
        print('invalid input, you will be directed back to main menu')    

#=====FUNCTION MAIN ADD=====

def add_data():
    key_id = input_unique_ID()
    name = input_name()
    age = input_age()
    height = input_height()
    weight = input_weight()
    previous_treatment = input_last_treatment()
    current_treatment = input_current_treatment()
    previous_date = input_date_last_visit()
    discharged_date = input_date_discharged(previous_date)
    code = input_category()
    while True:
        display_table()
        print(f'      {key_id}\t{name}\t{age}\t{height}\t{weight}\t{previous_treatment}\t{current_treatment}\t{previous_date}\t{discharged_date}\t{code}')
        print()
        save = input('save the data?(y or n): ')
        if save == 'y' or save =='yes':
            data = [key_id, name, age, height, weight, previous_treatment, current_treatment, previous_date, discharged_date, code]
            patients.append(data)
            print('data added sucessfully')
            break
        elif save == 'n' or save == 'no':
            print('data reverted')
            break
        else:
            print('invalid input')      

    display_data()

#=====FUNCTION MAIN UPDATE=====
def update_data():
    while True:
        update_sub_menu()
        update_main = input('please choose the edit option: ')
        while  update_main != '1' and update_main != '2':
            print('invalid input')
            update_sub_menu()
            update_main = input('please choose the edit option: ')
            
        if update_main == '1':
            update1 = True
            while True:
                id2 = input('choose 7 digits ID that will be updated (or press 0 to go back): ')
                while len(id2) !=7 or not id2.isnumeric() or id2 == '0':
                    if id2 == '0':
                        update1 = False
                        break
                    else:
                        print('invalid input')
                        id2 = input('choose 7 digits ID that will be updated (or press 0 to go back): ')
                        
                if update1 == True:
                    update2 = False
                    id2 = int(id2)
                    for id_data_u in range(len(patients)):
                        if patients[id_data_u][0] == id2:
                            print('id is found')
                            update2 = True
                            break
                    if update2 == True:
                        display_table()
                        def show_update():
                            print(f'      {patients[id_data_u][0]}\t{patients[id_data_u][1]}\t{patients[id_data_u][2]}\t{patients[id_data_u][3]}\t{patients[id_data_u][4]}\t{patients[id_data_u][5]}\t{patients[id_data_u][6]}\t{patients[id_data_u][7]}\t{patients[id_data_u][8]}\t{patients[id_data_u][9]}')
                            print()    
                        show_update()
                        print('do you want to continue update this data?\npress y to edit data\npress n to go back')

                        id3 = input('your input: ')
                        while id3 != 'y' and id3 != 'n':
                            print('invalid input')
                            id3 = input('your input: ')    
                        if id3 == 'y':
                            update3 = True 
                            while update3:
                                display_table2()
                                id4 = input('choose name of the column: ').lower()
                                while id4 == 'id' or id4 == 'name' or id4 == 'age' or id4 == 'height' or id4 == 'weight' or id4 == 'previous_treatment' or id4 == 'entry_date' or id4 == 'current_treatment' or id4 == 'category' or id4 == 'out_date' or id4 == 'ID' or id4 =='E': 
                                    if id4 == 'id':
                                        unique_id = input_unique_ID()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][0] = unique_id                                    
                                            show_update()
                                            print('data ID succesfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'name':
                                        name = input_name()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][1] = name                                    
                                            show_update()
                                            print('data NAME succesfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'age':  
                                        age = input_age()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][2] = age
                                            show_update()
                                            print('data AGE successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'height':  
                                        height = input_height()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][3] = height
                                            show_update()
                                            print('data HEIGHT successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'weight':  
                                        weight = input_weight()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][4] = weight
                                            show_update()
                                            print('data WEIGHT successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'previous_treatment':  
                                        previous_treatment = input_last_treatment()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][5] = previous_treatment
                                            show_update()
                                            print('data PREVIOUS_TREATMENT successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'current_treatment':  
                                        current_treatment = input_current_treatment()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][6] = current_treatment
                                            show_update()
                                            print('data CURRENT_TREATMENT successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'entry_date':  
                                        last_visit = input_date_last_visit()
                                        check_in = last_visit.split('/')
                                        check_out = patients[id_data_u][8].split('/')
                                        ci_y,ci_m,ci_d = int(check_in[0]),int(check_in[1]),int(check_in[2])
                                        co_y,co_m,co_d = int(check_out[0]),int(check_out[1]),int(check_out[2])
                                        valid_checkin = 10000 * ci_y + 100 * ci_m + ci_d
                                        valid_checkout = 10000 * co_y + 100 * co_m + co_d                                
                                        while valid_checkin > valid_checkout:
                                            print('entry_date cannot be after out_date!, the out_date is at ',patients[id_data_u][8])
                                            last_visit = input_date_last_visit()
                                            check_in = last_visit.split('/')
                                            ci_y,ci_m,ci_d = int(check_in[0]),int(check_in[1]),int(check_in[2])
                                            valid_checkin = 10000*ci_y + 100*ci_m + ci_d
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][7] = last_visit
                                            show_update()
                                            print('data ENTRY_DATE successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'out_date':  
                                        previous_date = patients[id_data_u][7] 
                                        discharged = input_date_discharged(previous_date)
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][8] = discharged
                                            show_update()
                                            print('data OUT_DATE successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                    elif id4 == 'category':  
                                        category = input_category()
                                        save_output = save_in_update()
                                        if save_output == 'y':
                                            patients[id_data_u][9] = category
                                            show_update()
                                            print('data CATEGORY successfully updated!')
                                            update3 = False
                                            break
                                        elif save_output == 'n':
                                            print('cancelled')
                                            update3 = False
                                            break
                                else:
                                    print('invalid input')
                        elif id3 == 'n':
                            pass
                    else:
                        print('data that you are looking for does not exist')
                        update2 == False
                    break
                if update1 == False:
                    print('reverted')
                    break
        if update_main == '2':
            print('back to main menu')   
            break 
            

#=====FUNCTION MAIN DELETE=====
def delete_data():
    display_data()
    print()
    id_delete_input = input("delete patient's full ID: ")
    while not id_delete_input.isnumeric():
        print('invalid, input must only be numeric')
        id_delete_input = input("delete patient's full ID: ")
    
    id_delete = int(id_delete_input)
    search_break = False
    for id_del in range(len(patients)):
        if patients[id_del][0] == id_delete: 
            display_table()
            print(f'      {patients[id_del][0]}\t{patients[id_del][1]}\t{patients[id_del][2]}\t{patients[id_del][3]}\t{patients[id_del][4]}\t{patients[id_del][5]}\t{patients[id_del][6]}\t{patients[id_del][7]}\t{patients[id_del][8]}\t{patients[id_del][9]}')
            print()
            search_break = True
            break

    if search_break == True:
        while True:
            delete_d = input("Are you sure you want to delete this patient's data? (press y or n)")
            if delete_d == 'y' or delete_d =='yes':
                del patients[id_del]
                print('data deleted!')
                break
            elif delete_d == 'n' or delete_d == 'no':
                print('cancelled!')
                break
            else: 
                print('invalid input')   
    else:
        print('data is not found')

#=====FUNCTION MAIN MENU=====
def main_menu():
    while True:
        menu()
        option = input('choose your option from 1 to 6: ')
        if option == '1':
            main_display_data()
        elif option == '2':
            add_data()
        elif option == '3':
            delete_data()
        elif option == '4':
            update_data()
        elif option == '5':
            authority_access()
        elif option == '6':
            print('Thank you, have a nice day, keep healthy!')
            break
        else: 
            print('input menu yang anda masukkan salah')
main_menu()




