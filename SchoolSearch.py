import time

#головне меню
def main_menu():
        print("----------Menu----------")
        print("Student")
        print("Teacher")
        print("Classroom")
        print("Bus")
        print("Quit")
        print("------------------------")
        
        option = input("Choose one from the suggested options(e.g S(tudent)): ").upper() 
    
        return option
        
    #Функція в котру передається вибір користувача і два файли
    #Базуючись на виборі користувача викликається потрібна функція пошуку   
def school_search(option,F1,F2):
    if(option == "S"):
        surname = input("Enter student's surname: ").upper()
        print("\nWould you like to find info based only on surname or based on surname and bus route?")
        print("1. Find based on surname\n2. Add bus ")
        subOption = input(("Enter 1 or 2: "))
        if (subOption == "1" or subOption == "2"):
            surname_search(F1,surname, subOption)
        else :
            print("Invalid option. Try again")
    elif (option == "T"):
        surname = input("Enter teacher's surname: ").upper()
        print("\nWhat kind of information are you looking for?")
        print("1. "+ (surname.lower()).capitalize() + "'s list of students \n2. Information about "  + (surname.lower()).capitalize())
        subOption = input(("Enter 1 or 2: "))
        if (subOption == "1" or subOption == "2"):
            teacher_search(F2,F1,surname, subOption)
        else :
            print("Invalid option. Try again")
    elif (option == "B"):
        busNumber = input("Enter bus number: ")
        bus_search(F1, busNumber)
    elif (option == "C"):
        classromNumber = input("Enter classroom number: ")
        classroom_search(F1, classromNumber)
    else:
        print("\nUnknown option. Try Again.\n")
       
      #пошук за прізвищем студента          
def surname_search(fileName, studentSurname, subOption):
    if(subOption == "2"):
        busNum = input("\nEnter a bus number: ").upper();  #додатковий пошук і за автобусом
    
    st = time.time()   #час початку пошуку
    with open(fileName, "rt") as f: #відкриваємо файл
        print("\nList of students whose surname is: " + (studentSurname.lower()).capitalize() + "\n")  
        for x in f: #проходимося по рядкам файду
            if studentSurname.strip() in x:  #умова чи присутнє прізвище в поточному рядку файлу
                    values = x.split(",")  #зберігаємо окремі дані в масив
                    if(subOption == "1"):
                        print("Student: " + values[0]+ " " + values [1]) 
                        print("Bus: " + values[4].strip())
                        print("Grade: " + values[2])
                        if(values[3] == 0):
                            print("Kindergarden")  
                        else:
                            print("Classroom: " + values[3])
                        print("\n")
                    elif studentSurname.strip() and busNum in x:
                        print("Student: " + values[0]+ " " + values [1])
                        print("Bus: " + values[4])
                        print("\n")
                        
        elapsed_real_time(st) 
                    
            #пошук за прізвищем вчителя  
def teacher_search(fileName1,fileName2, teacherSurname,subOption):
    st = time.time()   #час початку пошуку
    with open(fileName1, "rt") as f1:  #відкриваємо файл teachers.txt
        for x in f1: #проходимося по рядкам файлу
            if teacherSurname.strip() in x:   #умова чи присутнє прізвище в поточному рядку файлу
                    values = x.split(",")
                    if(subOption == "1"):
                        print("\nTeacher: " + values[1]+ " " + values [0])
                        print("Classroom: " + values[2])
                        with open(fileName2, "rt") as f2:  #відкриваємо файл list.txt
                            for x in f2:
                                if values[2].strip() in x:
                                    valuesStudent = x.split(",")
                                    print("Student: " + valuesStudent[0]+ " " + valuesStudent[1])
                            print("-------------------------")
                    elif(subOption == "2"):  
                        print(values[1]+ " " + values [0] + " teaches at class №" + values[2])
        elapsed_real_time(st)

#пошук за номером автобусу
def bus_search(fileName, busNumber):
    st = time.time()   #час початку пошуку
    if (busNumber == 0):
        print("\nList of students who don't use a bus: ")
        with open(fileName, "rt") as f:     #відкриваємо файл
            for x in f:                 #проходимося по рядкам файлу
                if busNumber in x:   #умова чи присутній номер автобусу в поточному рядку файлу
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
                    print("Classroom: " + values[3] + "\n")
    else:
        print("\nBus: "+ busNumber)
        with open(fileName, "rt") as f:
            for x in f:
                if busNumber in x:
                    values = x.split(",")
                    print("Student: " + values[0]+ " " + values [1])
                    print("Classroom: " + values[3] + "\n")        
            
    elapsed_real_time(st)
                
          
       #пошук за номером класу  
def classroom_search(fileName, classromNumber):
    st = time.time()   #час початку пошуку
    if(classromNumber == "0"):
        print("Children who are still in kindergarden: ")
    else:
        print("\nStudents of Classroom №" + classromNumber +":")
    with open(fileName, "rt") as f:     #відкриваємо файл
        for x in f:                     #проходимося по рядкам файлу
            if classromNumber in x:   #умова чи присутній номер класу в поточному рядку файлу
                    values = x.split(",")
                    if(classromNumber == "0"):
                        print("Child: " + values[0]+ " " + values [1])
                    else:
                       print("Student: " + values[0]+ " " + values [1])
        elapsed_real_time(st)       
                         
       #функція котра вираховує час пошуку
def elapsed_real_time(startTime):
    endTime = time.time() 
    elapsed_time = endTime - startTime 
    print('\nExecution time:', elapsed_time, 'seconds')  
    
 
#Ініціалізація змінних з іменами файлів
F1 = 'list.txt' 
F2 = 'teachers.txt'

#Цикл котрий постійно викликає меню допоки користувач не вийде
while(True):
    option = main_menu() 
    if option == "Q":
        print('\nДо побачення')  
        break
    else:
        school_search(option,F1,F2) 
       
