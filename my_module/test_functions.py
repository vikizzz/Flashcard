from classes import *
from functions import *

"""Tests for classes"""
def test_user():
    user = User()
    assert callable(user.add_user)
    user.add_user('name','password')
    assert len(user.users['name']) == 1
    assert len(user.users['password']) == 1
    assert len(user.users['cards']) == 1
    assert callable(user.show_user)

def test_card():
    card = Card()
    assert callable(card.add_card)
    card.add_card('term', 'definition')
    assert len(card.cards) == 1
    assert callable(card.remove_card)
    card.remove_card('term')
    assert len(card.cards) == 0
    assert callable(card.show_card)

"""Tests for functions"""
def test_login():
    assert callable(login)

def test_signup():
    user = User()
    assert callable(signup)
    signup (user, 'name', 'password')
    assert len(user.users['name']) == 1
    assert len(user.users['password']) == 1
    assert len(user.users['cards']) == 1

def test_start():
    assert callable(start)

def test_quiz_fb():
    assert callable(quiz_fb)

def test_quiz():
    assert callable(quiz)

def test_start_card():
    assert callable(start_card)