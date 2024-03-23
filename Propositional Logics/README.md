## Propositional Logic
Logic of propositions/statements about the world.
Propositional logic (PL) is the simplest form of logic where all the statements are made by propositions. A proposition is a declarative statement which is either true or false. It is a technique of knowledge representation in logical and mathematical form.

## Propositional Symbols
They represent sentences or facts about the world

## Logic Connectives
* ~ not
* v or
* ^ and
* -> implication
* <-> biconditional

### NOT

|  P  |  ~P  |
|-----|------|
|  False  |  True  |
|  True  |  False  |

### AND

|  P  |  Q  |  P^Q  |
|-----|-----|-------|
|  True  |  True  |  True  |
|  True  |  False  |  False  |
|  False  |  True  |  False  |
|  False  |  False  |  False  |

### OR

|  P  |  Q  |  PVQ  |
|-----|-----|-------|
|  True  |  True  |  True  |
|  True  |  False  |  True  |
|  False  |  True  |  True  |
|  False  |  False  |  False  |

### IMPLICATION
If P is true, then Q is true.

|  P  |  Q  |  P->Q  |
|-----|-----|-------|
|  True  |  True  |  True  |
|  True  |  False  |  False  |
|  False  |  True  |  True  |
|  False  |  False  |  True  |

### BICONDITIONAL
Q is true if and only if P is true.

|  P  |  Q  |  P<->Q  |
|-----|-----|-------|
|  True  |  True  |  True  |
|  True  |  False  |  False  |
|  False  |  True  |  False  |
|  False  |  False  |  True  |

## Knowledge Engineering
It can be defined as the process of trying to take a problem and figure what propositional system to use in order to encode/represent the problem logically.
