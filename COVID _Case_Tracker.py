import matplotlib.pyplot as plt 
class Covid_Case:
    def __init__(self,weeks,cases):
        self.weeks=weeks
        self.cases=cases


    def main_fun(self):
        try:
            plt.plot(self.weeks,self.cases,color='blue',marker='o',linestyle='--',linewidth=2,label="20-25 COVID CASES")
            plt.title("COVID Case Tracker")
            plt.xlabel("-Weeks-")
            plt.ylabel("-Cases-")
            plt.legend()
            plt.grid()
            plt.xticks([1,2,3,4,5],['W1','W2','W3','W4','W5'])
            plt.show()
        except Exception as e:
            print(f"❌ ERROR : {e}") 

weeks = [1, 2, 3, 4, 5]
cases = [100, 200, 400, 300, 150]                   
    
tracker=Covid_Case(weeks,cases)
tracker.main_fun()    