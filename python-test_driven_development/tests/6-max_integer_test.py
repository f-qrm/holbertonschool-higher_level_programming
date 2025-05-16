#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self): #teste une liste triee, verifie que le res. est = a 4
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_unordered_list(self): #Vérifie que la fonction ne dépend pas de l’ordre et que res. = 4 tjrs
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_max_at_beginning(self):# teste que le nr max est au debut, verifie que la function ne saute pas le premier element
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_single_element(self): #Vérifie que ça marche même avec une mini liste, Cas avec un seul élément dans la liste
        self.assertEqual(max_integer([7]), 7)
    def test_empty_list(self): #verifie si le resultat est none vu comme cest une liste vide
        self.assertIsNone(max_integer([]))
    def test_negative_numbers(self): #verifie que la function gerre bien es nombres negatifs, le plus grand est -1,
        self.assertEqual(max_integer([-1, -5, -3]), -1)
    def test_mixed_numbers(self): #verifie que la function compare bien tous les cas positif et negatif, le max est 10.
        self.assertEqual(max_integer([-10, 0, 10]), 10)
    def test_duplicate_max(self): #plusieurs 3, verifie si il retourne le bon max.
        self.assertEqual(max_integer([2, 3, 3, 1]), 3)
    def test_floats(self): #liste avec des floats, verifie le plus grand. verifie si la function marche avec des floats aussi.
        self.assertEqual(max_integer([1.1, 2.2, 0.3]), 2.2)
    def test_all_same(self): #test avec des elements identique, verifie si le max function, verifie si ca ne cause pas d1erreur
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
    def test_string_list(self): #test avec liste de chaine de characteres. 
        self.assertEqual(max_integer(["a", "z", "m"]), "z")
    def test_string_argument(self): #test avec ascii si t est le plus granad charactere.
        self.assertEqual(max_integer("Holberton"), "t")
