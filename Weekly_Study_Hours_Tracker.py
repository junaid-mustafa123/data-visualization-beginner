import matplotlib.pyplot as plt
class Weekly_Study_Hours:
    def __init__(self,days,hours):
        self.days=days
        self.hours=hours


    def weekly_function(self):
        try:
            plt.plot(self.days,self.hours,marker='o',linewidth=2,linestyle='--',label="Weekly Study Hours")
            plt.title("===Weekly Study Hours Tracker===")    
            plt.xlabel("===DAYS===")
            plt.ylabel("===HOURS===")
            plt.legend()
            plt.grid()
            plt.xticks([1,2,3,4,5,6,7],["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
            plt.show()

        except Exception as e:
            print(f"✖️ ERROR : {e}")    
days = [1, 2, 3, 4, 5, 6, 7]
hours = [3, 4, 5, 6, 4, 2, 7]
        
hours=Weekly_Study_Hours(days,hours)
hours.weekly_function()    