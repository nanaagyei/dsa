# Data Structures and Algorithms in Python

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

> A comprehensive collection of data structures and algorithm implementations in Python, featuring LeetCode solutions and classical CS algorithms built from scratch.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Individual Files](#running-individual-files)
  - [Example Usage](#example-usage)
- [Content Categories](#content-categories)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
  - [LeetCode Problems](#leetcode-problems)
- [Contributing](#contributing)
  - [How to Contribute](#how-to-contribute)
  - [Code Guidelines](#code-guidelines)
  - [Contribution Ideas](#contribution-ideas)
- [Code of Conduct](#code-of-conduct)
- [Learning Resources](#learning-resources)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Overview

Welcome to the **Data Structures and Algorithms in Python** repository! This project is a comprehensive learning resource and reference implementation for fundamental computer science concepts, data structures, and algorithmic problem-solving.

This repository serves multiple purposes:
- 📚 **Learning Resource**: Study implementations of classic data structures and algorithms
- 💡 **Interview Preparation**: Practice with curated LeetCode problems from "Grind 75" and beyond
- 🔍 **Reference Implementation**: Clean, well-documented Python code following best practices
- 🎯 **Skill Building**: Understand algorithmic thinking and problem-solving patterns

Whether you're a student learning these concepts for the first time, a professional preparing for technical interviews, or an educator looking for teaching materials, this repository provides clear, understandable implementations of essential computer science concepts.

## Features

- ✅ **Custom Implementations**: Data structures built from scratch without external libraries
- ✅ **100+ LeetCode Solutions**: Curated problems with clear, efficient solutions
- ✅ **Well-Documented Code**: Clear comments and docstrings explaining logic
- ✅ **Multiple Algorithm Categories**: Sorting, searching, graph algorithms, dynamic programming, and more
- ✅ **Educational Focus**: Code written for clarity and learning
- ✅ **Active Development**: Continuously updated with new problems and improvements

## Repository Structure

```
dsa/
│
├── data_structures_algos/      # Core data structure implementations
│   ├── binary_heap.py          # Min/Max heap implementation
│   ├── linked_list.py          # Singly and doubly linked lists
│   ├── tree.py                 # Binary tree operations
│   ├── trie.py                 # Prefix tree implementation
│   ├── stack_queues.py         # Stack and queue structures
│   ├── bubble_sort.py          # Bubble sort algorithm
│   ├── insertion_sort.py       # Insertion sort algorithm
│   ├── quicksort.py            # Quicksort algorithm
│   ├── dijkstra_algorithm.py   # Shortest path algorithm
│   └── ...                     # More implementations
│
├── leetcode-problems/          # LeetCode problem solutions
│   ├── two_sum.py              # Array/Hash table problems
│   ├── binary_search.py        # Binary search variations
│   ├── merge_two_sorted_lists.py  # Linked list problems
│   ├── valid_parentheses.py    # Stack problems
│   ├── invert_binary_tree.py   # Tree problems
│   ├── clone_graph.py          # Graph problems
│   ├── combination_target_sum.py  # Backtracking problems
│   ├── longest_common_subsequence.py  # DP problems
│   └── ...                     # 100+ problem solutions
│
├── Root Level Files/           # Additional algorithm exercises
│   ├── fib.py                  # Fibonacci implementations
│   ├── dynamic_programming_ex.py  # DP examples
│   ├── recursion_exercise.py   # Recursion practice
│   ├── simple_graph.py         # Graph algorithms
│   └── ...                     # More exercises
│
└── README.md                   # This file
```

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- A code editor (recommended: [VS Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/nanaagyei/dsa.git
   cd dsa
   ```

2. **Verify Python installation**

   ```bash
   python --version
   # or
   python3 --version
   ```

3. **No external dependencies required!**
   
   This repository uses only Python's standard library, so no package installation is needed.

## Usage

### Running Individual Files

Each Python file is self-contained and can be run independently:

```bash
# Run a specific data structure implementation
python data_structures_algos/linked_list.py

# Run a LeetCode solution
python leetcode-problems/two_sum.py

# Run an algorithm example
python fib.py
```

### Example Usage

Here's how to use the LinkedList implementation:

```python
from data_structures_algos.linked_list import LinkedList

# Create a new linked list
ll = LinkedList()

# Insert elements
ll.insert(3)
ll.insert(2)
ll.insert(1)

# Print the list
ll.print_list()  # Output: 1, 2, 3

# Read element at index
print(ll.read(1))  # Output: 2

# Get list length
print(ll.length())  # Output: 3

# Reverse the list
ll.reverse()
ll.print_list()  # Output: 3, 2, 1
```

Example with a LeetCode solution:

```python
from leetcode_problems.two_sum import Solution

# Create solution instance
sol = Solution()

# Example test case
nums = [2, 7, 11, 15]
target = 9

# Find indices
result = sol.twoSum(nums, target)
print(result)  # Output: [0, 1]
```

## Content Categories

### Data Structures

The `data_structures_algos/` directory contains implementations of:

- **Linear Data Structures**
  - Linked Lists (Singly & Doubly)
  - Stacks
  - Queues
  
- **Tree Data Structures**
  - Binary Trees
  - Binary Heaps (Min/Max)
  - Tries (Prefix Trees)

- **Advanced Structures**
  - Graphs (adjacency list/matrix)
  - Hash Tables/Maps

### Algorithms

Comprehensive algorithm implementations including:

- **Sorting Algorithms**
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Quick Sort
  - Merge Sort (in various problem solutions)

- **Searching Algorithms**
  - Binary Search
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)

- **Graph Algorithms**
  - Dijkstra's Shortest Path
  - Graph Traversal
  - Clone Graph
  - Flood Fill

- **Dynamic Programming**
  - Fibonacci Sequences
  - Longest Common Subsequence
  - Maximum Subarray
  - Climbing Stairs
  - And more...

- **Other Paradigms**
  - Recursion
  - Backtracking
  - Greedy Algorithms
  - Two Pointers
  - Sliding Window

### LeetCode Problems

The repository contains 100+ LeetCode problem solutions organized by topic:

- **Arrays & Hashing**: Two Sum, Group Anagrams, Product Except Self
- **Two Pointers**: Valid Palindrome, Container With Most Water
- **Sliding Window**: Longest Substring, Minimum Window
- **Stack**: Valid Parentheses, Daily Temperatures, Largest Rectangle
- **Binary Search**: Search Rotated Array, Koko Eating Bananas
- **Linked Lists**: Reverse List, Merge Lists, Detect Cycle
- **Trees**: Invert Tree, Max Depth, Lowest Common Ancestor
- **Tries**: Implement Trie, Word Search
- **Heap/Priority Queue**: Kth Largest, Median from Stream
- **Backtracking**: Combination Sum, Permutations, Word Search
- **Graphs**: Number of Islands, Course Schedule, Clone Graph
- **Dynamic Programming**: Climbing Stairs, Coin Change, LCS
- **Greedy**: Jump Game, Gas Station
- **Intervals**: Merge Intervals, Insert Interval
- **Math & Geometry**: Rotate Image, Spiral Matrix
- **Bit Manipulation**: Number of 1 Bits, Counting Bits

Many solutions are from the popular **"Grind 75"** interview preparation list.

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding new algorithms, improving documentation, or optimizing existing solutions, your help is appreciated.

### How to Contribute

1. **Fork the repository**
   
   Click the "Fork" button at the top right of this page.

2. **Clone your fork**

   ```bash
   git clone https://github.com/YOUR-USERNAME/dsa.git
   cd dsa
   ```

3. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

   Use descriptive branch names like:
   - `feature/add-avl-tree`
   - `fix/linked-list-bug`
   - `docs/improve-readme`

4. **Make your changes**

   - Write clear, readable code
   - Follow existing code style
   - Add comments and docstrings
   - Test your changes

5. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

   Use conventional commit messages:
   - `Add: new feature or file`
   - `Fix: bug fix`
   - `Update: improvements to existing code`
   - `Docs: documentation changes`

6. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of your changes
   - Reference any related issues

### Code Guidelines

Please follow these guidelines when contributing:

- **Code Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python style guide
- **Naming**: Use descriptive variable and function names
- **Comments**: Add comments explaining complex logic
- **Docstrings**: Include docstrings for functions and classes
- **Type Hints**: Consider adding type hints for better code clarity (optional)
- **Dependencies**: Avoid external dependencies; use standard library when possible
- **File Organization**: Place files in appropriate directories
- **Testing**: Test your code before submitting

**Example of good code style:**

```python
def binary_search(arr: list, target: int) -> int:
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Contribution Ideas

Not sure where to start? Here are some ideas:

- **Add New Algorithms**
  - Advanced sorting algorithms (Radix Sort, Counting Sort, Heap Sort)
  - String algorithms (KMP, Rabin-Karp, Z-Algorithm)
  - Advanced graph algorithms (Bellman-Ford, Floyd-Warshall, A*)
  - Advanced tree structures (AVL Trees, Red-Black Trees, B-Trees, Segment Trees)

- **Add More LeetCode Solutions**
  - Medium and Hard difficulty problems
  - Less common problem categories
  - Alternative solutions with different approaches

- **Improve Existing Code**
  - Optimize time/space complexity
  - Add edge case handling
  - Improve code readability
  - Add more comprehensive comments

- **Documentation**
  - Add complexity analysis (Big O notation)
  - Create tutorials or explanations
  - Add more usage examples
  - Improve inline documentation

- **Testing**
  - Add unit tests
  - Add example test cases
  - Create test utilities

- **Organization**
  - Better file categorization
  - Add problem difficulty labels
  - Create index files for easier navigation

## Code of Conduct

This project is dedicated to providing a welcoming and inclusive environment for everyone. We expect all contributors to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

Please be professional and courteous in all interactions. Harassment, trolling, or discriminatory behavior will not be tolerated.

For more details, see the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

## Learning Resources

Here are some excellent resources for learning data structures and algorithms:

### Books
- **"Introduction to Algorithms"** by Cormen, Leiserson, Rivest, and Stein (CLRS)
- **"Algorithm Design Manual"** by Steven Skiena
- **"Grokking Algorithms"** by Aditya Bhargava
- **"Elements of Programming Interviews in Python"** by Aziz, Lee, and Prakash

### Online Platforms
- [LeetCode](https://leetcode.com/) - Practice coding problems
- [HackerRank](https://www.hackerrank.com/) - Coding challenges and tutorials
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - DSA tutorials and articles
- [VisuAlgo](https://visualgo.net/) - Algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Time/space complexity reference

### Courses
- [Algorithms Specialization](https://www.coursera.org/specializations/algorithms) - Coursera (Stanford)
- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)
- [Princeton Algorithms Course](https://www.coursera.org/learn/algorithms-part1)

### YouTube Channels
- [Abdul Bari](https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw)
- [Back To Back SWE](https://www.youtube.com/c/BackToBackSWE)
- [NeetCode](https://www.youtube.com/c/NeetCode)

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 nanaagyei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contact

- **GitHub**: [@nanaagyei](https://github.com/nanaagyei)
- **Repository**: [https://github.com/nanaagyei/dsa](https://github.com/nanaagyei/dsa)

Feel free to open an issue for:
- 🐛 Bug reports
- 💡 Feature requests
- 📖 Documentation improvements
- ❓ Questions about implementations

## Acknowledgments

- **LeetCode** for providing an excellent platform for practicing algorithms
- **The "Grind 75"** list for curating essential interview problems
- **The Python Community** for creating an accessible and powerful language
- **All Contributors** who help improve this repository

---

**Happy Coding! 🚀**

*If you find this repository helpful, please consider giving it a ⭐ star to support the project!*
