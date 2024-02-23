def calc(n):
    months = n//30
    days = n%30
    year = n//365
    print("No of Months in",n,"days is",months)
    print("No of days in" , n , "days is" , days)
    print("No of year in" , n , "days is" , year)


n=int(input("Enter the No of days"))
calc(n)