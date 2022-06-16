Approach #1: Group By Character

Given s = "00110011", we can compute groups = [2, 2, 2, 2]
where every element represents groups of adjacent characters
that are all the same value.

We can then compute count to be the sum of min(groups[i], groups[i+1])
= min(s[0], s[1]) + min(s[1], s[2]) + min(s[2], s[3]) 
= min(2, 2) + min(2, 2) + min(2, 2) = 6
