import nltk
from typing import List, Set

# 0. words is a list of all valid English words
words = set(nltk.corpus.words.words())

# 1. Define chain, a function which takes a start and target word
# of equal length (this is guaranteed by the caller).
# Return a list of words that chain the start and target by
# changing one letter at a time
# e.g. (cat, dog) -> [cat, cot, cog, dog]

class InvalidWord(Exception):
    pass

def chain(start: str, target: str) -> List[str]:
    if start not in words:
        raise InvalidWord(start)
    if target not in words:
        raise InvalidWord(target)

    result = [start]

    if start == target:
        return result

    full_candidates = {w for w in words if len(w) == len(start)}
    next_candidates = next_words(start, full_candidates)
    if target in next_candidates:
        return result + [target]
    
    return []

def _chain(start, target):
    if start == target:
        return [start]

    candidates = {w for w in words if len(w) == len(start)}
    next_candidates = next_words(start, candidates)
    steps = [_chain(x, target) for x in next_candidates]


def one_char_different(left: str, right: str) -> bool:
    if len(left) != len(right):
        return False
    different = False
    for (a,b) in zip(left, right):
        if a != b:
            if different:
                return False
            else:
                different = True
    return different

def next_words(start: str, candidates: Set[str]) -> Set[str]:
    return {x for x in candidates if one_char_different(start, x)}


# 2. Alter chain to return the *shortest* list of words
