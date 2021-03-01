# In a row of trees, the i-th tree produces fruit with type tree[i].
# You start at any tree of your choice, then repeatedly perform the following steps:
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2,
# then back to step 1, then step 2, and so on until you stop.
# You have two baskets, and each basket can carry any quantity of fruit,
# but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?

import collections


def total_fruit(tree):
    c = collections.Counter()
    left = 0
    count = 0
    for i in range(len(tree)):
        c[tree[i]] += 1
        while len(c) > 2:
            c[tree[left]] -= 1
            if c[tree[left]] == 0:
                del c[tree[left]]
            left += 1
        if sum(c.values()) > count:
            count = sum(c.values())
    return count


print(total_fruit([1, 0, 0, 0, 1, 0, 4, 0, 4]))
