'''
Created on 22 Aug 2022
@author: CMP
'''

import numpy as np
import regex as re


class Coins(object):
    # Available denominations in pence stirling.
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]

    def __init__(self, total):
        self.total = total

    def __call__(self):
        total_pence = self.parse_input()
        odd_combinations = self.change(total_pence)
        return odd_combinations

    def parse_input(self):
        """
        Parse input string of format `£0-0`. Compute equivalent pence total. 
        """
        assert isinstance(self.total, str), f'`parse_input` requires an input \
            of type `String`. Received input {type(self.total)}.'

        # Parse input string as pounds, pence
        matches = re.findall(r'(\d+(?:\.\d+)?)\b', self.total)

        # Separate
        pounds, pence = matches[0], matches[1]

        # Convert to whole pence. Adjust for single digit inputs
        pence = int(pence) * 10 if len(pence) == 1 else int(pence)

        # Compute total in pence.
        pence_total = (int(pounds) * 100) + pence
        return pence_total

    def change(self, total_pence) -> int:
        """
        Solves dynamic programming problem (dp): Return all possible odd 
        combinations of `coins` that sum to `total`.
        
        Args:
            total: `Int`. An Integer representing the total that a combination must 
                sum to.
            coins: List. A `Python` `List` of available `coins`.
        Returns:
            dp_odd: `Int`. An Integer representing the total odd combinations whose
                sum equals `total`. 
        """
        # Total decision space.
        dp = [0] * (total_pence + 1)
        dp[0] = 1
        for coin in self.COINS:
            for j in range(coin, total_pence + 1):
                dp[j] += dp[j - coin]

        # Odd combinations
        dp_odd = []
        for c in dp[:total_pence]:
            if c % 2 > 0:
                dp_odd.append(c)

        # Get total
        return dp_odd[-1]
