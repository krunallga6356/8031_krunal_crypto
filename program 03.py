
priciple = int(input("Enter the priciple amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))

def simple_interest(priciple, rate, time):
    return (priciple * rate * time) / 100

print("The simple interest is:", simple_interest(priciple, rate, time))
