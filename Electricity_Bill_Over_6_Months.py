import matplotlib.pyplot as plt
class Electricity_Bill:
    def __init__(self,units,bills):
        self.units=units
        self.bills=bills

    def main_fun(self):
        try:
            plt.plot(self.units,self.bills,color="red",marker='o',linestyle='--',linewidth=2,label="6 Month bill")
            plt.title("===Electricity Bill Over 6 Months===")
            plt.xlabel("--UNITS--")
            plt.ylabel("--BILLS--")
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e :
            print(f"❌ ERROR : {e}")      


units = ["350/JAN", "400/FEB", "380/MARCH", "420/APRIL", "410/MAY", "390/JUNE"]
bills = [3500, 4000, 3900, 4300, 4200, 4050]              
bill=Electricity_Bill(units,bills)
bill.main_fun()
        
    

