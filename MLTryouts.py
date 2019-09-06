import csv
import tkinter as t

mortgageAmount = 0
mortgageNumber = 0
rentAmount = 0
rentNumber = 0
ownAmount = 0
ownNumber = 0
currentID = 0
currentType = ""
avgMortgageAmount = 0
avgRentAmount = 0
avgOwnAmount = 0

tab1V = "0"
tab2V = "0"
tab3V = "0"
tab4V = "0"
tab5V = "0"
tab6V = "0"
tab7Max = "0"

mortgageRatio = 0.2
rentRatio = 0.4
ownRatio = 0.5

with open('home_ownership_data.csv') as id:
    idFinder = csv.reader(id)

    for row in idFinder:
        if row[1] == 'MORTGAGE':
            mortgageNumber += 1
            currentType = "M"
        elif row[1] == 'RENT':
            rentNumber += 1
            currentType = "R"
        elif row[1] == 'OWN':
            ownNumber += 1
            currentType = "O"

        currentID = row[0]
        with open('loan_data.csv') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == currentID:
                    if currentType == 'M':
                        mortgageAmount += int(row[1])
                    elif currentType ==  'R':
                        rentAmount += int(row[1])
                    elif currentType == 'O':
                        ownAmount += int(row[1])
                    break

avgMortgageAmount = mortgageAmount/mortgageNumber
avgRentAmount = rentAmount/rentNumber
avgOwnAmount = ownAmount/ownNumber

print("Home Ownership,  Average Loan Amount \nMortgage: " + str(avgMortgageAmount) +
          "\nRent: " + str(avgRentAmount) + "\nOwn: " + str(avgOwnAmount))

tab7Max = avgMortgageAmount

if avgRentAmount > tab7Max:
    tab7Max = avgRentAmount

if avgOwnAmount > tab7Max:
    tab7Max = avgOwnAmount

temp = tab7Max
magnitude = 1

while temp > 100:
    temp = temp/10
    magnitude *= 10

temp = int(temp)
temp += 1
tab7Max = temp * magnitude

tab1V = int(tab7Max/7)
tab2V = tab1V*2
tab3V = tab1V*3
tab4V = tab1V*4
tab5V = tab1V*5
tab6V = tab1V*6

mortgageRatio = avgMortgageAmount/tab7Max
rentRatio = avgRentAmount/tab7Max
ownRatio = avgOwnAmount/tab7Max

root = t.Tk()

w = t.Canvas(root, height=700, width=1000)
w.pack()

frame = t.Frame(root)
frame.place(relwidth=1,  relheight=1)

title = t.Label(frame, text="Average loan amounts for different home ownership styles")
title.place(relx=0.5, rely=0, anchor='n')

bottomTitle= t.Label(frame, text="Home Ownership")
bottomTitle.place(relx=0.5, rely=1, anchor='s')

sideTitle = t.Label(frame, text="Average \nLoan \nAmount\n ($)")
sideTitle.place(relx=0, rely=0.5, anchor='w')

zero = t.Label(frame, text="0")
zero.place(relx=0.15, rely=0.9, anchor='se')

tab1 = t.Label(frame, text=tab1V)
tab1.place(relx=0.15, rely=0.8, anchor='se')

tab2 = t.Label(frame, text=tab2V)
tab2.place(relx=0.15, rely=0.7, anchor='se')

tab3 = t.Label(frame, text=tab3V)
tab3.place(relx=0.15, rely=0.6, anchor='se')

tab4 = t.Label(frame, text=tab4V)
tab4.place(relx=0.15, rely=0.5, anchor='se')

tab5 = t.Label(frame, text=tab5V)
tab5.place(relx=0.15, rely=0.4, anchor='se')

tab6 = t.Label(frame, text=tab6V)
tab6.place(relx=0.15, rely=0.3, anchor='se')

tab7 = t.Label(frame, text=tab7Max)
tab7.place(relx=0.15, rely=0.2, anchor='se')

graph = t.Frame(frame)
graph.place(relx=0.2, rely=0.9, relheight=0.73, relwidth=0.7, anchor='sw')

column1 = t.Frame(graph, bg='red')
column1.place(relx=0, rely=1, relwidth=0.3, anchor='sw', relheight=mortgageRatio)

column2 = t.Frame(graph, bg='green')
column2.place(relx=.35, rely=1, relwidth=0.3, anchor='sw', relheight=rentRatio)

column3 = t.Frame(graph, bg='blue')
column3.place(relx=0.7, rely=1, relwidth=0.3, anchor='sw', relheight=ownRatio)

mortgageTitle = t.Label(frame, text="Mortgage")
mortgageTitle.place(relx=0.3, rely=0.91, anchor='n')

rentTitle = t.Label(frame, text="Rent")
rentTitle.place(relx=0.55, rely=0.91, anchor='n')

ownTitle = t.Label(frame, text="Own")
ownTitle.place(relx=0.8, rely=0.91, anchor='n')

root.mainloop()


