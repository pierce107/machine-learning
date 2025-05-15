import random

# the possiblity for income and age
p_income= {'Hoch ': 0.4 , 'Niedrig ': 0.6}
p_age = {'Jung ': 0.6 ,'Alt': 0.4}

# possiblity table for a possible purchase
p_marketpreferenz = {
('Hoch ', 'Jung '): {'Android ': 0.42 , 'Apple ': 0.56} ,
('Hoch ', 'Alt '): {'Android ': 0.5 , 'Apple ': 0.5} ,
('Niedrig ', 'Jung '): {'Android ': 0.8 , 'Apple ': 0.2} ,
('Niedrig ', 'Alt '): {'Android ': 0.9 , 'Apple ': 0.1}
}

# empty lists for initialize
age = []
income = []
brand = []

for i in range(10):
  # possiblity for a person to be young
  # adds to the list 'age' a random number (possiblity)
  age.append(round(random.random(), 3))
  # prints out the random number
  print(age[i])
  # if the printed random number is lower than the above written possiblity for age, then it is young
  if age[i] <= p_age['Jung ']:
    print('Jung')
  else:
    print('Alt')

# possiblity for a person to be rich
  income.append(round(random.random(), 3))
  print(income[i])
  if income[i] <= p_income['Hoch ']:
    print('Hoch')
  else:
    print('Niedrig')

# possiblity for a person to buy an Android phone according to the possiblity table for a purchase
  brand.append(round(random.random(), 3))
  print(brand[i])
  # the possiblity to buy an Android for a rich and young person 
  if brand[i] <= p_marketpreferenz[('Hoch ', 'Jung ')]['Android ']:
    print('Android')
  else:
    print('Apple')


  print('\n')

#Die Fragen der Präsentationen in Powerpoint vorstellen 