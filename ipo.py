'''
A company registers an IPO on a website sellshares.com. All the shares on this website are available for bidding for a particular time frame called the bidding window. At the end of the bidding window an auction logic is used to decide how many of the available shares go to which bidder until all the shares that are available have been allotted, or all the bidders have received the shares they bid for, whichever comes earlier.

The bids arrive from the users in the form of <user Id, number of shares, bidding price, timestamp> until the bidding window is closed.

The auction logic assigns shares to the bidders as follows:

The bidder with the highest price gets the number of shares they bid for
If multiple bidders have bid at the same price, the bidders are assigned shares as follows: Each bidder in the same price group gets assigned one share each consecutively, with each bidder being arranged inside the group based on their timestamp. Once a bidder gets the number of shares they bid for, they will be removed from the above iterative process and the process which then continues until all bidders are removed or the shares get exhausted, whichever comes first.
List the user Id's of all users who did not get even one share after the shares have been allocated.

Input
bids: a 2D array of arrays of integers, Id, shares, price, timestamp named u, sc, bp, ts going forward
total_shares: an integer, the total shares to allocate
Output
a list of integers, each an Id for those bidders who receive no shares, sorted ascending

Examples
Example 1:
Input:

bids = [[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]]
total_shares = 18
Output: 4

Explanation:

The highest price bid is for user Id 2 for 7 shares at a price of 8, so that user gets 7 shares leaving 11 to allocate to lower prices. Users with Id's 1 and 3 each bid 5 for 5 and 7 shares, with bidder 1 having the earlier timestamp. After 5 iterations, 10 shares have been allocated with 5 shares going to each of these two bidders. Bidder 1 has the full allotment, bidder 3 has 2 more shares to buy and there is 1 share left to allocate. It goes to bidder 3 and all shares have been allotted. Bidder 4 is the only bidder who gets no shares.

Constraints
1<=n<=10^4
1<=u, sc, bp, ts, total_shares<=10^9
'''

from typing import List
from collections import OrderedDict

class Bidder:
    
    def __init__(self, u, shares, price, timestamp):
        self.u = u
        self.shares = shares
        self.price = price
        self.timestamp = timestamp
        self.received = 0

def get_unallotted_users(bids: List[List[int]], total_shares: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    
    NUM_BIDDERS = len(bids)
    
    bidders = {}
    prices = []
    
    # create bidders
    for bidder_idx in range(NUM_BIDDERS):
        price = bids[bidder_idx][2]
        bid = bids[bidder_idx]
        if price not in prices:
            prices.append(price)
            bidders[price] = []
            bidders[price].append(Bidder(bid[0], bid[1], bid[2], bid[3]))
        else:
            # seen this price before
            bidders[price].append(Bidder(bid[0], bid[1], bid[2], bid[3]))
    
    
    prices.sort(reverse=True) # sort the bids in descending order
    
    while total_shares > 0 and len(prices) > 0: # shares remain and still have bidders to allocate shares
        cur_highest_bid = prices.pop(0)
        contestant_bidders = bidders[cur_highest_bid]
        if len(contestant_bidders) > 1: # allocate shares among bidders
            total_shares_asked = sum([bidder.price for bidder in bidders[cur_highest_bid]])
            
            if total_shares_asked <= total_shares: # all contestants will get at least one share
                total_shares -= total_shares_asked
                bidders.pop(cur_highest_bid) # remove all contestants since they are all allocated
                
            else: # apportion shares among contestants, NO SHARES LEFT AFTER THIS IS DONE
                while total_shares > 0:
                    bidder = contestant_bidders.pop(0)
                    if bidder.shares > 0: # bidder still wants a share
                        bidder.received += 1
                        bidder.shares -= 1
                        total_shares -= 1
                    contestant_bidders.append(bidder)
                    
                # keep only the unallocated bidders
                for i in range(len(contestant_bidders)):
                    bidder = contestant_bidders.pop(0)
                    if bidder.received == 0:  # unallocated bidders
                        contestant_bidders.append(bidder)
                    

        else: # only one bidder at this price
            bidder = contestant_bidders.pop(0) # will get shares 
            bidder.received = bidder.shares
            print(bidder.shares)
            total_shares = max(total_shares - bidder.shares, 0)
        
    unallocated_bidder_ids = []
    if total_shares == 0: # no more shares to distribute, there is possibility of unallocated bidders
        for price, contestant_bidders in bidders.items():
            for bidder in contestant_bidders:
                if bidder.received == 0: # unallocated
                    unallocated_bidder_ids.append(bidder.u)
            
#     if len(prices) == 0: # no more bids to allocate shares to (have shares remaining after allocating to all bidders)
        
    # sort bidder ids in ascending order
    unallocated_bidder_ids.sort(reverse=False)
    return unallocated_bidder_ids

if __name__ == '__main__':
    bids = [[int(x) for x in input().split()] for _ in range(int(input()))]
    total_shares = int(input())
    res = get_unallotted_users(bids, total_shares)
    print(' '.join(map(str, res)))
