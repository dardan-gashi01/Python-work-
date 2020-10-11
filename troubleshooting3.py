#task 3
#troubleshooting
#solutions for phone 
file = open("phone_solutions.txt" , "w")
file.write("01 get your screen repaired\n")
file.write("02 restart your phone\n")
file.write("03 Take everything out of your phone and put it in a bag of rice for 24-36 hours\n")
file.write("04 Charge your phone and check if it works if not then send your phone to us and we will fix it\n")
file.write("05 Update your phone software\n")
file.close()

file = open("laptop_solutions.txt" , "w")
file.write("01 turn laptop off and on\n")
file.write("02 make sure your laptop is connected to a power source\n")
file.write("03 hold the power button for 5 seconds to reset your laptop\n")
file.write("04 raise your laptop onto a lifted surface\n")
file.write("05  \n")
file.close()


def choice():
   device = input("""what device are you having a problem with?
                       1)Phone 2)Laptop""")
   if "1" in device or "phone" in device or "Phone" in device:
       phone()
   elif "2" in device or "laptop" in device or "Laptop" in device:
       laptop()
   else:
       choice()


def phone():
    with open("phone_solutions.txt" , "r") as a_file:
        phone_line = a_file.readlines()

    question1_a = input("""what type of phone do you have?
                       1)apple  2)android """)
    if "1" in question1_a or "apple" in question1_a or "Apple" in question1_a:
        question_apple1 = input("""which model of phone is it?
                                1)IPhone5 2)Iphone5s or c 3)Iphone6 4)Iphone6s """)
        question_apple2 = input("""how much memory do you have on your phone?
                                1)8GB  2)16GB  3)32GB 4)64GB 5)128GB  """)
        question_apple_problem = input("what is wrong with your phone?")
        if "cracked" in question_apple_problem or "shattered" in question_apple_problem or "glass" in question_apple_problem or "screen" in question_apple_problem:
            print(phone_line[0])
        elif  "laggy" in question_apple_problem or "frozen" in question_apple_problem:
            print(phone_line[1])
        elif "wet" in question_apple_problem or "water" in question_apple_problem or "lake" in question_apple_problem or "river" in question_apple_problem:
            print(phone_line[2])
        elif "display" in question_apple_problem or "blank" in question_apple_problem:
            print(line[3])
        elif "access" in question_apple_problem or "features" in question_apple_problem:
            print(line[4])
        else:
            from random import randint
            print(randint(1000000,9999999))
            print("this is your case number")


    elif "2" in question1_a or "android" in question1_a or "Android" in question1_a:
        question_android1 = input("""what brand phone do you have?
                                  1)Samsung 2)1+ 3)HTC """)
        question_android2 = input("""how much memory does it have?
                                  1)8GB  2)16GB  3)32GB 4)64GB 5)128GB  """)
        question_android_problem = input("what is wrong with your phone? ")
        if "cracked" in question_android_problem or "shattered" in question_android_problem or "glass" in question_android_problem or "screen" in question_android_problem:
            print(phone_line[0])
        elif  "laggy" in question_android_problem or "frozen" in question_android_problem:
            print(phone_line[1])
        elif "wet" in question_android_problem or "water" in question_android_problem or "lake" in question_android_problem or "river" in question_android_problem:
            print(phone_line[2])
        elif "display" in question_android_problem or "blank" in question_android_problem:
            print(line[3])
        elif "access" in question_android_problem or "features" in question_android_problem:
            print(line[4])
        else:
            from random import randint
            print(randint(1000000,9999999))
            print("this is your case number")

def laptop():
    with open("laptop_solutions.txt" , "r") as b_file:
        laptop_line = b_file.readlines()
        question1_b = input("""what software laptop do you have?
                               1)MAC OS  2)windows  """)
        if "1" in question1_b or "MAC" in question1_b or "MAC OS" in question1_b or "mac os" in question1_b or "mac" in question1_b:
           question_mac1 = input(""" which model of a mac do you have?
                                     1)mac book pro  2)mac book  3)mac  """)
           question_mac2 = input(""" how much ram does your mac have have?
                                    1)4GB  2)8GB  3)16GB   """)
           question_mac_problem = input("what is wrong with your mac """)
           if "laggy" in question_mac_problem or "frozen" in question_mac_problem:
              print (laptop_line[0])
           elif "turn on" in question_mac_problem or "power" in question_mac_problem:
              print (laptop_line[1])
           elif "os" in question_mac_problem or "not responding" in question_mac_problem:
              print (laptop_line[2])
           elif "heat" in question_mac_problem or "over heat" in question_mac_problem:
              print(laptop_line[3])
           else:
               from random import randint
               print(randint(1000000,9999999))
               print("this is your case number")


        elif "2" in question1_b or "windows" in question1_b or "Windows" in question1_b:
            question_windows1 = input("""what model of a windows laptop do you have?
                                  1)samsung 2)dell 3)toshiba """)
            question_windows2 = input("""how much memory does it have?
                                  1)8GB  2)16GB  3)32GB 4)64GB 5)128GB  """)
            question_windows_problem = input("what is wrong with your phone? ")
            if "laggy" in question_windows_problem or "frozen" in question_windows_problem:
                 print (laptop_line[0])
            elif "turn on" in question_windows_problem or "power" in question_windows_problem:
                 print (laptop_line[1])
            elif "os" in question_windows_problem or "not responding" in question_windows_problem:
                 print (laptop_line[2])
            elif "heat" in question_windows_problem or "over heat" in question_windows_problem:
                 print(laptop_line[3])


            else:
               from random import randint
               print(randint(1000000,9999999))
               print("this is your case number")


choice()
