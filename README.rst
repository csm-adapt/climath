=======
climath
=======

This allows the user to perform a number of common mathematical
operations on a list of numbers. This is a framework that can be
easily extended to any number of operations. The initial set of
capabilities (add, subtract, multiply, divide, mean, median, and std)
took less than two minutes each to develop.


Description
===========

The primary goal of this code was to provide a template for creating
commands/programs with any number of subcommands. But why not make a
template that has some actual value? Within the first afternoon, this
had grown into a program with a much larger scope.

TODO
====

* Add basic plotting tools.
    * Lines
        * `climath plot line x1 x2 x3 ...`
        * `climath plot line --scatter x1 x2 x3 ...`
    * Histogram
        * `climath plot hist x1 x2 x3 ...`
        * `climath plot hist --nbins=32 x1 x2 x3 ...`
    * Statistics to plot a histogram and overlaid statistical fit.
        * `climath plot gaussian x1 x2 x3 ...`
        * `climath plot gaussian --nbins=32 x1 x2 x3 ...`
        * `climath plot gaussian --rug x1 x2 x3 ...`
* Add additional statistical operations to `reduce`:
    * iqr
    * mode
    * Parameterization/fit to
        * `stats.gaussian`
        * `stats.laplace`
        * ...

Note
====

This project has been set up using PyScaffold 3.0.3. For details and usage
information on PyScaffold see http://pyscaffold.org/.
