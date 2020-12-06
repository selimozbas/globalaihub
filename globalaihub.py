# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:48:27 2020

@author: selimozbas
@mail : selimozbas@gmail.com
"""

# GlobalAIHub, TurkishAIHub homework


ad = "Selim"
soyad = "Ozbas"



course = [] # Kurs listesi
my_course = [] # atanmis kurslar
exam = {} # sınav sonucları


def main():
    
    count=0

    while count<4:
        
        first_name = input("Enter your firstname...: ")
        last_name = input("Enter your lastname...: ")
    
        if first_name == ad and last_name == soyad:
            print('Welcome \n',first_name,"",last_name)
            
            add_course()
           
            
        elif first_name != ad or last_name != soyad:
            
            if count >= 3:
                print("\nPlease try again later")
                break
            else:
                print("\nThe firstname or lastname is wrong!!! ")
                count+=1
                

def add_course():
    
     
    count=0
    
    while count<5:
        add_course = input("Enter the course...: ")
        course.append(add_course)
        count+=1
        
    print("You can take following courses")
    print(course)
    
    course_pcs = int(input("Please enter how mnany take courses..: "))
    
    i = 0
    
    if course_pcs > 2:
             
        while i < course_pcs :
            select = input("Please choice the course...: ")
            
            if select in course:
                my_course.append(select)
                i+=1
                
            else:
                print("Cannot find the course in the list") 

        exam_of_course()

    else:
        result("You failed in class")
        
        


def exam_of_course():
    
    print("You can take an exam from following courses")
    print(my_course)
 
    choice_course = input("Which course exams will you take..: ")
           
    if choice_course in my_course:
        
        print("hesaplamay geciyiroz")
        midterm_exam = float(input ("Please enter midterm exam result of the course...:"))
        exam["Midterm Exam"] = midterm_exam
        final_exam = float(input("Please enter final exam result of the_course...:"))
        exam["Final Exam"] = final_exam
        project = float(input("Please enter project result of  the course...:"))    
        exam["Project"] = project
        
    else:
        print("Please select a course from assigned list")
        
    
    result = (exam["Midterm Exam"] * 0.3) + (exam["Final Exam"] * 0.5) + (exam["Project"] * 0.2)
    print("Exam result..:", result)
    
    if result < 30:
        print("Lesson is FF")
        
    elif 30<=result<=50:
        print("Lesson is DD")
        
    elif 51<=result<=70:
        print("Lesson is CC")
        
    elif 71<=result<=90:
        print("Lesson is BB")
        
    else:
        print("Lesson is AA")
        
def result(text):
    
    result = text
    return result
    exit()
    main()

    
main()


    




