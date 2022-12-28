class Vecteur2D:
    # Constructor de la clsse Vecteur2D
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    # La methode toStrring() pour Python
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # La methode afficher()
    def afficher(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    # Methode de srucharge d'addition de deux vecteurs du plan
    def __add__(self, vecteur2D):
        return Vecteur2D(self.x + vecteur2D.x, self.y + vecteur2D.y)
    
# Un vecteur de 2D sans parametre
vect1 = Vecteur2D()

# Un vecteur de 2D avec ses deux parametre
vect2 = Vecteur2D(2,4)

# Affichage des vecteurs comme un tuple
print(vect1)
print(vect2)

# Affichage des vecteurs avec la methode afficher()
print(vect1.afficher())

# La somme de deux vecteurs du plan
vect3 = vect1 + vect2

# L'affichage de la somme de deux vecteurs du plan
print(vect3.afficher())