"""tasks.py - the DATA LAYER. Nothing here talks to the model.

The model never computes a number's label; it asks this code. Session.start_task
picks a rule and hands back labeled examples, check_number verifies any number the
student tests, and next_example serves a fresh labeled example after a wrong guess.
"""

import random
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def is_square(n):
    return n >= 1 and isqrt(n) ** 2 == n


# Your Rule Bank, one entry per (rule_text, range_low, range_high INCLUSIVE, predicate).
# The predicate is the source of truth for "Works / Doesn't Work".
# Every rule below has at least 5 numbers that Work inside its range.
RULE_BANK = [
    # parity
    ("even numbers",    1,  30,  lambda x: x % 2 == 0),
    ("odd numbers",     1,  30,  lambda x: x % 2 != 0),
    ("even numbers",    30, 60,  lambda x: x % 2 == 0),
    ("odd numbers",     30, 60,  lambda x: x % 2 != 0),
    # multiples - spread across many divisors so types vary
    ("multiples of 3",  3,   30,  lambda x: x % 3 == 0),
    ("multiples of 3",  60,  90,  lambda x: x % 3 == 0),
    ("multiples of 4",  4,   40,  lambda x: x % 4 == 0),
    ("multiples of 4",  40,  80,  lambda x: x % 4 == 0),
    ("multiples of 5",  5,   30,  lambda x: x % 5 == 0),
    ("multiples of 5",  90,  120, lambda x: x % 5 == 0),
    ("multiples of 6",  6,   60,  lambda x: x % 6 == 0),
    ("multiples of 6",  60,  120, lambda x: x % 6 == 0),
    ("multiples of 7",  7,   50,  lambda x: x % 7 == 0),
    ("multiples of 7",  50,  100, lambda x: x % 7 == 0),
    ("multiples of 8",  8,   80,  lambda x: x % 8 == 0),
    ("multiples of 9",  9,   90,  lambda x: x % 9 == 0),
    ("multiples of 10", 10,  50,  lambda x: x % 10 == 0),
    ("multiples of 10", 50,  100, lambda x: x % 10 == 0),
    ("multiples of 11", 11,  99,  lambda x: x % 11 == 0),
    ("multiples of 12", 12,  120, lambda x: x % 12 == 0),
    # special shapes
    ("square numbers",  1,   50,  is_square),
    ("square numbers",  1,   100, is_square),
    ("prime numbers",   2,   30,  is_prime),
    ("prime numbers",   30,  70,  is_prime),
    ("prime numbers",   50,  100, is_prime),
]

WORKS = "Works"
DOESNT = "Doesn't Work"


class Session:
    """Holds all per-session state so the model stays stateless about numbers."""

    def __init__(self):
        self.used = set()      # rule-bank indices already played (for variety)
        self.task = None       # the active task's data
        self.shown = set()     # numbers already revealed this task

    # --- tool 1 -------------------------------------------------------------
    def start_task(self):
        """Pick a fresh rule and return its range + three labeled examples
        (2 Works, 1 Doesn't Work). Rule text is included so the model can judge
        the student's worded guess, but it must keep it secret per the prompt."""
        choices = [i for i in range(len(RULE_BANK)) if i not in self.used]
        if not choices:                      # all played -> allow repeats again
            self.used.clear()
            choices = list(range(len(RULE_BANK)))
        idx = random.choice(choices)
        self.used.add(idx)

        rule, lo, hi, pred = RULE_BANK[idx]
        inside  = [x for x in range(lo, hi + 1) if pred(x)]
        outside = [x for x in range(lo, hi + 1) if not pred(x)]
        self.task = {"rule": rule, "lo": lo, "hi": hi, "pred": pred,
                     "in": inside, "out": outside}
        self.shown = set()

        in_pick = random.sample(inside, 2)
        out_pick = random.choice(outside)
        self.shown.update(in_pick)
        self.shown.add(out_pick)

        examples = [{"number": n, "label": WORKS} for n in in_pick]
        examples.append({"number": out_pick, "label": DOESNT})
        random.shuffle(examples)
        return {"rule": rule, "range": f"{lo}-{hi}", "examples": examples}

    # --- tool 2 -------------------------------------------------------------
    def check_number(self, number):
        """True label for any number the student tests (applies the rule itself,
        so numbers outside the shown range are still judged correctly)."""
        if self.task is None:
            return {"error": "no active task - call start_task first"}
        label = WORKS if self.task["pred"](number) else DOESNT
        return {"number": number, "label": label}

    # --- tool 3 -------------------------------------------------------------
    def next_example(self):
        """One more labeled example (Works or Doesn't Work) not shown yet."""
        if self.task is None:
            return {"error": "no active task - call start_task first"}
        bag  = [(WORKS, x)  for x in self.task["in"]  if x not in self.shown]
        bag += [(DOESNT, x) for x in self.task["out"] if x not in self.shown]
        if not bag:
            return {"error": "no fresh examples left"}
        label, n = random.choice(bag)
        self.shown.add(n)
        return {"number": n, "label": label}


if __name__ == "__main__":
    # offline self-test - no model needed. Confirms every rule is playable and correct.
    for rule, lo, hi, pred in RULE_BANK:
        works = [x for x in range(lo, hi + 1) if pred(x)]
        assert len(works) >= 5, f"{rule} {lo}-{hi} has only {len(works)} Works"
        print(f"  {rule:16s} {lo:>3}-{hi:<3}  {len(works)} Works: {works}")
    print(f"\n{len(RULE_BANK)} tasks, all with >=5 Works.\n")

    s = Session()
    t = s.start_task()
    print("sample task:", t)
    print("check 7:", s.check_number(7))
    print("check 8:", s.check_number(8))
    print("next:", s.next_example())