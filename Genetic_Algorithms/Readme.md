## Genetic Algorithms

### Why Genetic Algorithms?
Genetic algorithms simulate the process of natural selection which means those species who can adapt to changes in their environment are able to survive and reproduce and go to next generation.

### how do GA's work?
#### Initialization
The evolutionary process begins with initialization, wherein an initial **population** of candidate solutions is generated. There are many different methods of initializing populations, but with Genetic Algorithms the most popular method of initialization is simply to create a population of randomly initialized binary strings, **chromosomes**.The bits of the strings are called **genes**.Once the initial population has been created, the evolutionary generational cycle begins.

#### Selection
The idea of **selection** phase is to select the fittest individuals and let them pass their genes to the next generation.
Two pairs of individuals (**parents**) are selected based on their fitness scores. Individuals with high fitness have more chance to be selected for reproduction.

#### Crossover
**Crossover** is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a **crossover point** is chosen at random from within the genes.
For example, consider the crossover point to be 3 as shown below.

![Crossover point](https://miro.medium.com/max/409/1*Wi6ou9jyMHdxrF2dgczz7g.png)

**Offspring** are created by exchanging the genes of parents among themselves until the crossover point is reached.
![Exchanging genes among parents](https://miro.medium.com/max/389/1*eQxFezBtdfdLxHsvSvBNGQ.png)

The new offspring are added to the population.

#### Mutation
While crossover simply swaps pre-existing information between pairs of candidate solutions, **mutation** in Evolutionary Algorithms is typically the standard method of introducing “new” genetic material into the population. Once the child population has been created via crossover, mutation in canonical Genetic Algorithms then occurs on all children in a “bit-flip” fashion by randomly changing codons on the chromosome between 0 and 1.

![Mutation: Before and After](https://miro.medium.com/max/439/1*CGt_UhRqCjIDb7dqycmOAg.png)

>Mutation occurs to maintain diversity within the population and prevent premature convergence.  


### Advantages of GA's:
With the understanding that we have about the Genetic Algorithms, it is the best time for us to discuss various advantages and disadvantages of them. Genetic Algorithms have a numerous number of advantages and hence a reason why they are particularly very popular. Some of the most common advantages of the Genetic Algorithms are given in this section of the article, as given below:

- Genetic Algorithms do not require any derivative information (There is every possibility that there may not be any information that we can rely on based on the problem that we choose to solve with these Genetic Algorithms).
- Genetic Algorithms are faster and efficient when compared to the traditional methods of brute-force search.
- Genetic Algorithms is proven to have many parallel capabilities
- Optimizes both continuous and discrete functions and also multi-objective problems.


### Disadvantages / Limitations of GA’s:
As per the discussions above, the following are the limitations to Genetic Algorithms which are listed as below:

- Genetic Algorithms are not best suited for simpler problems where the derivative information is readily available.
- Fitness value gets evaluated on a set of generations, and this can be an expensive process for a certain number of problems using Genetic Algorithms.
- If a Genetic algorithm is not put to use in the best manner, it may not converge to an optimal solution.


### References
* [Genetic Algorithm in Artificial Intelligence](https://mindmajix.com/genetic-algorithm-in-artificial-intelligence#:~:text=Genetic%20Algorithms%20are%20faster%20and,and%20also%20multi%2Dobjective%20problems.)
* [Introduction to Genetic Algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3)
* [How does a Genetic Algorithm work?](https://www.pico.net/kb/how-does-a-genetic-algorithm-work)