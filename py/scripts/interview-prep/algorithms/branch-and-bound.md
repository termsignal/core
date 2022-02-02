# Branch and Bound Algorithm


**Branch and bound** is an algorithm design paradigm which is generally used for solving combinatorial optimization problems. These problems are typically exponential in terms of time complexity and may require exploring all possible permutations in worst case. The Branch and Bound Algorithm technique solves these problems relatively quickly.

Let us consider the [**0/1 Knapsack problem**](https://www.geeksforgeeks.org/printing-items-01-knapsack/) to understand Branch and Bound.

There are many algorithms by which the knapsack problem can be solved:

* [Greedy Algorithm for Fractional Knapsack](https://www.geeksforgeeks.org/fractional-knapsack-problem/)
* [DP solution for 0/1 Knapsack](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
* [Backtracking Solution for 0/1 Knapsack](https://www.geeksforgeeks.org/printing-items-01-knapsack/).

Let’s see the Branch and Bound Approach to solve the **0/1 Knapsack problem** : The Backtracking Solution can be optimized if we know a bound on best possible solution subtree rooted with every node. If the best in subtree is worse than current best, we can simply ignore this node and its subtrees. So we compute bound (best solution) for every node and compare the bound with current best solution before exploring the node.

Example bounds used in below diagram are, A down can give $315, B down can $275, C down can $225, D down can $125 and E down can $30.

![Branch and Bound Algorithm](https://media.geeksforgeeks.org/wp-content/uploads/knapsack3.jpg "Click to enlarge")

1. [Branch and Bound | Set 1 (Introduction with 0/1 Knapsack)](https://www.geeksforgeeks.org/branch-and-bound-set-1-introduction-with-01-knapsack/)
2. [Branch and Bound | Set 2 (Implementation of 0/1 Knapsack)](https://www.geeksforgeeks.org/branch-and-bound-set-2-implementation-of-01-knapsack/)
3. [Branch and Bound | Set 3 (8 puzzle Problem)](https://www.geeksforgeeks.org/branch-bound-set-3-8-puzzle-problem/ "Permalink to Branch and Bound | Set 3 (8 puzzle Problem)")
4. [Branch And Bound | Set 4 (Job Assignment Problem)](https://www.geeksforgeeks.org/branch-bound-set-4-job-assignment-problem/ "Permalink to Branch And Bound | Set 4 (Job Assignment Problem)")
5. [Branch and Bound | Set 5 (N Queen Problem)](https://www.geeksforgeeks.org/branch-and-bound-set-4-n-queen-problem/ "Permalink to Branch and Bound | Set 5 (N Queen Problem)")
6. [Branch And Bound | Set 6 (Traveling Salesman Problem)](https://www.geeksforgeeks.org/branch-bound-set-5-traveling-salesman-problem/ "Permalink to Branch And Bound | Set 6 (Traveling Salesman Problem)")

If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
