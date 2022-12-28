class Rectangle:
    # Constructor de la classe Rectangle
    def __init__(self, longueur=1, largeur=1, nom="rectangle"):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = nom
        
    # Methode toString()
    def __str__(self):
        return f"{self.nom} (longueur = {self.longueur}, largeur = {self.largeur})"
    
    # Methode surface
    def surface(self):
        return self.longueur * self.largeur