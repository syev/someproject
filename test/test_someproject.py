"""Unit tests"""
import unittest
import someproject.someproject

class TestSomeProject(unittest.TestCase):
    def test_get_project_name(self):
        self.assertEqual(someproject.someproject.get_project_name(), "Someproject # 0")

#    def test_get_other_project_name(self):
#        self.assertEqual(someproject.someproject.get_other_project_name(), "Someproject # 1")
