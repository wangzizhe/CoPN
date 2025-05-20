---
layout: default
title: Literature
nav_order: 4
---

# Literature

## I. Classical Petri Nets

[Petri, C. A. (1962). Kommunikation mit automaten](https://edoc.sub.uni-hamburg.de/informatik/volltexte/2011/160)

## II. Extensions to Classical Petri Nets

### Predicate/Transition Nets (PrT-Nets)

- Transitions are guarded by predicates (boolean conditions)
- Tokens carry data (e.g., integers, strings)

[Genrich, H., & Lautenbach, K. (1979). The analysis of distributed systems by means of predicate/transition-nets. *Semantics of Concurrent Computation*, 123-146](https://link.springer.com/chapter/10.1007/BFb0022467)

[Genrich, H. J. (1987). Predicate/transition nets. In *Petri Nets: Central Models and Their Properties: Advances in Petri Nets 1986, Part I Proceedings of an Advanced Course Bad Honnef, 8.–19. September 1986* (pp. 207-247). Springer Berlin Heidelberg](https://link.springer.com/chapter/10.1007/978-3-540-47919-2_9)

### Colored Petri Nets (CPN)

- Tokens are typed ("colored") to model heterogeneous states
- Transitions fire only when guards (conditions) are met

[Jensen, K. (1981). Coloured Petri nets and the invariant-method. *Theoretical computer science*, *14*(3), 317-336](https://www.sciencedirect.com/science/article/pii/0304397581900499)

[Jensen, K. (1997). *Coloured petri nets. Basic concepts, analysis methods and practical use*. Berlin: Springer](https://link.springer.com/book/10.1007/978-3-642-60794-3)

### Guards/Conditions

**PrT-Nets and CPN** introduced the concept of guards, establishing a foundation for modeling conditional behavior.

### Inhibitor Arc

* Arcs that *prevent* a transition firing if a place has tokens

[Peterson, J. L. (1981). *Petri net theory and the modeling of systems*. Prentice Hall PTR](https://dl.icdst.org/pdfs/files3/2bf95f7fde49a09814231bbcbe592526.pdf) (Section 7.2, p. 195)

[MURATA, T. (1989). Petri nets: properties, analysis and applications. *Proceedings of the IEEE*, *77*(4), 541-580](https://ieeexplore.ieee.org/abstract/document/24143) (Section II.F, p. 546)

### Read (Test) Arc

* Arcs that *test* for presence (without consuming)

[Montanari, U., & Rossi, F. (1995). Contextual nets. *Acta Informatica*, *32*, 545-596](https://link.springer.com/article/10.1007/BF01178907) (Section 2, p. 549)

## III Context-Aware Petri Nets

### Contextual Petri Nets

* Extends classical Petri Nets with **context arcs**  that check token presence without consuming them

[Baldan, P., Corradini, A., & Montanari, U. (2001). Contextual Petri nets, asymmetric event structures, and processes. *Information and Computation*, *171*(1), 1-49](https://www.sciencedirect.com/science/article/pii/S0890540101930603)

### Feature Petri Nets

* Integrates **feature modeling** into Petri Nets to model **software product lines** by allowing configuration-specific behavior based on **enabled/disabled features**

[Muschevici, R., Clarke, D., & Proenca, J. (2010, September). Feature petri nets. In *Proceedings of the 14th international software product line conference (SPLC 2010)* (Vol. 2, pp. 99-106). Lancaster University; Lancaster, United Kingdom](https://lirias.kuleuven.be/retrieve/128498)

### Context Petri Nets

* A high-level extension of Petri Nets explicitly designed to **model and adapt to changing context**

[Cardozo, N., González, S., Mens, K., & D'Hondt, T. (2012). Context petri nets: Definition and manipulation](https://soft.vub.ac.be/~ncardozo/docs/papers/2012/cardozo12pnse.pdf)

## IV. Other Petri Nets Extensions

### Timed Petri Nets

* **Time delays** are added to **transitions** (or sometimes tokens)

[Ramchandani, C. (1974). Analysis of asynchronous concurrent systems by timed Petri nets](https://dspace.mit.edu/handle/1721.1/149425)

### Stochastic Petri Nets

*  **Firing times** become **random variables**, often with **exponential distributions**

[Molloy. (1982). Performance analysis using stochastic Petri nets. *IEEE Transactions on computers*, *100*(9), 913-917](https://ieeexplore.ieee.org/abstract/document/1676110)

### Continuous/Hybrid Petri Nets

* **Token counts** and **transition flows** are **real-valued**, not just integer

[Alla, H., & David, R. (1998). Continuous and hybrid Petri nets. *Journal of Circuits, Systems, and Computers*, *8*(01), 159-188](https://www.worldscientific.com/doi/abs/10.1142/s0218126698000079)

[David, R., & Alla, H. (2005). *Discrete, continuous, and hybrid Petri nets* (Vol. 1). Berlin: Springer](https://link.springer.com/book/10.1007/b138130)