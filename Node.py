
class Node :
    """
    Node class that represent nodes in a rooted tree
    A node is composed of:
    ● The board itself at the current node
    ● A list of nodes, its children
    """
    def __init__(self, board, children=[]):
        self.board = board
        self.children = children
        
#PRIMITIVES

    def content(self):
        """
        Renvoie l'attribut labels du noeud
        Parametres : 
            param1(Node) : Le noeud lui-meme
        Returns : 
             string:les etiquettes (peut etre autre chose qu'un string)
        """
        return self.board
    
    def children(self):
        """
        Renvoie les enfants du noeud
        Parametres : 
            param1(Node) : Le noeud lui meme
        Returns : 
            list : Les enfants (noeuds) du noeud
        """
        return self.children
        
    def is_leaf(self):
        """
        Indique si le noeud est une feuille ou pas
        Parametres : 
            param1(Node) : Le noeud lui meme
        Returns : 
            bool : True si le noeud n'a pas d'enfants, sinon False
        """
        return True if not self.children else False
    
    def degree(self):
        """
        Renvoie le degre du noeud (son nombre de fils)
        Parametres : 
            param1(Node) : Le noeud lui meme
        Returns : 
            int : son nombre de fils
        """
        return len(self.children)
    