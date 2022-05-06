# #OOP - Create your own object. Make at least two additional methods for it.

# #need to create a class with methods inside?
# Smell identification program:

# it smells 

# tells me what that smell is

# #on the object init 
#     4 categories : sweetnes, bittermes sourness umami
#sweetnes = 1-10
# # b = 1-10
# so = 1-10
# um = 1-10
#this is very sweet if sweetness = 10
# tellwhat is it take int variabes to determine what rto be said 
# it smells input asking the user to smell the object



class SmellIdentity:
    def __init__(self, sweetness, bitterness, sourness, umami, food):
        self.sweetness = sweetness
        self.bitterness = bitterness
        self.sourness = sourness
        self.umami = umami
        self.food = food


    def it_smells(self):
        print('hey put that {self.food} near my face so i can smell it ')
    
    def what_smell_is(self):
        if self.sweetness > 7:
            return 'this is very sweet'
        if self.bitterness > 7:
            return 'this is very bitter'
        if self.sourness > 7:
            return 'this is very sour'
        if self.umami > 7:
            return 'this is very umami'
my_smellIdenitity = SmellIdentity('food', 10,1,0,0)
my_smellIdenitity.it_smells()
print(my_smellIdenitity.what_smell_is())