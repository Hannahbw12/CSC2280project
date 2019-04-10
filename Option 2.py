import csv

#def analyze(document):
document=input("Enter document name:")
file = open(document)
filename = csv.reader(file)
    #options = input ("Options:\nGeneral- general statistics on data.\nCrime- for statistics categorized by types of crime.\nDistrict- for statistics categorized by District.\nEnter one of the options:")
    #if options == "crime":
crime_count=0
arrest_count=0
domestic_count=0
#n=0
    
for row in filename:
    if row[1] == "true" or row[1] == "false":
        crime_count += 1
    if row[1] == "true":
        arrest_count += 1
    if row[2] == "true":
        domestic_count += 1
    #if row[4] == "16" and row[1] == "false":
        #n+=1
           
print("The number of reported crimes:" , crime_count)
print("The number of arrests:" , arrest_count)
print("The number of cases involving domestic violence:" , domestic_count)

#

part2 = input("Would you like to see crimes per district (y/n):")
if part2.lower() == "y":
    district_select = input("Select a district (1-25):")
elif part2.lower() == "n":
    quite = input("Would you like to quite?: (y/n)")
        
elif part2.lower() != "y" and part2.lower() != "n":
    stay_return = input("Would you like to stay in this option or return to the main page (stay/return):")
    
    #loop it back to original question 
    



#print("The number of reported crimes in district 17:" , d17_totalcount)
                 
#d17_totalcount=0            
#for row in filename:
    #if row[4] == "16":
    #d17_totalcount += 1
#print("The number of reported crimes in district 17:" , d17_totalcount)
