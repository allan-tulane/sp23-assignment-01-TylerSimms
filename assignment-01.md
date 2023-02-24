

# CMPS 2200 Assignment 1

**Name:** Tyler Simms


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  $2^{n+1} \in O(2^n)$ is true. $2^{n+1}$ is equal to 2*2^n. Using the definition of asymptotic dominance, 2*2^n <= c * 2^n when c = 2 and n >= 1, 2*2^n <= 2 * 2^n. Therefore, $2^{n+1} \in O(2^n)$ is indeed true.
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  $2^{2^n} \in O(2^n)$ is false. Exponents can be directly compared when the exponents have the same base. Both expressions have the same base so the exponents can be compared. 2^n grows much faster than n. No value for c in 2^{2^n} <= c * 2^n can make up the difference for most given values of n. The exponent 2^n is just far too great when the value of n is significantly large.
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  $n^{1.01} \in O(\mathrm{log}^2 n)$ is false. n^{1.01} is almost linear. Once n is equal to 15, n^{1.01} is larger than \mathrm{log}^2 n, using base 2 for the log. No value for c in $n^{1.01} <= c * \mathrm{log}^2 n can make up the difference when n is significantly large.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  $n^{1.01} \in \Omega(\mathrm{log}^2 n)$ is true. n^{1.01} is almost linear. Once n is equal to 15, n^{1.01} is larger than \mathrm{log}^2 n, using base 2 for the log. No value for c in $n^{1.01} >= c * \mathrm{log}^2 n can make the expression false when n is significantly large.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  $\sqrt{n} \in O((\mathrm{log} n)^3)$ is false. At first, it appears that \mathrm{log} is larger than \sqrt{n} starting when n is equal to 3, using base 2 for the log. However, sqrt{n} eventually becomes larger than (\mathrm{log} n)^3 at large values of n. No value for c in \sqrt{n} <= c * (\mathrm{log} n)^3 can make up the difference when n is significantly large.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
    $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$ is true. \mathrm{log} n)^3 looks like it is larger than \sqrt{n} starting when n is equal to 3, using base 2 for the log. However, sqrt{n} eventually becomes larger than (\mathrm{log} n)^3 at large values of n. No value for c in \sqrt{n} >= c * (\mathrm{log} n)^3 can make the expression false when n is significantly large.

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
  
This function takes one argument, named x. Foo then checks whether x is less than or equal to 1 using an if statement.
If the condition is true, x is returned. If the condition is false, an else statement is executed. The else statement's
code block creates two local variables, ra and rb. ra is assigned a recursive call of foo with the argument x-1. rb is
assigned a recursive call of foo with the argument x-2. The sum of ra and rb is returned and the function ends. The
function's purpose is to ultimately return the number in the Fibonacci sequence that corresponds with the index given as
the argument x, assuming the indexes begin at 0 instead of 1. For example, entering 10 as x will make foo return 55 because
55 is the number in the Fibonacci sequence at index 10, making sure to remember that the indexes begin at 0.

.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

  The work of this implementation is O(n). The span is also O(n).

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  

  The work of this algorithm is O(n). The span is O(n).
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

  The work of this algorithm is O(n). The span is O(logn).
.  
.  
.  
.  
.  
.  
.  
.  

