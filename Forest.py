# -*- coding: utf-8 -*-
"""
Forest module to build and manage list
of rooted tree
"""
class Forest(list):
        
    
    def reste(self):
        """
        Renvoie la foret sans son premier arbre
        Parametres : 
            param1(Forest) : La foret elle-meme
        Returns : 
            list : La foret a partir de son 2e element, ou une liste vide s'il n'y en pas 
        """
        if len(self)>1:
            return self[1:]
        else:
            return []
        
    def premierArbre(self):
        """
        Renvoie le premier arbre de la foret
        Parametres : 
            param1(Forest) : La foret elle-meme
        Returns : 
            RTree : Le premier arbre 
        """
        return self[0]
    
    def sousArbres(self):
        """
        Renvoie les sous-arborescences
        Parametres : 
            param1(Forest) : La foret elle-meme
        Returns : 
            list : Les sous-arborescences du premier arbre de la foret, ou une liste vide s'il n'y en pas 
        """
        return self.premierArbre().sub_tree()
    
    def display_depth(self):
        """
        Affiche les etiquettes de chaque noeud a travers un parcours en profondeur
        Parametres : 
            param1(Forest) : La foret elle-meme
        Returns : 
             None : condition d'arret pour sortir de la recursivite
        """
        if not self:
            return None
        else:
            reste = self.reste()
            sousArbres = self.sousArbres()
            print(self[0].labels)
            
            f = Forest(sousArbres+reste)
            f.display_depth()
    
    def display_width(self):
        """
        Affiche les etiquettes de chaque noeud a travers un parcours en largeur
        Parametres : 
            param1(Forest) : La foret elle-meme
        Returns : 
             None : condition d'arret pour sortir de la recursivite
        """
        if not self:
            return None
        else:
            reste = self.reste()
            sousArbres = self.sousArbres()
            print(self[0].labels)
            
            f = Forest(reste+sousArbres)
            f.display_width()
            
    def descending(self):
        """
        Renvoie le degre de l'arborescence (le degre le plus grand de ses noeuds)
        Parametres : 
            param1(RTree) : L'arborescence elle-meme
        Returns : 
            int : le degre le plus grand
        """
        if not self:
            return []
        else:
            reste = self.reste()
            sousArbres = self.sousArbres()
            
            f = Forest(sousArbres+reste)
            return [self[0]] + f.descending()
            
    
                

                