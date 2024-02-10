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

This system proved to be efficient enough, solving the input array i was given in only 14 milliseconds on average, for python i think this is a good accomplishment

<img width="185" alt="image" src="https://github.com/EgeEken/AOC-2023/assets/96302110/f72f2332-5214-426a-9b14-8e73f01ed572">


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

For this one i just did a straightforward map because it was easy and short enough and fast enough to brute force
The program first creates a map list of all the layers,
in the format of map[(range_start, range_end)] = offset
Then puts each seed through each map until it reaches the end.

### Part 2

At first i of course had to try to brute force this part by just putting each number in the new range through the system of the first question, but that did not work out, so i had to optimize.

I did it by changing the system so it works through ranges instead of single numbers, at first i was trying to make it work in a similar way but about two hours into debugging that, i had an epiphany:
This question was perfect for recursion.

First i reworked the "range_remove(r1, r2)" system i had thought of, what it does is remove r2 from r1, and return two values, one set of all the new ranges that remain, one tuple of the range that was cut, so that the cut part can be treated with the relevant offset.

Here's a visualization of it:

![image](https://github.com/EgeEken/AOC-2023/assets/96302110/45084775-e8d1-46bb-89d7-70186254a69c)

and the recursive minimum function:

```python
def recursive_min(r, mapindex, ml):
    if mapindex == len(ml):
        return r[0]
    cutset = set()
    remset = set()
    for n in ml[mapindex]:
        _, cut = range_remove(r, n)
        if cut != ():
            cutset.add(cut)
            remset.add((cut[0] + ml[mapindex][n], cut[1] + ml[mapindex][n]))
    remaining = {r}
    while len(cutset) > 0:
        c2 = cutset.pop()
        for r2 in remaining:
            rem, cut = range_remove(r2, c2)
            if cut != ():
                remaining = rem
    remset |= remaining
    return min(recursive_min(ri, mapindex + 1, ml) for ri in remset)
```

This function takes in a set of ranges from the input, the same maplist created in part 1, and a map index to know which layer we are on, then recursively applies each layer to each range, including the new ranges created during the cutting process. The recursive system ended up being very efficient which is super satisfying, especially considering the brute force solution was likely going to take days. This program finds the solution within 4 milliseconds on average:

<img width="211" alt="image" src="https://github.com/EgeEken/AOC-2023/assets/96302110/e60ca273-7b02-4aca-b307-20d88c86d75e">




</details>

## Day 6
<details><summary>(click here for details)</summary>


### Part 1

Day 6 was shockingly easy, especially after day 5 being the hardest one so far
Really nothing to note, except once again after finishing this one i decided to shorten the code and brought it down to 3 lines total for the entire day6.py file, which is of course a bigger thing than just the main function being 2 lines:

```python
res = 1
for td in list(zip([int(i) for i in open("input.txt", "r").readlines()[0][:-1].split(": ")[1].split(" ") if i.isnumeric()], [int(i) for i in open("input.txt", "r").readlines()[1][:-1].split(": ")[1].split(" ") if i.isnumeric()])): res *= len([1 for i in range(1, td[0]) if i * (td[0] - i) > td[1]])
print(res)
```

This one is "only" 299 columns unlike the one i did for day 1 by the way 

### Part 2

Part 2 was nothing special, it COULD have required some math to optimize if it was gonna take long enough but thankfully it takes less than 3 seconds to brute force so there was no point really

</details>

## Day 7
<details><summary>(click here for details)</summary>


### Part 1

Day 7 was pretty easy, but i ended up wasting a couple hours on it because i got stuck trying to make the card valuation system work properly, without realising that the text says the order of the cards matters more than the value of the cards in the hand for some reason? That changes the card comparison function from the complicated evaluation of the card type as well as the values of individual cards in them into these simple 7 lines:

```python
def compare(c1, c2):
    for i in range(len(c1)):
        if numerate(c1[i]) > numerate(c2[i]):
            return 1
        elif numerate(c1[i]) < numerate(c2[i]):
            return -1
    return 0
```

(numerate() is only for the sake of convenience/readability, it could just as well be written individually each time but that would be pretty ugly code)

```python
def numerate(c):
    return 13 - ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"].index(c)
```


### Part 2

Part 2 was not too different, simply required the addition of Joker cards as bonus points whenever available, not much to comment

</details>

## Day 8
<details><summary>(click here for details)</summary>

### Part 1

Day 8 was very easy too, really not much more than parsing the input text and following the route instructions as given, my whole python file for the part 1 solution is only 30 lines long

### Part 2

Part 2 had a little problem with the description not specifying a specific property in the given input set that does not necessarily have to be there, because WITH that property, you can simply use LCM (Lowest Common Multiple) to find the answer pretty easily, but without that property you would have no choice but to actually brute force it the entire way, or at least twice for each loop if you did manage to fully optimize it, and brute forcing simply does not work because of how many iterations you need.

That property being the assumption that the size of the loop (from Z, back to Z) is always the same as the size as the distance to reach the end (from A, to Z).

This felt a little unsatisfying as a solution because it relied on a hidden property of the given input rather than the system given in the question itself


</details>

## Day 10
<details><summary>(click here for details)</summary>

### Part 1

Part 1 was pretty straightforward, many different ways to go about the problem though. I solved it by sending a signal from both sides of the starting point, until they meet at the furthest side of the pipes, when they do, the iteration count will be the answer.

### Part 2

I could not finish part 2, as i did not have the time to rewrite the whole system after realising that i have to account for the gaps between pipes, and not just what tile is or is not inside the main loop, at that time i did not have more hours to spare, and when i was finally done with exams and all, advent of code 2023 was already finished and i did not have the motivation to go back and finish everything now that everyone had already moved on. Maybe next year i'll be able to finish it, stay tuned :)

</details>

<br /> 
