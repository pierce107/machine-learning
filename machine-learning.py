import random

# the possiblity for income and age
p_income= {'Hoch ': 0.4 , 'Niedrig ': 0.6}
p_age = {'Jung ': 0.6 ,'Alt': 0.4}

# possiblity table for a possible purchase
p_marketpreferenz = {
('Hoch ', 'Jung '): {'Android ': 0.42 , 'Apple ': 0.58} ,
('Hoch ', 'Alt '): {'Android ': 0.5 , 'Apple ': 0.5} ,
('Niedrig ', 'Jung '): {'Android ': 0.8 , 'Apple ': 0.2} ,
('Niedrig ', 'Alt '): {'Android ': 0.9 , 'Apple ': 0.1}
}

# empty lists for initialize
age = []
income = []
brand = []
sampleset = []

for i in range(5000):
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
    sampleset.append(('Hoch', 'Jung', 'Android'))
  else:
    sampleset.append(('Hoch', 'Jung', 'Apple'))

# possiblity for a person to buy an Android phone according to the possiblity table for a purchase
  brand.append(round(random.random(), 3))
  print(brand[i])
  # the possiblity to buy an Android for a rich and old person 
  if brand[i] <= p_marketpreferenz[('Hoch ', 'Alt ')]['Android ']:
    sampleset.append(('Hoch', 'Alt','Android'))
  else:
    sampleset.append(('Hoch', 'Alt', 'Apple'))

# possiblity for a person to buy an Android phone according to the possiblity table for a purchase
  brand.append(round(random.random(), 3))
  print(brand[i])
  # the possiblity to buy an Android for a poor and young person 
  if brand[i] <= p_marketpreferenz[('Niedrig ', 'Jung ')]['Android ']:
    sampleset.append(('Niedrig', 'Jung', 'Android'))
  else:
    sampleset.append(('Niedrig', 'Jung', 'Apple'))

# possiblity for a person to buy an Android phone according to the possiblity table for a purchase
  brand.append(round(random.random(), 3))
  print(brand[i])
  # the possiblity to buy an Android for a poor and old person 
  if brand[i] <= p_marketpreferenz[('Niedrig ', 'Alt ')]['Android ']:
    sampleset.append(('Niedrig', 'Alt', 'Android'))
  else:
    sampleset.append(('Niedrig', 'Alt', 'Apple'))


  print('\n')
print(sampleset)
count_of_young = sampleset.count('Jung')
count_of_old = sampleset.count('Alt')
count_of_android = sampleset.count('Android')
count_of_apple = sampleset.count('Apple')
print(count_of_apple)
count_of_rich = sampleset.count('Hoch')
count_of_poor = sampleset.count('Niedrig')
#Die Fragen der Präsentationen in Powerpoint vorstellen
# P(Ap)
print(count_of_apple/len(sampleset))
# P(j | An)
# P(j, h | Ap)