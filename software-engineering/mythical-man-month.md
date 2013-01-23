# The Mythical Man Month

## 1. The Tar Pit

Large system programming is like a tar pit: the more you struggle, the quicker you sink.

The programmers can get trapped in the poor system implementation, and the project dies.

A programming system product must be:

1. General (for input and algorithms)
2. Thoroughly tested so it can be depended upon. This increases costs three-fold.
3. Documented so it can be used, fixed and extended.
4. Composable: it must work with other programs on the system. This increases costs three-fold.
5. Within budget.

## 2. The Mythical Dev-Month

Poor scheduling causes the demise of commercial software projects.

1. Scheduling is difficult.
2. We naively equate *effort* with *progress*.
3. Progress is poorly monitored.
4. Typical solution for late projects is to add more manpower.

Is other fields, managers will over-estimate the schedule to compensate for unforeseen issues.

In software projects, we often assume that everything will go well! But, we run into bugs, unforeseen implementation complications.

It is a fallacy to measure completion time of software projects in dev-months. The cost will increase proportional to the dev-months, but the rate of progress will not (due to increasing communication overhead).

Brook's rule of thumb for estimating the completion time of software projects:

* 1/3 time for planning
* 1/6 time for coding
* 1/4 time for component tests
* 1/4 time for system test with all components in hand

Underestimating the schedule can become very dangerous for projects at the end because:

* project is already fully-funded and has a large number of developers
* the customer is ready to receive the product
* delays are going to increase the cost dramatically and reduce customers' confidence

Another problem is that managers will estimate the schedule according to the customer's desired dates, rather than being realistic.

Brook's Law: **Adding manpower to a late software project makes it later.**

## 3. The Surgical Team

Many managers believe having a small number of good programmers is better than having a large number of mediocre programmers.

However, with fewer people, implementing large system programs becomes difficult.

Large projects must be broken into smaller subtasks, and each subtask needs to have a dedicated team.

## 4. Conceptual Integrity

Conceptual integrity is the most important aspect of large system programming.

It is better to have one good idea and carry it through the project than having several uncoordinated good ideas.

It is important that all aspects of the system follow the same philosophy and conceptual integrity. By doing so, the system provides a lighter conceptual load for users.
