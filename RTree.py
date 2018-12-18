# -*- coding: utf-8 -*-
"""
RTree module to build and manage rooted tree
"""

from Node import Node
from Forest import Forest
class Rtree(Node) :
    
    """
    A rooted tree is represented by its root node
    """
    
    def __init__(self, labels, sub_Rtree = []):
        super().__init__(labels, sub_Rtree)
        
        
#PRIMITIVES

    def root(self):
        """
        Renvoie la racine de l'arborescence (=elle-meme)
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            RTree: L'arborescence
        """
        return self
    
    def sub_tree(self):
        """
        Renvoie les sous-arborescences
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            list : Les sous-arborescences de l'arborescence
        """
        return self.children
        
#METHODES
        


    
    def display_depth(self):
        """
        Affiche les etiquettes de chaque noeud a travers un parcours en profondeur
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
             Aucun (fonction d'affichage)
        """
        if not self.sub_tree():
            print(self.labels)
        else:
            #transforms the rooted tree in forest
            f = Forest([self])
            #calls the corresponding method on the forest
            f.display_depth()

    def display_width(self):
        """
        Affiche les etiquettes de chaque noeud a travers un parcours en largeur
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
             Aucun (fonction d'affichage)
        """
        if not self.sub_tree():
            print(self.labels)
        else:
            #transforms the rooted tree in forest
            f = Forest([self])
            #calls the corresponding method on the forest
            f.display_width()


    def descending(self):
        """
        Renvoie la liste de tous les noeuds fils, petits-fils, etc.
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
             list:Liste de tous les noeuds de la descendance (vide si pas d'enfants)
        """
        if not self.sub_tree():
            return []
        else:
            #transforms the rooted tree in forest
            f = Forest([self])
            #calls the corresponding method on the forest
            return f.descending()
        
    def ascending(self, startingNode):
        """
        Renvoie la liste de tous les noeuds pères, grands-pères, etc.
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
            param2(RTree) : Le noeud dont on veut connaitre l'ascendance
        Returns : 
             list:Liste de tous les noeuds de l'ascendance (vide si pas d'ascendance = noeud racine)
        """
        if self.father(startingNode) is None :
            return []
        else:
            return self.ascending(self.father(startingNode)) + [self.father(startingNode)]
        

    def father(self, child):
        """
        Renvoie le noeud pere du noeud child passe en parametre
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
            param2(Node) : Le noeud enfant
        Returns : 
             Node: le noeud pere s'il est trouve
             None: si le noeud child n'a aucun pere (= noeud racine de l'arborescence self)
        """
        listeNodes = self.descending()
        for node in listeNodes:
            if(child in node.children):
                return node
        return None
    
    def degreeT(self):
        """
        Renvoie le maximum des degres des noeuds
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            int : nombre de fils maximum après avoir parcouru tous les noeuds
        """
        listeNodes = self.descending()
        degreeMax = 0
        for node in listeNodes:
            if(node.degree() > degreeMax):
                degreeMax = node.degree()
        return degreeMax
    
    def depth(self):
        """
        Renvoie le maximum des profondeurs des feuilles
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            int : profondeur maximum de l'arborescence (en comparant les profondeurs de chaque noeud)
        """
        listeNodes = self.descending()
        maxDepth = 0
        for node in listeNodes:
            nodeDepth = len(self.ascending(node))
            if(nodeDepth > maxDepth):
                maxDepth = nodeDepth
        return maxDepth
    
    def width(self):
        """
        Renvoie le nombre maximum de noeuds a un niveau donné
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            int : nombre maximum de noeuds a un niveau donné
        """
        listeNodes = self.descending()
        arrayAscendance = []
        for node in listeNodes:  
            nodeDepth=len(self.ascending(node))
            if(len(arrayAscendance) == nodeDepth):
                arrayAscendance.append(0)
            arrayAscendance[nodeDepth]+=1
        return max(arrayAscendance)
        
        
        
            
            


# Test
rt6 = Rtree('n6')
rt5 = Rtree('n5')
rt4 = Rtree('n4')
rt3 = Rtree('n3')
rt2 = Rtree('n2')
rt1 = Rtree('n1', [rt4, rt5, rt6])
rt0 = Rtree('n0', [rt1, rt2, rt3])

print(rt0.width())
