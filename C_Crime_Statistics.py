import csv
def main():

    number = 4
    ##
    while number != 0:
        print("Instructions- Choose of of the following:\n 1 - for statistics based off of chosen district\n 2 - for statistics based off type of crime\n 0 - to quit\n")
        print("----------------------------------------------------------------------------")
        number = int(input("Enter Option Number:"))
        if number == 1:
            option2()
        elif number == 2:
            option3()
        elif number == 0:
            break
        else:
            print("Invalid Entry")
            number = int(input("\nEnter Option Number:"))

        
    

      
def option2():
    fileName= open('Crimes.csv')
    Csv_fileName = csv.reader(fileName)
    next(Csv_fileName, None)

    district = input("What district, 1-25, do you want specifics on? ")


    district_total = 0
    overall_total = 0
    overall_arrest_total = 0
    arrest_count = 0
    domestic_count = 0
    total_other_district = 0
    liquorD = 0
    robberyD = 0
    theftD = 0
    offense_involving_childrenD = 0
    assaultD = 0
    batteryD = 0
    burglaryD = 0
    sexual_assaultD = 0
    narcoticsD = 0
    criminal_damageD = 0
    weapons_violationD = 0
    deceptive_practiceD = 0
    homicideD = 0
    arsonD = 0
    criminal_trespassD = 0
    kidnappingD = 0
    intimidationD = 0

    liquorT = 0
    robberyT = 0
    theftT = 0
    offense_involving_childrenT = 0
    assaultT = 0
    batteryT = 0
    burglaryT = 0
    sexual_assaultT = 0
    narcoticsT = 0
    criminal_damageT = 0
    weapons_violationT = 0
    deceptive_practiceT = 0
    homicideT = 0
    arsonT = 0
    criminal_trespassT = 0
    kidnappingT = 0
    intimidationT = 0

    district_crime_total = 0
    liquorDC = 0
    robberyDC = 0
    theftDC = 0
    offense_involving_childrenDC = 0
    assaultDC = 0
    batteryDC = 0
    burglaryDC =0
    sexual_assaultDC = 0
    narcoticsDC = 0
    criminal_damageDC = 0
    weapons_violationDC = 0
    deceptive_practiceDC = 0
    homicideDC = 0
    arsonDC = 0
    criminal_trespassDC = 0
    kidnappingDC = 0
    intimidationDC = 0
       
    total_other_district = 0
    liquorTC = 0
    robberyTC = 0
    theftTC = 0
    offense_involving_childrenTC = 0
    assaultTC = 0
    batteryTC = 0
    burglaryTC = 0
    sexual_assaultTC = 0
    narcoticsTC = 0
    criminal_damageTC = 0
    weapons_violationTC = 0
    deceptive_practiceTC = 0
    homicideTC = 0
    arsonTC = 0
    criminal_trespassTC = 0
    kidnappingTC = 0
    intimidationTC = 0
    

    for row in Csv_fileName:
        overall_total += 1
        if row[8] == "true":
            overall_arrest_total += 1
            if int(row[11]) == int(district):
                district_total += 1
                if row[5] == "LIQUOR LAW VIOLATION":
                    liquorD +=1
                if row[5]== "ROBBERY":
                    robberyD += 1
                if row[5] == "THEFT" or row[5] == "MOTOR VEHICLE THEFT":
                    theftD += 1
                if row[5] == "OFFENSE INVOLVING CHILDREN":
                    offense_involving_childrenD += 1
                if row[5] == "ASSAULT":
                    assaultD += 1
                if row[5] == "BATTERY":
                    batteryD += 1
                if row[5] == "BURGLARY":
                    burglaryD +=1
                if row[5] == "CRIM SEXUAL ASSAULT" or row[5] == "SEX OFFENSE":
                    sexual_assaultD += 1
                if row[5] == "NARCOTICS":
                    narcoticsD += 1
                if row[5] == "CRIMINAL DAMAGE":
                    criminal_damageD += 1
                if row[5] == "WEAPONS VIOLATION":
                    weapons_violationD += 1
                if row[5] == "DECEPTIVE PRACTICE":
                    deceptive_practiceD += 1
                if row[5] == "HOMICIDE":
                    homicideD += 1
                if row[5] == "ARSON":
                    arsonD += 1
                if row[5] == "CRIMINAL TRESPASS":
                    criminal_trespassD += 1
                if row[5] == "KIDNAPPING":
                    kidnappingD += 1
                if row[5] == "INTIMIDATION":
                    intimidationD += 1
            else:
                total_other_district += 1
                if row[5] == "LIQUOR LAW VIOLATION":
                    liquorT +=1
                if row[5]== "ROBBERY":
                    robberyT += 1
                if row[5] == "THEFT" or row[5] == "MOTOR VEHICLE THEFT":
                    theftT += 1
                if row[5] == "OFFENSE INVOLVING CHILDREN":
                    offense_involving_childrenT += 1
                if row[5] == "ASSAULT":
                    assaultT += 1
                if row[5] == "BATTERY":
                    batteryT += 1
                if row[5] == "BURGLARY":
                    burglaryT +=1
                if row[5] == "CRIM SEXUAL ASSAULT" or row[5] == "SEX OFFENSE":
                    sexual_assaultT += 1
                if row[5] == "NARCOTICS":
                    narcoticsT += 1
                if row[5] == "CRIMINAL DAMAGE":
                    criminal_damageT += 1
                if row[5] == "WEAPONS VIOLATION":
                    weapons_violationT += 1
                if row[5] == "DECEPTIVE PRACTICE":
                    deceptive_practiceT += 1
                if row[5] == "HOMICIDE":
                    homicideT += 1
                if row[5] == "ARSON":
                    arsonT += 1
                if row[5] == "CRIMINAL TRESPASS":
                    criminal_trespassT += 1
                if row[5] == "KIDNAPPING":
                    kidnappingT += 1
                if row[5] == "INTIMIDATION":
                    intimidationT += 1
        if int(row[11]) == int(district):
            district_crime_total += 1
            if row[5] == "LIQUOR LAW VIOLATION":
                liquorDC +=1
            if row[5]== "ROBBERY":
                robberyDC += 1
            if row[5] == "THEFT" or row[5] == "MOTOR VEHICLE THEFT":
                theftDC += 1
            if row[5] == "OFFENSE INVOLVING CHILDREN":
                offense_involving_childrenDC += 1
            if row[5] == "ASSAULT":
                assaultDC += 1
            if row[5] == "BATTERY":
                batteryDC += 1
            if row[5] == "BURGLARY":
                burglaryDC +=1
            if row[5] == "CRIM SEXUAL ASSAULT" or row[5] == "SEX OFFENSE":
                sexual_assaultDC += 1
            if row[5] == "NARCOTICS":
                narcoticsDC += 1
            if row[5] == "CRIMINAL DAMAGE":
                criminal_damageDC += 1
            if row[5] == "WEAPONS VIOLATION":
                weapons_violationDC += 1
            if row[5] == "DECEPTIVE PRACTICE":
                deceptive_practiceDC += 1
            if row[5] == "HOMICIDE":
                homicideDC += 1
            if row[5] == "ARSON":
                arsonDC += 1
            if row[5] == "CRIMINAL TRESPASS":
                criminal_trespassDC += 1
            if row[5] == "KIDNAPPING":
                kidnappingDC += 1
            if row[5] == "INTIMIDATION":
                intimidationDC += 1
        else:
            total_other_district += 1
            if row[5] == "LIQUOR LAW VIOLATION":
                liquorTC +=1
            if row[5]== "ROBBERY":
                robberyTC += 1
            if row[5] == "THEFT" or row[5] == "MOTOR VEHICLE THEFT":
                theftTC += 1
            if row[5] == "OFFENSE INVOLVING CHILDREN":
                offense_involving_childrenTC += 1
            if row[5] == "ASSAULT":
                assaultTC += 1
            if row[5] == "BATTERY":
                batteryTC += 1
            if row[5] == "BURGLARY":
                burglaryTC +=1
            if row[5] == "CRIM SEXUAL ASSAULT" or row[5] == "SEX OFFENSE":
                sexual_assaultTC += 1
            if row[5] == "NARCOTICS":
                narcoticsTC += 1
            if row[5] == "CRIMINAL DAMAGE":
                criminal_damageTC += 1
            if row[5] == "WEAPONS VIOLATION":
                weapons_violationTC += 1
            if row[5] == "DECEPTIVE PRACTICE":
                deceptive_practiceTC += 1
            if row[5] == "HOMICIDE":
                homicideTC += 1
            if row[5] == "ARSON":
                arsonTC += 1
            if row[5] == "CRIMINAL TRESPASS":
                criminal_trespassTC += 1
            if row[5] == "KIDNAPPING":
                kidnappingTC += 1
            if row[5] == "INTIMIDATION":
                    intimidationTC += 1     

    print("\nTotal number of crimes in Chicago:", overall_total)    
    print("Total number of crimes for the district: ",district_crime_total)
    print("This district holds {0:0.4}".format((district_total / overall_total) * 100) ,"% of the crimes for Chicago \n")


    print("Number of each crime:")
    print(" Liquor Law Violations:",liquorDC)
    print(" Robberies:",robberyDC)
    print(" Thefts:",theftDC)
    print(" Offenses Involving Children:",offense_involving_childrenDC)
    print(" Assaults:",assaultDC)
    print(" Batteries:", batteryDC)
    print(" Burglaries:", burglaryDC)
    print(" Sexual Assaults:", sexual_assaultDC)
    print(" Narcotics:", narcoticsDC)
    print(" Criminal Damages:", criminal_damageDC)
    print(" Weapons Violations:", weapons_violationDC)
    print(" Deceptive Practices:", deceptive_practiceDC)
    print(" Homicides:", homicideDC)
    print(" Arsons:", arsonDC)
    print(" Criminal Trespassing:", criminal_trespassDC)
    print(" Kidnappings:", kidnappingDC)
    print(" Intimidation:", intimidationDC)

    


    


    print("\nThe percentage of each crime this district holds:")
    print(" Liquor Law Violations:{0:0.4}".format((liquorDC / (liquorDC + liquorTC)) * 100), "%")
    print(" Robberies:{0:0.4}".format((robberyDC / (robberyDC + robberyTC)) * 100), "%")
    print(" Thefts:{0:0.4}".format((theftDC / (theftDC + theftTC)) * 100), "%") 
    print(" Offenses Involving Children:{0:0.4}".format((offense_involving_childrenDC / (offense_involving_childrenDC + offense_involving_childrenTC)) * 100), "%")
    print(" Assaults:{0:0.4}".format((assaultDC / (assaultDC + assaultTC)) * 100), "%")
    print(" Batteries:{0:0.4}".format((batteryDC / (batteryDC + batteryTC)) * 100), "%")
    print(" Burglaries:{0:0.4}".format((burglaryDC / (burglaryDC + burglaryTC)) * 100), "%")
    print(" Sexual Assaults:{0:0.4}".format((sexual_assaultDC / (sexual_assaultDC + sexual_assaultTC)) * 100), "%")
    print(" Narcotics:{0:0.4}".format((narcoticsDC / (narcoticsDC + narcoticsTC)) * 100), "%")
    print(" Criminal Damages:{0:0.4}".format((criminal_damageDC / (criminal_damageDC + criminal_damageTC)) * 100), "%")
    print(" Weapons Violations:{0:0.4}".format((weapons_violationDC / (weapons_violationDC + weapons_violationTC)) * 100), "%")
    print(" Deceptive Practices:{0:0.4}".format((deceptive_practiceDC / (deceptive_practiceDC + deceptive_practiceTC)) * 100), "%")
    print(" Homicides:{0:0.4}".format((homicideDC / (homicideDC + homicideTC)) * 100), "%")
    print(" Arsons:{0:0.4}".format((arsonDC / (arsonDC + arsonTC)) * 100), "%")
    print(" Criminal Trespassing:{0:0.4}".format((criminal_trespassDC / (criminal_trespassDC + criminal_trespassTC)) * 100), "%")
    print(" Kidnappings:{0:0.4}".format((kidnappingDC / (kidnappingDC + kidnappingTC)) * 100), "%")
    print(" Intimidation:{0:0.4}".format((intimidationDC / (intimidationDC + intimidationTC)) * 100), "%")

    print("Total number of crimes for the district, resulting in arrest: ",district_total)
    print("This district holds {0:0.4}".format((district_total / overall_arrest_total) * 100) ,"% of the arrests for Chicago\n")
    
    print("\nArrests for each crime:\n Liquor Law Violations:",liquorD)
    print(" Robberies:",robberyD)
    print(" Thefts:",theftD)
    print(" Offenses Involving Children:",offense_involving_childrenD)
    print(" Assaults:",assaultD)
    print(" Batteries:", batteryD)
    print(" Burglaries:", burglaryD)
    print(" Sexual Assaults:", sexual_assaultD)
    print(" Narcotics:", narcoticsD)
    print(" Criminal Damages:", criminal_damageD)
    print(" Weapons Violations:", weapons_violationD)
    print(" Deceptive Practices:", deceptive_practiceD)
    print(" Homicides:", homicideD)
    print(" Arsons:", arsonD)
    print(" Criminal Trespassing:", criminal_trespassD)
    print(" Kidnappings:", kidnappingD)
    print(" Intimidation:", intimidationD)

    print("\nThe percentage of each crime, resuting in arrest, this district holds:")
    print(" Liquor Law Violations:{0:0.4}".format((liquorD / (liquorD + liquorT)) * 100), "%")
    print(" Robberies:{0:0.4}".format((robberyD / (robberyD + robberyT)) * 100), "%")
    print(" Thefts:{0:0.4}".format((theftD / (theftD + theftT)) * 100), "%") 
    print(" Offenses Involving Children:{0:0.4}".format((offense_involving_childrenD / (offense_involving_childrenD + offense_involving_childrenT)) * 100), "%")
    print(" Assaults:{0:0.4}".format((assaultD / (assaultD + assaultT)) * 100), "%")
    print(" Batteries:{0:0.4}".format((batteryD / (batteryD + batteryT)) * 100), "%")
    print(" Burglaries:{0:0.4}".format((burglaryD / (burglaryD + burglaryT)) * 100), "%")
    print(" Sexual Assaults:{0:0.4}".format((sexual_assaultD / (sexual_assaultD + sexual_assaultT)) * 100), "%")
    print(" Narcotics:{0:0.4}".format((narcoticsD / (narcoticsD + narcoticsT)) * 100), "%")
    print(" Criminal Damages:{0:0.4}".format((criminal_damageD / (criminal_damageD + criminal_damageT)) * 100), "%")
    print(" Weapons Violations:{0:0.4}".format((weapons_violationD / (weapons_violationD + weapons_violationT)) * 100), "%")
    print(" Deceptive Practices:{0:0.4}".format((deceptive_practiceD / (deceptive_practiceD + deceptive_practiceT)) * 100), "%")
    print(" Homicides:{0:0.4}".format((homicideD / (homicideD + homicideT)) * 100), "%")
    print(" Arsons:{0:0.4}".format((arsonD / (arsonD + arsonT)) * 100), "%")
    print(" Criminal Trespassing:{0:0.4}".format((criminal_trespassD / (criminal_trespassD + criminal_trespassT)) * 100), "%")
    print(" Kidnappings:{0:0.4}".format((kidnappingD / (kidnappingD + kidnappingT)) * 100), "%")
    print(" Intimidation:{0:0.4}".format((intimidationD / (intimidationD + intimidationT)) * 100), "%")

    print("\nThe probability of each crime in this district resulting in an arrest\n(0 = very unlikely, 1 = very likely):")
    print(" Liquor Law Violations:{0:0.4}".format(liquorD / liquorDC) if liquorDC else 0)
    print(" Robberies:{0:0.4}".format(robberyD / robberyDC) if robberyDC else 0)
    print(" Thefts:{0:0.4}".format(theftD / theftDC) if theftDC else 0) 
    print(" Offenses Involving Children:{0:0.4}".format(offense_involving_childrenD / offense_involving_childrenDC) if offense_involving_childrenDC else 0)
    print(" Assaults:{0:0.4}".format(assaultD / assaultDC) if assaultDC else 0)
    print(" Batteries:{0:0.4}".format(batteryD / batteryDC) if batteryDC else 0)
    print(" Burglaries:{0:0.4}".format(burglaryD / burglaryDC) if burglaryDC else 0)
    print(" Sexual Assaults:{0:0.4}".format(sexual_assaultD / sexual_assaultDC) if sexual_assaultDC else 0)
    print(" Narcotics:{0:0.4}".format(narcoticsD / narcoticsDC) if narcoticsDC else 0)
    print(" Criminal Damages:{0:0.4}".format(criminal_damageD / criminal_damageDC) if criminal_damageDC else 0)
    print(" Weapons Violations:{0:0.4}".format(weapons_violationD / weapons_violationDC) if weapons_violationDC else 0)
    print(" Deceptive Practices:{0:0.4}".format(deceptive_practiceD / deceptive_practiceDC) if deceptive_practiceDC else 0)
    print(" Homicides:{0:0.4}".format(homicideD / homicideDC) if homicideDC else 0)
    print(" Arsons:{0:0.4}".format(arsonD / arsonDC) if arsonDC else 0)
    print(" Criminal Trespassing:{0:0.4}".format(criminal_trespassD / criminal_trespassDC) if criminal_trespassDC else 0)
    print(" Kidnappings:{0:0.4}".format(kidnappingD / kidnappingDC) if kidnappingDC else 0)
    print(" Intimidation:{0:0.4}".format(intimidationD / intimidationDC) if intimidationDC else 0)
    print(" \n")



def option3():
    file = open("Crimes.csv")
    filename = csv.reader(file)
    
    #initialize counts
    crime_count=0
    arrest_count=0
    domestic_count=0
    population = 2716000
    #count the number of rows for the number of number of reported crimes


    #######3doption = input("Would you like to see crimes per district (y/n):")
    #append data
    data = []
    data1 = []
    data2 = []

    robbery1 = 0
    theft1 = 0
    offense_involving_children1 = 0
    assault1 = 0
    battery1 = 0
    burglary1 = 0
    sexual_assault1 = 0
    narcotics1 = 0
    criminal_damage1 = 0
    deceptive_practice1 = 0
    homicide1 = 0
    weapons_violation1 = 0
    other1 = 0
    liquor1 = 0
    arson1 = 0
    criminal_trespass1 = 0
    kidnapping1 = 0
    intimidation1 = 0

    for row in filename:
        data.append(row[8])#8 or 4
        data1.append(row[9])#9 or 5
        data2.append(row[5])#5 or 1
        crime_count+=1
        #arrest
        if row[8] == "true":
            arrest_count += 1
        #domestic    
        if row[9] == "true":
            domestic_count += 1
        #arrest + crime
        if row[5] == "LIQUOR LAW VIOLATION" and row[8] == "true":
            liquor1 +=1
        if row[5]== "ROBBERY" and row[8] == "true":
            robbery1 += 1
        if (row[5] == "THEFT" or row[5] == "MOTOR VEHICLE THEFT") and row[8] == "true":
            theft1 += 1
        if row[5] == "OFFENSE INVOLVING CHILDREN" and row[8] == "true":
            offense_involving_children1 += 1
        elif row[5] == "ASSAULT" and row[8] == "true":
            assault1 += 1
        if row[5] == "BATTERY" and row[8] == "true":
            battery1 += 1
        if row[5] == "BURGLARY" and row[8] == "true":
            burglary1 +=1
        if (row[5] == "CRIM SEXUAL ASSAULT" or row[5] == "SEX OFFENSE") and row[8] == "true":
            sexual_assault1 += 1
        if row[5] == "NARCOTICS" and row[8] == "true":
            narcotics1 += 1
        if row[5] == "CRIMINAL DAMAGE" and row[8] == "true":
            criminal_damage1 += 1
        if row[5] == "WEAPONS VIOLATION" and row[8] == "true":
            weapons_violation1 += 1
        if row[5] == "DECEPTIVE PRACTICE" and row[8] == "true":
            deceptive_practice1 += 1
        if row[5] == "HOMICIDE" and row[8] == "true":
            homicide1 += 1
        if row[5] == "ARSON" and row[8] == "true":
            arson1 += 1
        if row[5] == "CRIMINAL TRESPASS" and row[8] == "true":
            criminal_trespass1 += 1
        if row[5] == "KIDNAPPING" and row[8] == "true":
            kidnapping1 += 1
        if row[5] == "INTIMIDATION" and row[8] == "true":
            intimidation1 += 1    

    other1 = arrest_count - liquor1 - robbery1 - theft1 - offense_involving_children1 - assault1 - battery1 - criminal_damage1 - sexual_assault1 - narcotics1 - weapons_violation1 - deceptive_practice1 - homicide1 - arson1 - criminal_trespass1 - kidnapping1 - intimidation1

    #calculate number of not arrested
    #calculate arrest percentage       
    not_arrested = crime_count - arrest_count
    arrest_percentage = 100* (arrest_count / crime_count)



    #print 1st batch of information           
    print("\nThe number of reported crimes:" , crime_count)
    print("The number of arrests:" , arrest_count)
    print("The number of cases without arrests:", not_arrested)
    print("The number of cases involving domestic violence:" , domestic_count)
    print("About {0:0.4}".format(arrest_percentage),"% of total reported crimes resulted in an arrest") #round to 4 decimal points

    crimes = []
    robbery = 0
    theft = 0
    offense_involving_children = 0
    assault = 0
    battery = 0
    burglary = 0
    sexual_assault = 0
    narcotics = 0
    criminal_damage = 0
    deceptive_practice = 0
    homicide = 0
    weapons_violation = 0
    other = 0
    liquor = 0
    arson = 0
    criminal_trespass = 0
    kidnapping = 0
    intimidation = 0


    for crime in data2:
        if crime == "LIQUOR LAW VIOLATION":
           liquor +=1
        elif crime == "ROBBERY":
           robbery += 1
        elif crime == "THEFT" or crime == "MOTOR VEHICLE THEFT":
           theft += 1
        elif crime == "OFFENSE INVOLVING CHILDREN":
           offense_involving_children += 1
        elif crime == "ASSAULT":
           assault += 1
        elif crime == "BATTERY":
           battery += 1
        elif crime == "BURGLARY":
           burglary +=1
        elif crime == "CRIM SEXUAL ASSAULT" or crime == "SEX OFFENSE":
           sexual_assault += 1
        elif crime == "NARCOTICS":
           narcotics += 1
        elif crime == "CRIMINAL DAMAGE":
           criminal_damage += 1
        elif crime == "WEAPONS VIOLATION":
           weapons_violation += 1
        elif crime == "DECEPTIVE PRACTICE":
           deceptive_practice += 1
        elif crime == "HOMICIDE":
           homicide += 1
        elif crime == "ARSON":
            arson += 1
        elif crime == "CRIMINAL TRESPASS":
            criminal_trespass += 1
        elif crime == "KIDNAPPING":
            kidnapping += 1
        elif crime == "INTIMIDATION":
            intimidation += 1    
        else:
           other += 1


    d={}

    d[' Liquor Law Violation'] = liquor
    d[' Weapons Violation'] = weapons_violation
    d[' Arson'] = arson
    d[' Kidnapping'] = kidnapping
    d[' Intimidation'] = intimidation
    d[' Robbery'] = robbery
    d[' Theft'] = theft
    d[' Offense Involving Children'] = offense_involving_children
    d[' Assault'] = assault
    d[' Battery'] = battery
    d[' Burglary'] = burglary
    d[' Sexual Assault or Sex Offense'] = sexual_assault
    d[' Narcotics'] = narcotics
    d[' Criminal Damage'] = criminal_damage
    d[' Deveptive Practice'] = deceptive_practice
    d[' Criminal Trespassing'] = criminal_trespass
    d[' Homicide'] = homicide
    d[' Other'] = other

    
    #print list of most frequent to least frequent
    newdict = list(sorted(d.items(), key = lambda kv: -kv[1]))
    print("\n\nList of Crimes (most to least frequent):")
    [print("{} : {}".format(x[0],x[1])) for x in newdict]


    #number of each crime has resulted in arrest
    c = {}
    c[' Liquor Law Violation'] = liquor1
    c[' Weapons Violation'] = weapons_violation1
    c[' Arson'] = arson1
    c[' Kidnapping'] = kidnapping1
    c[' Intimidation'] = intimidation1
    c[' Robbery'] = robbery1
    c[' Theft'] = theft1
    c[' Offense Involving Children'] = offense_involving_children1
    c[' Assault'] = assault1
    c[' Battery'] = battery1
    c[' Burglary'] = burglary1
    c[' Sexual Assault or Sex Offense'] = sexual_assault1
    c[' Narcotics'] = narcotics1
    c[' Criminal Damage'] = criminal_damage1
    c[' Deveptive Practice'] = deceptive_practice1
    c[' Criminal Trespassing'] = criminal_trespass1 
    c[' Homicide'] = homicide1
    c[' Other'] = other1

    
    #Cimes that lead to an arrest list from most to least frequent
    newdict1 = list(sorted(c.items(), key = lambda kv: -kv[1]))
    print("\n\nList of Crimes leading to an Arrest (most to least frequent):")
    [print("{} : {}".format(x[0],x[1])) for x in newdict1]
    

    #Percetages of crimes
    print("\n\nPercent of crime:\n Robberies:{0:0.4}".format((robbery/crime_count) *100), "%")
    print(" Thefts:{0:0.4}".format((theft/crime_count) *100), "%")
    print(" Liquor Law Violations:{0:0.4}".format((liquor/crime_count) *100), "%")
    print(" Criminal Tresspass:{0:0.4}".format((criminal_trespass/crime_count) *100), "%")
    print(" Arson:{0:0.4}".format((arson/crime_count) *100), "%")
    print(" Offenses Involving Children:{0:0.4}".format((offense_involving_children/ crime_count) *100), "%")
    print(" Assault:{0:0.4}".format((assault/crime_count) *100), "%")
    print(" Battery:{0:0.4}".format((battery/crime_count) *100), "%")
    print(" Burglary:{0:0.4}".format((burglary/crime_count) *100), "%")
    print(" Sexual Assault:{0:0.4}".format((sexual_assault/crime_count) *100), "%")
    print(" Narcotics:{0:0.4}".format((narcotics/crime_count) *100), "%")
    print(" Criminal Damage:{0:0.4}".format((criminal_damage/crime_count) *100), "%")
    print(" Deceptive Practice:{0:0.4}".format((deceptive_practice/crime_count) *100), "%")
    print(" Kidnapping:{0:0.4}".format((kidnapping/crime_count) *100), "%")
    print(" Intimidation:{0:0.4}".format((intimidation/crime_count) *100), "%")
    print(" Homicide:{0:0.4}".format((homicide/crime_count) *100), "%")
    print(" Other:{0:0.4}".format((other/crime_count) *100), "%")


    #print probability of crime being reported 
    print("\n\nProbability of crime being reported \n(0 = very unlikely, 1 = very likely)\n Robberies:{0:0.4}".format(robbery/crime_count))
    print(" Thefts:{0:0.4}".format(theft / crime_count) )
    print(" Liquor Law Violations:{0:0.4}".format(liquor/crime_count))
    print(" Criminal Tresspass:{0:0.4}".format(criminal_trespass/crime_count))
    print(" Arson:{0:0.4}".format(arson/crime_count))
    print(" Offenses Involving Children:{0:0.4}".format(offense_involving_children/crime_count))
    print(" Assault:{0:0.4}".format(assault/crime_count))
    print(" Battery:{0:0.4}".format(battery/crime_count))
    print(" Burglary:{0:0.4}".format(burglary/crime_count))
    print(" Sexual Assault:{0:0.4}".format(sexual_assault/crime_count))
    print(" Narcotics:{0:0.4}".format(narcotics/crime_count))
    print(" Criminal Damage:{0:0.4}".format(criminal_damage/crime_count))
    print(" Deceptive Practice:{0:0.4}".format(deceptive_practice/crime_count))
    print(" Kidnapping:{0:0.4}".format(kidnapping/crime_count))
    print(" Intimidation:{0:0.4}".format(intimidation/crime_count))
    print(" Homicide:{0:0.4}".format(homicide/crime_count))
    print(" Other:{0:0.4}".format(other/crime_count))


    #probability of being arrested for a crime
    print("\n\nProbability of each crime resulting in an arrest \n(0 = very unlikely, 1 = very likely)\n Robberies: {0:0.4}".format(robbery/crime_count))
    print(" Thefts: {0:0.4}".format(theft1 / theft))
    print(" Liquor Law Violations:{0:0.4}".format(liquor1 / liquor))
    print(" Criminal Tresspass:{0:0.4}".format(criminal_trespass1 /criminal_trespass))
    print(" Arson:{0:0.4}".format(arson1/arson))
    print(" Offenses Involving Children:{0:0.4}".format(offense_involving_children1 / offense_involving_children))
    print(" Assault:{0:0.4}".format(assault1 / assault ))
    print(" Battery:{0:0.4}".format(battery1 / battery))
    print(" Burglary:{0:0.4}".format(burglary1 / burglary))
    print(" Sexual Assault:{0:0.4}".format(sexual_assault1 /sexual_assault))
    print(" Narcotics:{0:0.4}".format(narcotics1 /narcotics))
    print(" Criminal Damage:{0:0.4}".format(criminal_damage1/criminal_damage))
    print(" Deceptive Practice:{0:0.4}".format(deceptive_practice1 /deceptive_practice))
    print(" Kidnapping:{0:0.4}".format(kidnapping1 /kidnapping))
    print(" Intimidation:{0:0.4}".format(intimidation1 /intimidation))
    print(" Homicide:{0:0.4}".format(homicide1/homicide))
    print(" Other:{0:0.4}".format(other1/ other))
    print(" \n")
    
main()
