import matplotlib.pyplot as plt 
class Monthly_Sales:
    def __init__(self,months,sales):
        self.months=months
        self.sales=sales

    def main_function(self):
        try:
            plt.plot(self.months,self.sales,color="blue",linestyle='--',linewidth=2,marker='o',label="2025 sales")
            plt.title("===Monthly Sales Tracker===")
            plt.xlabel("---Months---")
            plt.ylabel("---Sales Of Each Month---")
            plt.legend()
            plt.grid()
            plt.xticks([1,2,3,4],["Jan","Feb","Mar","Apr"])
            plt.show()
        except Exception as e:
            print("ERROR : ",e) 

months = [1, 2, 3, 4]
sales = [150, 200, 250, 300]  
tracker=Monthly_Sales(months,sales)
tracker.main_function()             

                

