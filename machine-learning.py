import random

# fuer Einkommen und Alter
p_income = {'Hoch': 0.59, 'Niedrig': 0.41}
p_age = {'Alt': 0.46, 'Jung': 0.54}

# Bedingte Wahrscheinlichkeitstabelle fuer Kaufentscheidung
p_marketpreference = {
( ' Hoch ' , ' Jung ' ): { ' Apple ': 0.375 , ' Android ': 0.625} ,
( ' Hoch ' , ' Alt ' ): { ' Apple ': 0.28 , ' Android ': 0.72} ,
( ' Niedrig ' , ' Jung ' ): { ' Apple ': 0.11 , ' Android ': 0.89} ,
( ' Niedrig ' , ' Alt ' ): { ' Apple ': 0.16 , ' Android ': 0.84}
}

random_income = round(random.random(), 3)
random_age = round(random.random(), 3)

Nutzer = float(input('Wieviel verdienen Sie: '))

for count in range(1): 
    print(Nutzer)
    if Nutzer <= p_income['Hoch ']:
        print('Hoch')
    else:
        print('Niedrig')




# for count in range(3): 
#   print(random_einkommen)
#   if random_einkommen <= p_einkommen['Hoch ']:
#     print('Hoch')
#   else:
#     print('Niedrig')

# for count in range(3): 
#   print(random_alter)
#   if random_alter <= p_alter['Jung ']:
#     print('Jung')
#   else:
#     print('Alt')



#  print(round(random.random(),3))
  # if nummer <= p_einkommen['Hoch ']:
  #   print('Hoch')
#  else:
#    print('Niedrig')

#print(p_einkommen['Hoch '])