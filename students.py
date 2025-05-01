import numpy as np
import time
students = np.array(["ahmed","sara","mohamed","leila","yousef"])
subjects = np.array(["Math","Physics","English","History"])
grades = np.array([
 [80, 70, 90, 60],
 [85, 75, 95, 70],
 [60, 65, 70, 75],
 [90, 95, 85, 80],
 [70, 80, 75, 85]]) 
siz = np.size(subjects)
students_size = np.size(students)
#=========================================
def calcmean () : 
  n=0
  a = False
  search =input("please enter the name of the student you want to search for :")
  for i in range(students_size)  :
    if students[i].lower() == search.lower()  :
      a = True
      n=i
      break
  if a :
    print (f"the mean grade for ** {search} ** is {int(round(np.mean(grades[n])))} grade.")
    time.sleep(3)
  else :  
    print("this student is not here to search for or invalid input.")  
    time.sleep(3)

#====================================
def thewholegrades () :
  n=0
  a = False
  search =input("please enter the name of the student you want to know the sum of the grades for him :")
  for i in range(students_size)  :
    if students[i].lower()== search.lower()  :
      a = True
      n=i
      break
  if a :
        print(f"the whole grades for ** {search} ** is {np.sum(grades[n])} grade.")
        time.sleep(3)
  else :
    print("this student is not here to search for or invalid input .") 
    time.sleep(3) 
#============================
def thefirst () :
  thegradeofthefirststudent = 0
  n=0
  for i in range(students_size) :
    if np.sum(grades[i]) > thegradeofthefirststudent:
        thegradeofthefirststudent= np.sum(grades[i])
        n=i
  print(f"the first student is **** {students[n]} ****.")
  time.sleep(3)
#============================
def thelast () :
  thegradeofthelasttstudent = grades[0].sum() 
  n=0
  for i in range(students_size)  :
    if np.sum(grades[i])< thegradeofthelasttstudent :
        thegradeofthelasttstudent= grades[i].sum()
        n=i
  print(f"the last student is !!! {students[n]} !!!")
  time.sleep(3)
#============================

def search () :
  n=0
  a = False
  search =input("please enter the name of the student you want to search for :")
  for i in range(students_size)  :
    if students[i].lower()== search.lower()  :
      a = True
      n=i
      break
  if a :
   x =  students.tolist().index(search)
   print (f"  ***** {search}'s grades *****")
   for i in range (siz) :
        print (f" in {subjects[i] } his grade is {grades[n][i]}")
        time.sleep(3)
  else :
    print("this student is not here to search for or invalid input .")  
    time.sleep(3)      
#===================================================================

  
def percentage () :
  search =input("please enter the name of the student you want to know his percentage :")
  n=0
  a=False
  for i in range(students_size)  :
    if students[i].lower()== search.lower()  :
      n=i
      a = True
      break
  if a :
    
    print(f"the percentage for {search} is {round(grades[n].sum()/400*100)}%")
    time.sleep(3)
  else :
    print("this student is not here to search for or invalid input .")  
    time.sleep(3)
#============================
 
def calcstd () :
  search =input("please enter the name of the student you want to know the standard deviation for him :")
  n=0
  a=False
  for i in range(students_size)  :
    if students[i].lower()== search.lower() :
      n=i
      a = True
      break
  if a :
        print(f"the std for {search} is {round(np.std(grades[n]))}")
        time.sleep(3)
  else :
    print("this student is not here to search for or invalid input .")  
    time.sleep(3) 
#===========================================
while True :
  print("********* MENU *********")
  print("1_ calculate the mean for a student.")
  print ("2_ calculate the whole grades for a student.")
  print("3_ know the first student.")
  print("4_ know the last student.")
  print("5 calculate the std  for a student.")
  print("6_ calculate the pecentage for a student.")
  print("7_search for a student.")
  print("8_ Exit.")
  choice = input("please enter your choice \n ")
  if choice=="1" :
    calcmean ()
  elif choice == "2" :
    thewholegrades ()
  elif choice == "3":
    thefirst () 
  elif choice == "4" :
    thelast ()
  elif choice == "5" :
    calcstd ()
  elif choice == "6" :
    percentage ()
  elif choice == "7" :
     search ()
  elif choice == "8" :
    break
  else :
    print("please enter any number from the main menu .")
    time.sleep(3)
    continue
#======================================================================



