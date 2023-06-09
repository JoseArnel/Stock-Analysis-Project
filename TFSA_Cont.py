import math
from os import system, name
import datetime
import csv
import pandas as pd
from matplotlib import pyplot as plt

def clear():
    _ = system('clear')

def date():
    print(datetime.date.today())

def write_csv(n, year, value):
  with open('investment.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "value"])
    for i in range(0,n):
      writer.writerow([year, value,])

def TFSA():
    limit = [5000, 5000, 5000, 5000, 5500, 5500, 1000, 5500, 5500, 5500, 6000, 6000, 6000, 6000, 6500]
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    age = int(input("Age: ")) 
    if (age < 18):
        print("Too young to invest")
    if (age > len(limit) + 18):
        acc = sum(limit)
        print(f'${acc:,d}')
        return 0
    age = age - 18
    acc = 0 
    for i in range(int((len(limit)) - age - 1), len(limit)):
        acc += limit[i]
    print(f'${acc:,d}')

def interest_calc(calc, pv, i, n, pmt):
  with open('interest.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Balance", "Principal", "Interest"])
    principal_s = pv 
    balance_s = pv 
    principal_e = pv
    clear()
    if (calc == 'y'):
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            principal_e = principal_s - pmt
            print("   start_principal " + " start_balance" +   " interest " + " end_balance " + " end_principal ")
            print(str(x) + " " +"{:.2f}".format(principal_s) +  "        " + "{:.2f}".format(balance_s) +  "     " + "{:.2f}".format(p_i)  + "  " + "{:.2f}".format(fv) +  "    " + "{:.2f}".format(principal_e))
            # print("principal:{:.2f}".format(principal_s) + "start balance::{:.2f}".format(balance_s) +   " interest:{:.2f}".format(p_i) + "end balance:{:.2f}".format(fv) + "end balance:{:.2f}".format(principal_e))
            writer.writerow([x, round(fv), round(principal_s), round(fv-principal_s)])
            principal_s = principal_s - pmt
            balance_s = fv
            pv = fv
        print(" ")
    else:
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            pv = fv
    return(fv)

# total interests
#Sum of all periodic payments
def tvm_calc(calc, pv, i, n, pmt):
  with open('tvm1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "PV", "PMT", "Interest", "FV"])
    principal_s = pv 
    balance_s = pv 
    principal_e = pv
    clear()
    if (calc == 'y'):
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            principal_e = principal_s - pmt
            print("   start_principal " + " start_balance" +   " interest " + " end_balance " + " end_principal ")
            print(str(x) + " " +"{:.2f}".format(principal_s) +  "        " + "{:.2f}".format(balance_s) +  "     " + "{:.2f}".format(p_i)  + "  " + "{:.2f}".format(fv) +  "    " + "{:.2f}".format(principal_e))
            writer.writerow([x, round(pv), round(-pmt), round(p_i), round(-fv)])
            principal_s = principal_s - pmt
            balance_s = fv
            pv = fv
        print(" ")
    else:
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            pv = fv
    return(fv)
        
def tvm_graph(calc, pv, i, n, pmt):
  with open('tvm_graph.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "PV", "SumofPMT", "AccumulatedInterest", "FV"])
    principal_s = pv 
    balance_s = pv 
    principal_e = pv
    sum_pmt = 0
    sum_int = 0
    clear()
    if (calc == 'y'):
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            principal_e = principal_s - pmt
            print("   start_principal " + " start_balance" +   " interest " + " end_balance " + " end_principal ")
            print(str(x) + " " +"{:.2f}".format(principal_s) +  "        " + "{:.2f}".format(balance_s) +  "     " + "{:.2f}".format(p_i)  + "  " + "{:.2f}".format(fv) +  "    " + "{:.2f}".format(principal_e))
            sum_pmt = pmt + sum_pmt
            sum_int = p_i + sum_int
            writer.writerow([x, round(pv), round(-sum_pmt), round(sum_int), round(-fv)])
            principal_s = principal_s - pmt
            balance_s = fv
            pv = fv
        print(" ")
    else:
        for x in range(1,n+1):
            p_i= pv * i
            fv = pv + p_i - pmt
            pv = fv
    return(fv)

def interest_visualizer():
    data = pd.read_csv('interest.csv')
    plt.plot(data.Balance / 10**6)
    plt.plot(data.Principal / 10**6)
    plt.plot(data.Interest / 10**6)
    plt.legend(['Balance', 'Interest', 'Principal'])
    plt.xlabel("Year")
    plt.ylabel("$(Millions)")
    plt.show()

def tvm_visualizer():
    data = pd.read_csv('tvm_graph.csv')
    plt.plot(data.PV / 10**6)
    plt.plot(data.SumofPMT / 10**6)
    plt.plot(data.AccumulatedInterest / 10**6)
    plt.plot(data.FV / 10**6)
    plt.legend(['PV', 'SumofPMT', 'AccumulatedInterest', 'FV'])
    plt.xlabel('Year')
    plt.ylabel('$(Millions)')
    plt.show()

def Milli():
    target = 1000000
    pv = int(input("Principal Value($): "))
    i = float(input("Interest(%): "))/100
    pmt = int(input("Contributions($): ")) * -1
    calc = input("Would you like to show the calculations (y/n) ")
    count = 0
    for x in range(100):
        count += 1
        fv = tvm_graph(calc, pv, i, count, pmt)
        if (fv > target):
            print("It will take you " + str(count) + "years to be a millionaire by: " + str(count+18) + " \n")
            break

TFSA()

# tvm_calc('y', 50000, 0.07, 31, -6000)

# def PorfolioAlloc():
#    value = int(input("Protfolio Value($): "))

# for fun 
# EPS, Stock Breka down Soo called.
# Implement Graph, Pyhton, Database,
# Students Loans