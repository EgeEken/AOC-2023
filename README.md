# AOC-2023
My solutions for the puzzles in Advent of Code 2023


## Day 1
<details><summary>(click here for details)</summary>

### Part 1

Part 1 was pretty straightforward, i just checked each character with .isnumeric()

### Part 2

Part 2 was a little more complex but thanks to .find() and .rfind() on python (i searched "find first occurence of substring python" on google), it was pretty easy, if i was using another language i think the best approach would be to simply make those functions yourself, which wouldnt even really be hard all it does is check to find the first occurrence of a substring

After i solved it i tried to make the calibrate(s) function in as little lines as possible, with no regard to its efficiency or readability, and came up with this monstrosity:

```python
def calibrate(s):
    first, last = ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))))] if min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))) > min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))) else ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))))], ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.rfind(x), ["1", "2", "3", "4", "5", "6", "7", "8", "9"])).index(max(list(map(lambda x: s.rfind(x), ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))))] if max(list(map(lambda x: s.rfind(x), ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))) > max(list(map(lambda x: s.rfind(x), ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))) else ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.rfind(x), ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])).index(max(list(map(lambda x: s.rfind(x), ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))))]
    return int(["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))))] if min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))) > min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))) else ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))))] + ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))))] if min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))) > min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))) else ["1", "2", "3", "4", "5", "6", "7", "8", "9"][list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"])).index(min(list(map(lambda x: s.find(x) if s.find(x) != -1 else len(s) + 1, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))))]) if last == -1 else int(first + last)
```

The second line is **1849 characters** if you are curious. There shouldn't technically be anything preventing me from dropping this down to 1 line actually since all i did to shorten is was replace every variable name with.. the actual code making the variable, hence why you see the same sections pop up several times each, but this stopped working at this point due to what i'm guessing is a problem with python, replacing the "first" variable in the second line with the first variable value itself breaks it for some reason. Well 2 lines still isnt that bad i'll take it.

</details>

## Day 2
<details><summary>(click here for details)</summary>

### Part 1

Another straightforward solution, .split() just about solves this day entirely

### Part 2

Slightly more complicated, but essentially the same method to solve part 2, not much to comment on

```python
for sect in ("".join(s.split(": ")[1])).split("; "):
        colors = dict()
        for c in sect.split(", "):
            colors[c.split(" ")[1] if "\n" not in c.split(" ")[1] else c.split(" ")[1][:-1]] = int(c.split(" ")[0])
```
This part is shared in both parts

</details>

## Day 3
<details><summary>(click here for details)</summary>

### Part 1

### Part 2

</details>

## Day 4
<details><summary>(click here for details)</summary>

### Part 1

### Part 2

</details>

## Day 5
<details><summary>(click here for details)</summary>

### Part 1

### Part 2

</details>

## Day 6
<details><summary>(click here for details)</summary>

### Part 1

### Part 2

</details>
