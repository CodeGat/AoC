from functools import cmp_to_key, reduce
from operator import indexOf

def ranking(hand: tuple[str, int]) -> list[int]:
    result: dict[str, int] = {}
    
    for card in hand[0]:
        if card in result:
            result[card] += 1
        else:
            result[card] = 1
            
    count: list[int] = sorted(list(result.values()), reverse=True)
    jokers: int = len([c for c in hand[0] if c == 'J'])
    for _ in range(jokers):
        # add one to the highest
        count[0] += 1
        # subtract one from the lowest
        if count[-1] == 1:
            count = count[:-1]
        else:
            count[-1] -= 1
    
    return sorted(count, reverse=True)

def compare_hands(h1: tuple[str, int], h2: tuple[str, int]) -> int:
    ranking: str = "J23456789TQKA"
    
    for i in range(len(h1[0])):
        i1: int = ranking.index(h1[0][i])
        i2: int = ranking.index(h2[0][i])
        
        if i1 < i2:
            return 1
        elif i1 > i2:
            return -1
    
    return 0

with open('./2023/d7/in.txt') as f:
    hands_components: list[list[str]] = [line.split() for line in f]
    hands: list[tuple[str, int]] = [(h[0], int(h[1])) for h in hands_components]
    
    hand_types: list[list[tuple[str, int]]] = [[] for _ in range(7)]
        
    for hand in hands:
        rank: list[int] = ranking(hand)  
        match rank:
            case [5]:
                hand_types[0].append(hand)
            case [4, 1]:
                hand_types[1].append(hand)
            case [3, 2]:
                hand_types[2].append(hand)
            case [3, 1, 1]:
                hand_types[3].append(hand)
            case [2, 2, 1]:
                hand_types[4].append(hand)
            case [2, 1, 1, 1]:
                hand_types[5].append(hand)
            case _:
                hand_types[6].append(hand)
    
    hand_strengths: list[list[tuple[str, int]]] = [sorted(hand, key=cmp_to_key(compare_hands)) for hand in hand_types]
    
    print(hand_strengths)
    print('-' * 10)
    
    ordering_by_strength: list[tuple[str, int]] = reduce(lambda l1, l2: l1 + l2, hand_strengths)
    
    ordering_by_lowest_rank: list[tuple[str, int]] = list(reversed(ordering_by_strength))
    winnings: list[int] = [bid * (rank + 1) for rank, (_, bid) in enumerate(ordering_by_lowest_rank)]
    
    print(sum(winnings))
    
