# Q1-1:

To calculate the values Q1-1, I set up a system of equations for each function, with the time varying depending on the target duration (1 second, 1 minute, etc.). The time was found by calculating how many microseconds were in each target duration.

For functions where n is able to be isolated (such as log(n), n, n^2, etc.), the equation was manipulated to solve for n.

- For log(n), the result was too large for Python to handle. To solve this, the evalf() and Pow() functions were leveraged from the sympy library.

For functions where n was unable to be isolated (n*log(n), n!), a brute force method was applied.*

* For n*log(n), the scipy.optimize.fsolve() function was leveraged from the scipy library. This function takes an initial guess (10000 used in this homework). It then uses a combination of root-finding algorithms to determine the next guess. Once the guesses converge enough towards a root, the function stops.
* For n!, the factorial() function was leveraged from the math library. Using an initial value of 'n = 1', the factorial was calculated using the factorial() function. The value of 'n' was incremented by 1 until n! was greater than or equal to the target time. The value for 'n-1' was taken as the answer, as that is the factorial that places the time at or right under the target time.

# Q2:

Looking at the time efficiency graphs for the Insertion and Merge Sorts, the Insertion not only took much longer for each data size, but also scaled faster. This was expected, as the Insertion Sort has a time efficiency of O(n^2), compared to Merge Sort's time efficiency of O(n*log(n)).
