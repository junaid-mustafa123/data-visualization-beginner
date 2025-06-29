
import matplotlib.pyplot as plt 
class Student_Marks:
    
    def __init__(self,subjects,student1,student2):
        self.subjects=subjects
        self.student1=student1
        self.student2=student2

    def student(self):
        try:
            plt.plot(self.subjects,self.student1,color='red',linestyle="--",marker='o',linewidth=2,label="Result 2025")
            plt.plot(self.subjects,self.student2,color='blue',marker='o',linestyle='--',linewidth=2,label="Result 2025")
            plt.title("****Student1 Marks Comparison***")
            plt.xlabel("***SUBJECTS***")
            plt.ylabel("***MARKS***")
            plt.xticks([1,2,3,4],['Math', 'Science', 'English', 'CS'])
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print("ERROR : ",e)  


subjects = [1, 2, 3, 4]
student1 = [85, 90, 75, 80]
student2 = [78, 88, 82, 85]
camparison=Student_Marks(subjects,student1,student2)
camparison.student()
