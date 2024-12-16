# Inter Planetary Weights by Jesse Ferguson
# input
# Get the user's first name.
first_name = input('Enter your first name: ')
#
sName = (first_name) 
print ('Hello', first_name)
#input
#get Earth Weight
iWeight = float(input('Please enter your weight?' ))
# saftey check weight will be 70.5
# Calculate

fMERCURY = 0.38 

fVENUS = 0.91 

fMOON = 0.165

fMARS = 0.38

fJUPITER = 2.34

fSATURN = 0.93

fURANUS = 0.92

fNEPTUNE =1.12

fPLUTO = 0.066
# Output
# These are the the weights on planetts on our soloar system.

print (sName, 'here are your weights on our Solar Systems planets: ')
print (f'weight on MERCURY {fMERCURY *iWeight:12.2f}')
print (f'weight on VENUS   {fVENUS *iWeight:12.2f}')
print (f'weight on MOON    {fMOON *iWeight:12.2f}')
print (f'weight on MARS    {fMARS *iWeight:12.2f}')
print (f'weight on JUPITER {fJUPITER *iWeight:12.2f}')
print (f'weight on SATURN  {fSATURN *iWeight:12.2f}')
print (f'weight on URANUS  {fURANUS *iWeight:12.2f}')
print (f'weight on NEPTUNE {fNEPTUNE *iWeight:12.2f}')
print (f'weight on PLUTO   {fPLUTO *iWeight:12.2f}')



