"""
Gabriel Meran
CS 100 2016F Section
HW 01 Sept 12, 2016
"""
2.18
a)>>> flowers = ['rose' , 'bougainvillea' , 'yucca' , 'marigold', 'daylilly',
               'lilly of the valley']
b)>>> flowers = ['rose' , 'bougainvillea' , 'yucca' , 'marigold', 'daylilly', 'lilly of the valley']
>>> 'potato' in flowers
False
>>> flowers2 = ['rose' , 'bougainvillea' , 'yucca' , 'marigold', 'daylilly', 'lilly of the valley', 'potato']
>>> 'potato' in flowers2
True
c)>>> thorny = []
>>> thorny.append(flowers[0])
>>> thorny[0]
'rose'
>>> thorny.append(flowers[1])
>>> thorny[1]
'bougainvillea'
>>> thorny.append(flowers[2])
>>> thorny[2]
'yucca'
d)>>> poisonous = []
>>> poisonous.append(flowers[5])
>>> poisonous[0]
'lilly of the valley'
e)>>> dangerous = [ thorny + poisonous]
>>> dangerous
[['rose', 'bougainvillea', 'yucca', 'lilly of the valley']]
2.19
>>> answers = ['Y' , 'N' , 'N', 'Y' , 'N' , 'Y' , 'Y', 'Y' , 'N', 'N' , 'N']
a)>>> numYes = answers.count('Y')
>>> numYes
5
b)>>> numNo = answers.count('N')
>>> numNo
6
>>> num_of_answers = numYes + numNo
>>> num_of_answers
11
c)>>> percentYes = numYes / num_of_answers
>>> percentYes
0.45454545454545453
>>> percentYes *100
45.45454545454545
d)>>> answers.sort()
>>> answers
['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']
e)>>> answers[6] = 'f'
>>> answers
['N', 'N', 'N', 'N', 'N', 'N', 'f', 'Y', 'Y', 'Y', 'Y']
2.21
>>> s = 'Derek'
>>> t = 'Jeter'
>>> intials = s[0] + t[0]
>>> intials
'DJ'

3)
HW Example :
>>> grades = ['A' , 'F' , 'C' , 'F' , 'A' , 'B' , 'A']
>>> grades
['A', 'F', 'C', 'F', 'A', 'B', 'A']
>>> num_of_A = grades.count('A')
>>> num_of_A
3
>>> num_of_B = grades.count('B')
>>> num_of_B
1
>>> num_of_C
1
>>> num_of_D = grades.count('D')
>>> num_of_D
0
>>> num_of_F = grades.count('F')
>>> num_of_F
2
>>> frequency = [ num_of_A , num_of_B , num_of_C , num_of_D , num_of_F]
>>> frequency
[3, 1, 1, 0, 2]

My Example:
>>> grades = [ 'A' , 'A' , 'B' , 'C' , 'C' , 'D' , 'F', 'D']
>>> num_of_A = grades.count['A']
>>> num_of_A = grades.count('A')
>>> num_of_B = grades.count('B')
>>> num_of_C = grades.count('C')
>>> num_of_D = grades.count('D')
>>> num_of_F = grades.count('F')
>>> num_of_A
2
>>> num_of_B
1
>>> num_of_C
2
>>> num_of_D
2
>>> num_of_F
1
>>> frequency = [num_of_A , num_of_B , num_of_C , num_of_D , num_of_F]
>>> frequency
[2, 1, 2, 2, 1]


