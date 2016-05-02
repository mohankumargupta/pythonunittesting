import unittest
import blackjack

class BlackjackTest(unittest.TestCase):
  def test_two_picture_cards(self):
    self.assertEquals(blackjack.blackjack(['K','Q']), 20)


    

