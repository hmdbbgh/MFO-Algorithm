=======================================
Moth-Flame Optimization Algorithm (MFO)
=======================================

**Contents:**

.. contents:: :local:

Introduction
------------

Optimization Algorithms
~~~~~~~~~~~~~~~~~~~~~~~

Optimization points out to the process of finding best solution(s) for a specific problem.
Throughout the last few decades with complexity growth of problems, demand of new optimization
tactics became more obvious. 

Before the suggestion of Heuristic optimization tactics, mathematical optimization tactics were the only optimization tool for
problems. Mathematical optimization tactics are mostly deterministic therefore they have local optims issues.
On the other hand meta-heuristic algorithms start from some initial solution and will get close to the solution through next iterations.

Some of the famous meta-heuristic algorithms are Genetic optimization, Grey Wolf optimization, Ant Colony optimization and ...

Introduction of Moth-Flame algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Moth-Flame optimization algorithm also known as MFO or Moth-Flame algorithm is one of the optimization
and meta-heuristic algorithms that finds a solution for the problem from the behavior of the moths around flame or fire.

This algorithm was proposed by Seyed Ali Mirjalili as an article named 
Moth-flame optimization algorithm: A novel nature-inspired heuristic paradigm in Knowledge-Based Systems journal back in 2015.
This algorithm is a modern heuristic algorithm inspired by nature, moth's behavior and their interest in flame or fire.


Algorithm
---------

What is MFO algorithm?
~~~~~~~~~~~~~~~~~~~~~~

Here we have a new optimization algorithm inspired by nature called Moth-Flame optimization algorithm
or Moth and Flame. 

The original inspiration of this optimization is moth's navigation method in nature
called transverse orientation. Moth's fly long distances through the night by amintaining a fixed angle
with respect to the moon. However, these fancy insects are trapped in a useless/deadly spiral path around artificial lights.

Moth-Flame Optimizer
~~~~~~~~~~~~~~~~~~~~

Moths are fancy insects, which are highly similar to the family of butterflies. Basically, there are over 160,000 various species of
this insect in nature. They have two main milestones in their lifetime: larvae and adult. The larvae is converted to moth in cocoons.

The most interesting fact about moths is their special navigation methods at night. They have been evolved to fly in night using
the moon light. They utilized a mechanism called transverse orientation for navigation. In this method, a moth flies by maintaining a
fixed angle with respect to the moon, a very effective mechanism for travelling long distances in a straight path.

Example
~~~~~~~

.. image:: https://github.com/hmdbbgh/MFO-Algorithm/blob/dev-README/Media/Pics/Pic.1.png

Pic. 1 shows a conceptual model of transverse orientation. Since the moon is far away from the moth,
this mechanism guarantees flying in straight line. 

The same navigation method can be done by humans. Suppose that the moon is in the south side of the sky and a human wants to go the east.
If he keeps moon of his left side when walking, he would be able to move towards the east on a straight line.

Despite the effectiveness of transverse orientation, we usually observe that moths fly spirally around the lights.
In fact, moths are tricked by artificial lights and show such behaviours. This is due to the inefficiency of
the transverse orientation, in which it is only helpful for moving in straight line when the light source is very far.
When moths see a human-made artificial light, they try to maintain a similar angle with the light to fly in straight line.

    Pic. 2

Since such a light is extremely close compared to the moon, however, maintaining a similar angle to the light source causes a
useless or deadly spiral fly path for moths. A conceptual model of this behaviour is illustrated in Pic. 2.
It may be observed in Pic. 2 that the moth eventually converges towards the light. This behaviour is modeled
mathematically to propose an optimizer called Moth-Flame Optimization (MFO) algorithm in the following subsection.

Explanation of MFO algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the proposed MFO algorithm, it is assumed that the candidate solutions are moths and the problem’s variables are
the position of moths in the space. Therefore, the moths can fly in 1-D, 2-D, 3-D, or hyper dimensional space with
changing their position vectors. 

Since the MFO algorithm is a population-based algorithm, the set of moths is 
represented in a matrix where n is the number of moths and d is the number of variables (dimension). For all the moths,
we also assume that there is an array for storing the corresponding fitness values where again n is the number of moths.

    Pic. 3

Note that moths and flames are both solutions. The difference between them is their approach and update methods in each iteration.
Moths are the actual search agents that move in the search space, while flames are moth's best calculated postion by far.
In other words, flames are flags/pins that are dropped by moths while searching the search space. Thus each moth searches around
a flag (flame) and updates it in case of finding a better solution. With this mechanism, a moth won't ever loses its best solution.

Initial values
~~~~~~~~~~~~~~

!! We could use any random disturbion for generating initial solutions and calulating fitness values for each solution.
This method is applied as default in which 'ub' is the upper bound and 'lb' is the lower bound for variable 'i'.
Therefore for 'n' in dimension 'd' will be able to generate ininial solutions. We can calculate the fitness for each
solution after initialization, thus the fitness function value of matrix 'M' will be 'OM'.

    Pic. 4

Algorithm iterations
~~~~~~~~~~~~~~~~~~~~

After the initialization, the 'P' function will iteratively run until the 'T' function returns true. The P function is the main function
that moves the moths around the search space. As mentioned above the inspiration of this algorithm is the transverse orientation.

Logaritmic spiral
~~~~~~~~~~~~~~~~~

A logarithmic spiral is chosen as the main update mechanism of moths in this paper. However, any types of spiral can be applied
here subject to the following conditions:

    **-Spiral’s initial point should start from the moth.**
    
    **-Spiral’s final point should be the position of the flame.**
    
    **-Fluctuation of the range of spiral should not exceed from the search space.**

Considering these points, a logarithmic spiral is defined for the MFO algorithm as follows:
    
    Pic. 5

where 'D(i)' indicates the distance of the 'i-th' moth for the 'j-th' flame, 'b' is a constant for defining the shape of
the logarithmic spiral, and 't' is a random number in [1, 1].

    Pic. 6

Equation shown in Pic. 5 is where the spiral flying path of moths is simulated. As may be seen in this equation, the next position of a moth is
defined with respect to a flame. The t parameter in the spiral equation defines how much the next position of the moth should be
close to the flame ('t' = '-1' is the closest position to the flame, while 't' = '1' shows the farthest). Therefore, a hyper ellipse
can be assumed around the flame in all directions and the next position of the moth would be within this space.

    Pic. 7

The spiral movement is the main component of the proposed method because it dictates how the moths update their positions around flames.
The spiral equation allows a moth to fly "around" a flame and not necessarily in the space between them.
Therefore, the exploration and exploitation of the search space can be guaranteed.
The logarithmic spiral, space around the flame, and the position considering different t on the curve are illustrated in Pic. 7.

    Pic. 8

Pic. 8 shows a conceptual model of position updating of a moth around a flame. Note that the vertical axis shows only one dimension
(1 variable/parameter of a given problem), but the method can be apllied for changing all the variables of the problem.
The possible positions (dashed black lines) that can be chosen as the next position of the moth (blue horizontal line) around the flame 
(green horizontal line) clearly show that a moth can explore and expliot the search space around the flame in one dimension.

Exploration happens when the next position is outside the space between the moth and flame as can be seen in the arrows labelled by 1, 3, and 4.
Exploitation occurs when the next position is inside the space between the moth and flame as can be observed in the arrow labelled by 2.

Conclusion
----------

The nethod of MFO algorithm was explained in this article. The algorithm proposes a model corresponding to flying moths behavior around a flame
so that possible solutions (the moths) converge to optimezed answers (flames).

This algorithm has so many applications in solving NP-Hard and continuous problems and by relying on the original article, this method
can be used to solve so many difficult problems.
