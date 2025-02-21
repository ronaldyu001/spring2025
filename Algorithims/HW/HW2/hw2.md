# Q1-1:

To calculate the values Q1-1, I set up a system of equations for each function, with the time varying depending on the target duration (1 second, 1 minute, etc.). The time was found by calculating how many microseconds were in each target duration.

For functions where n is able to be isolated (such as log(n), n, n^2, etc.), the equation was manipulated to solve for n.

- For log(n), the result was too large for Python to handle. To solve this, the evalf() and Pow() functions were leveraged from the sympy library.

For functions where n was unable to be isolated (n*log(n), n!), a brute force method was applied.* 

* For n*log(n), the scipy.optimize.fsolve() function was leveraged from the scipy library. This function takes an initial guess (10000 used in this homework). It then uses a combination of root-finding algorithms to determine the next guess. Once the guesses converge enough towards a root, the function stops.
* For n!, the gamma() function was leveraged from the math library. This gamma function accounts for decimal values, unlike the factorial() function. An initial value of n = 1 was used, and incremented by .000001 until the value is equal to or greater than the target time. A small increment was used to improve the accuracy of the gamma function, with a longer runtime being the cost. However, the runtime is not unreasonable.
