# class Classone:
#      def __init__(self,name,grades):
#         self.name=name
#         self.grades=grades
# objectone=Classone("aditi",[123,25,46])
# print(objectone.name)
# print(objectone.grades) 
# # #accessing the method of a class using an object
# # class classtwo:
# #     def __init__(self,audio,video):
#         self.audio=audio
#         self.video=video
#         self.kratos=23

# # objecttwo=classtwo(5,6)
# # print(objecttwo.kratos)

 list1=[1,2,4,5,6,6,2,3,1]
 print(list1)

 list1=set(list1)
 print(list1)
 print(list1)
 print(list1)
 a=int(input("enter: "))
 print(a,list1)


# # Question:
# # Create a class called "Student" with the following attributes: "name", "age", and "grades" (a list of integers).
# # Implement a method in the class called "average_grade" that calculates and returns the average grade of the student.

# # Create a list of three Student objects with different names, ages, and grades.
# # Use a loop to iterate through the list and print the name, age, and average grade for each student.
# # Additionally, identify and print the student with the highest average grade.

class Student:
    def __init__(self,name,age,grades):
    self.name=name
    self.age=age
    self.grades=grades
    def average_grade:
        sum=0
        for i in self.grade:
            sum=sum+i
        return sum/len(self.grade) if len(self.grade)>0 else 0

student1=Student(["Aditi",14,[45,25,78]])
student2=Student(["Abhay",14,[70,80,80]])
student3=Student(["kartik",15,[90,99,19]])
all_students=[student1,student2,student3]

for i in all_students:
    avg_grade=i.average_grade
    print(f"{i.name} \nage: {i.age} \naverage_student: {avg_grade}")
    if avg_grade>


