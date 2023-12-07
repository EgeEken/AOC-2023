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

For part 1 i went through the array until i found a number, checked around the number using a big if statement, if there was a symbol around the number, i followed the line until the number ended, and once i found the full number, i added it to the sum, and replaced the following numbers with empty strings to prevent adding the same number several times.

### Part 2

Part 2 was similar but instead of finding numbers, i found asterisks, here i had to consider the possibilities of the numbers around each asterisk and what they represent, it required finding how many numbers are around, and if there's only 2, what those numbers are in full, for example

This is the paint.net page where i figured out a way to simplify all possibilities down to, it probably looks like nonsense but what it means is that i cut the sections around it into top, middle, and bottom, where middle only has two characters, so has different properties. There is a total of 4 ways to read the numbers around, so i labeled them with appropriate numbers in a way that lines them up nicely for a condition where if their sum is not exactly -1, 1, or 3, it can be discarded (except for the very unsatisfying, unfortunate edge case of top:-1, mid:1, bot:-1). 
![image](https://github.com/EgeEken/AOC-2023/assets/96302110/92c21b48-2760-4087-b717-07a173305b0f)

This system proved to be efficient enough, solving the input array i was given in only 15 milliseconds, for python i think this is a good accomplishment

</details>

## Day 4
<details><summary>(click here for details)</summary>

### Part 1

Day 4 was another simple one, solved with not much more than .split() and .isnumeric()

### Part 2

Part 2 was barely different to part 1, not much to comment on

```python
def winning(s):
    res = []
    winners, total = s.split("|")
    winners = [a for a in winners.split(": ")[1].split(" ") if a.isnumeric()]
    total = [a for a in total[:-1].split(" ") if a.isnumeric()]
    for n in total:
        if n in winners:
            res.append(n)
    return res
```
This function was the core of both parts.

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
