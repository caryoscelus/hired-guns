======
combat
======

stats
=====

Most important stats for combat include:

* hp (TODO: decide how permanent is death)
* ap - action points
* psy (? - perhaps temporary name for some kind of energy)

general rules
=============

grid
----

Combat takes place on a grid. Currently, it's 5x4, but it's subject to change.

When combat starts, opposing sides are usually placed on left (player party) and
right (enemy) sides.

turn resolution
---------------

* sides take turns one after another
* units perform actions immediately
* unit has action points which can be spent on actions and are recharged each
  turn

ranged
------

Ranged weapons have different efficiency (both in power and aim) at different
range.

melee
-----

To go into melee, unit needs to enter same cell as enemy unit. This may activate
free 'defence' action and may also fail. When two units are on the same cell,
range attacks on any of them has a high chance of injuring the other. Most means
of ranged combat are either completely unusable or ineffective. Unit can try to
escape melee range, but that may fail if enemy pursues or activate free 'shot in
the back' attack.

? - how to implement two units on one cell:

* actually place them on one cell
  - increases visual density
  - can lead to situation when unit can only escape to another occupied cell

* 'unite' two cells
  - looks weird
  - complicates range computations


medicine
--------

Perhaps it should work similar to melee combat: on the same cell (except for
self-heal, of course).

Usefulness - ?

ideas
=====

* special modes, e.g. taking cover, suppression fire, running
* grid positions have special meaning
* ability to reserve units from combat field
