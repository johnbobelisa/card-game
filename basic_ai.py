from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
import time

class BasicAIPlayer(Player):

	"""Creates a Basic AI player, and determines how they play the game"""
	
	def play_card(self, trick: list[Card], broken_hearts: bool)-> Card:
		"""
		Defines Basic AI card logic for playing cards.
		Arguments:
			trick => a list of Card being played by others
			broken_hearts => True or False if hearts has been broken
		
		Returns the weakest legally playable Card
		"""
		
		valid_cards = []
		for card in self.hand:												#checks for all playable cards
			if super().check_valid_play(card,trick,broken_hearts)[0]:
				valid_cards.append(card)
		weakest = min(valid_cards)											#choose the lowest rank and suit cards among the playable cards
		self.hand.remove(weakest)
		time.sleep(2)
		return weakest

	def pass_cards(self) -> list[Card]:
		"""
		Defines Basic AI logic for passing cards.
		Returns a list of three weakest Card to pass
		"""
		self.hand.sort()
		cards_passed = self.hand[-3:]										#passes the three strongest cards (due to sort)
		for card in cards_passed:
			self.hand.remove(card)
		return cards_passed

if __name__ == "__main__":
	import random
	for _ in range(100):				#change range to run multiple times to test for error message. your code should be able to withstand a lot of scenerios
		deck = []
		for suit in Suit:
			for rank in Rank:
				deck.append(Card(rank,suit))    
		player1 = BasicAIPlayer("Test Player 1")
		player1.hand = []
		for i in range(13):
			random_card = random.choice(deck)
			player1.hand.append(random_card)
			deck.remove(random_card)
#		trick = random.choice([random.choice(deck),[]])
		trick = random.choice([random.choice(deck)])
		if trick:
			trick = [trick]
		broken_hearts = random.choice([True,False])
		player1.hand.sort()
		rand_card = random.choice(player1.hand)
		print((player1.hand))
		print(f"\nTrick:{(trick)}, Broken Hearts:{broken_hearts}")
		print(f"Valid play check: {player1.check_valid_play(rand_card, trick, broken_hearts)}\nCard tested: {rand_card}")
		print(f"\nCard played: {player1.play_card(trick,broken_hearts)}")#			, Valid Play: {player1.check_valid_play(player1.play_card(trick,broken_hearts), trick, broken_hearts)[0]}")
		print(f"Card passed: {(player1.pass_cards())}")