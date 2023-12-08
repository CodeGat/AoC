def ranking(hand: tuple[str, int]) -> list[int]:
    result: dict[str, int] = {}
    
    for card in hand[0]:
        if card in result:
            result[card] += 1
        else:
            result[card] = 1
         
    return sorted(list(result.values()), reverse=True)


with open('./2023/d7/in.txt') as f:
    hands_components: list[list[str]] = [line.split() for line in f]
    hands: list[tuple[str, int]] = [(h[0], int(h[1])) for h in hands_components]
    
    result: list[list[tuple[str, int]]] = [[] for _ in range(7)]
        
    for hand in hands:
        rank: list[int] = ranking(hand)  
        match rank:
            case [5]:
                result[0].append(hand)
            case [4, 1]:
                result[1].append(hand)
            case [3, 2]:
                result[2].append(hand)
            case [3, 1, 1]:
                result[3].append(hand)
            case [2, 2, 1]:
                result[4].append(hand)
            case [2, 1, 1, 1]:
                result[5].append(hand)
            case _:
                result[6].append(hand)
                
    print(result)
            
        