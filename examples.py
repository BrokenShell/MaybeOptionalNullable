import random
from typing import Callable, Any, Union, List

MaybeCallable = Union[Callable[..., Any], Any]


def shimmering_gem() -> str:
    return f"A shimmering {random.choice(['ruby', 'emerald', 'sapphire'])}"


def sided_die() -> str:
    return f"A {random.randint(1, 20)}-sided die made of {random.choice(['bone', 'wood', 'crystal'])}"


def spell_scroll() -> str:
    return f"A scroll containing {random.choice(['fireball', 'invisibility', 'healing'])} spell"


def key_set() -> str:
    return f"A set of keys made from {random.choice(['iron', 'silver', 'gold'])}"


def magical_ring() -> str:
    return f"A magical ring that glows {random.choice(['red', 'blue', 'green'])}"


def flatten(maybe_callable: MaybeCallable, *args, **kwargs) -> Any:
    if callable(maybe_callable):
        return flatten(maybe_callable(*args, **kwargs))
    else:
        return maybe_callable


def get_random_treasure(treasure_table: List[MaybeCallable]) -> str:
    treasure = random.choice(treasure_table)
    return flatten(treasure)


if __name__ == '__main__':
    treasure_table_1: List[MaybeCallable] = [
        "A pile of gold coins",
        shimmering_gem,
        "A dusty old map",
        sided_die,
        "A mysterious potion bottle",
        spell_scroll,
        "A knight's sword, rusted with age",
        key_set,
        "An ancient book with unreadable text",
        magical_ring
    ]

    for _ in range(5):
        print(get_random_treasure(treasure_table_1))
