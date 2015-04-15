import unittest
from A import *
make_board()
class test_pacman(unittest.TestCase):
	def test_initial_state(self):
		pacman = Pacman()
		self.assertEqual(pacman.get_pos(),[11,20])

	def test_initial_coins(self):
		self.assertEqual(len(coins),19)

	def test_initial_score(self):
		pacman = Pacman()
		self.assertEqual(pacman.get_score(),0)

	def test_movetowall_restricted(self):
		curr_pos = pac.get_pos()
		pac.change_pos('w')
		self.assertEqual([curr_pos[0]-1,curr_pos[1]],pac.get_pos())

	def test_moveleft(self):
		curr_pos = pac.get_pos()
		pac.change_pos('a')
		new_pos = pac.get_pos()
		self.assertEqual(curr_pos[0],new_pos[0])
		self.assertEqual(curr_pos[1]-1,new_pos[1])

	def test_moveright(self):
		curr_pos = pac.get_pos()
		self.assertTrue(pac.change_pos('d'))
		new_pos = pac.get_pos()
		self.assertEqual(curr_pos[0],new_pos[0])
		self.assertEqual(curr_pos[1]+1,new_pos[1])

	def test_movedown(self):
		curr_pos = pac.get_pos()
		self.assertTrue(pac.change_pos('s'))
		new_pos = pac.get_pos()
		self.assertEqual(curr_pos[0]+1,new_pos[0])
		self.assertEqual(curr_pos[1],new_pos[1])

	def test_collect_coin(self):
		coin_pos = coins[0]
		pac.pos = coin_pos
		self.assertTrue(pac.collect_coin(pac.pos[0],pac.pos[1]))
		self.assertEqual(pac.get_score(),1)
