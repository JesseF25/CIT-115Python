#Compunding Interest-Jesse Ferguson
#

#input
principal_investment =float(input('Enter starting principal: '))
#R=Rate
R= float(input('Annual interest rate: '))
#T=number of periods
T = float(input('How many times per year is the interest componded? '))

PV = float(principal_investment)
#M = compounding
M = float(input('How many years will the account earn interest? '))

#conversion 
#FV= future_value
FV = principal_investment * (1+((R/100)/12))**(T*M)
# this comes our correct!!! 1,051.22
'''
FV =PV *(1+((R/100)/M))**(M*T)
#this comes out incorrect at 1,347.35

FV = 1000 *(1+((2.5/100) /12))**(12 * 2)
this is the equation with out the variables= 1,347.35
'''
#Output

#
print(f'At the end of {M} years you will have ${FV:,.2f} ')                          
#print (f'the number is {FV:.2f}')
