"""
RECURSION

Recursion is a programming technique where a function calls itself in order to solve a problem. The primary functions of recursion are to break down complex problems into simpler
or smaller instances of the same problem and to manage these smaller problems in a clean and efficient manner. Key aspects of recursion include the base case (the condition under 
which the recursion ends) and the recursive case (where the function calls itself). Here are some examples to illustrate the concept:

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

""" 
Factorial Calculation:

The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
For instance, 5! = 5 * 4 * 3 * 2 * 1.
Recursively, n! can be defined as n * (n-1)!, with the base case being 1! = 1.

"""

def factorial(n):
  if n==1:
      return 1
  else:
      return n * factorial(n - 1)

# print(factorial(5))

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
Fibonacci Sequence:

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
Recursively, the Fibonacci of n (Fib(n)) can be defined as Fib(n-1) + Fib(n-2), with base cases Fib(0) = 0 and Fib(1) = 1.

"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(5):
    print("Termino:  " + str(n) + "  =  "+ str(fibonacci(n))) # Output: 8

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""
Tree Traversal:

In data structures like trees, recursion is commonly used for traversal. For example, in a binary tree, each node has two children (left and right).
A common recursive tree traversal method is the in-order traversal, where you visit the left subtree, the node itself, and then the right subtree.

"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Example Tree
#       1
#     /   \
#    2     3
#   / \
#  4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root)  # Output: 4 2 5 1 3


#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

These examples demonstrate how recursion can simplify complex problems by breaking them down into smaller, more manageable parts. It's particularly
useful in scenarios where a problem can naturally be divided into similar sub-problems. However, it's important to handle recursion carefully to avoid
issues like stack overflow and to ensure that the base case is well-defined to terminate the recursion.

"""
