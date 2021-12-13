<h1 align="center">
	🌟 Advent of Code 2021 🎄
</h1>

<p align="center">
	<i>My solutions for <b>Advent of Code 2021</b>.</i>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/appinha/adventofcode_2021?color=blueviolet" />
	<img alt="Number of lines of code" src="https://img.shields.io/tokei/lines/github/appinha/adventofcode_2021?color=blueviolet" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/appinha/adventofcode_2021?color=blue" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/appinha/adventofcode_2021?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/appinha/adventofcode_2021?color=brightgreen" />
</p>

<h3 align="center">
	<a href="#%EF%B8%8F-about">About</a>
	<span> · </span>
	<a href="#-what-is-advent-of-code">What is <i>Advent of Code</i>?</a>
	<span> · </span>
	<a href="#-contents">Contents</a>
	<span> · </span>
	<a href="#%EF%B8%8F-usage">Usage</a>
	<span> · </span>
	<a href="#%EF%B8%8F-table-of-puzzles">Table of puzzles</a>
</h3>

---

[![Day 01](https://badgen.net/badge/01/%E2%98%85%E2%98%85/yellow)](my_solutions/day01)
[![Day 02](https://badgen.net/badge/02/%E2%98%85%E2%98%85/yellow)](my_solutions/day02)
[![Day 03](https://badgen.net/badge/03/%E2%98%85%E2%98%85/yellow)](my_solutions/day03)
[![Day 04](https://badgen.net/badge/04/%E2%98%85%E2%98%85/yellow)](my_solutions/day04)
[![Day 05](https://badgen.net/badge/05/%E2%98%85%E2%98%85/yellow)](my_solutions/day05)
[![Day 06](https://badgen.net/badge/06/%E2%98%85%E2%98%85/yellow)](my_solutions/day06)
[![Day 07](https://badgen.net/badge/07/%E2%98%85%E2%98%85/yellow)](my_solutions/day07)
[![Day 08](https://badgen.net/badge/08/%E2%98%85%E2%98%85/yellow)](my_solutions/day08)
[![Day 09](https://badgen.net/badge/09/%E2%98%85%E2%98%85/yellow)](my_solutions/day09)
[![Day 10](https://badgen.net/badge/10/%E2%98%85%E2%98%85/yellow)](my_solutions/day10)
[![Day 11](https://badgen.net/badge/11/%E2%98%85%E2%98%85/yellow)](my_solutions/day11)
[![Day 12](https://badgen.net/badge/12/%E2%98%85%E2%98%85/yellow)](my_solutions/day12)
[![Day 13](https://badgen.net/badge/13/%E2%98%85%E2%98%85/yellow)](my_solutions/day13)

(TODO: add final picture of AoC calendar)

## 🗣️ About

(TODO: impressions about this year's event)

## 🌟 What is *Advent of Code*?

	🚀 TLDR: an online event where a two-part programming puzzle is released each day from Dec 1st to 25th.

[Advent of Code](http://adventofcode.com) is an online event created by [Eric Wastl](http://was.tl/). In his words:

> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

*Source: https://adventofcode.com/about*

## 📑 Contents

My solutions for the puzzles are available in the folder [📁 my_solutions](my_solutions) and are organized into subfolders for each day of the event.

In this folder's root, the following files can be found:

* `puzzle_solver.py` - main framework developed to streamline coding.
* `solve_puzzles.py` - script for running the puzzle solving codes.
* `Makefile` - used for starting the execution of the above script.

Inside each subfolder, the following files can be found:

* `input_test.txt` - text file containing input from tests given in the puzzle.
* `input.txt` - text file containing my personal input for the puzzle.
* `main.py` - Python code for solving the puzzle.

## 🛠️ Usage

**Solve puzzle for a certain day:**

```
make day=01
```

**Solve puzzle for a certain day and part:**

```
make day=08 part=1
```

```
make day=08 part=2
```

**Solve puzzle for testing input:**

```
make test day=12
```

```
make test day=12 part=1
```

**Create a new day folder from template:**

```
make new day=02
```

## 🗓️ Table of puzzles

| DAY							| PUZZLE TITLE	| PUZZLE SUMMARY
| :-:							| :-						| :-
| [📁 01](my_solutions/day_01)	| **Sonar Sweep**		| 📃 **Input:** the sonar sweep report - a list of measurements of the sea floor depth (a list of integers).<br />⭐ **Part One:** count the number of times a depth measurement increases from the previous measurement. <br />⭐ **Part Two:** count the number of times the sum of three-measurement windows increases from the previous sum.
| [📁 02](my_solutions/day_02)	| **Dive!**		| 📃 **Input:** a list of commands - a tuple of a direction and an integer number.<br />⭐ **Part One:** follow the planned course (list of commands) to calculate the final horizontal position and depth; multiply them. <br />⭐ **Part Two:** same as before, but with a new interpretation  of the commands.
| [📁 03](my_solutions/day_03)	| **Binary Diagnostic**		| 📃 **Input:** the submarine's diagnostic report - a list of binary numbers.<br />⭐ **Part One:** use the binary numbers to calculate the gamma rate and epsilon rate, then multiply them together to find the power consumption of the submarine. <br />⭐ **Part Two:** use the binary numbers to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together to find the life support rating of the submarine.
| [📁 04](my_solutions/day_04)	| **Giant Squid**		| 📃 **Input:** a random order in which to draw numbers and a random set of bingo boards.<br />⭐ **Part One:** figure out which board will win first, then calculate the final score for that board. <br />⭐ **Part Two:** figure out which board will win last, then calculate the final score for that board.
| [📁 05](my_solutions/day_05)	| **Hydrothermal Venture**		| 📃 **Input:** a list of nearby lines of vents - a list of 2D coordinate pairs.<br />⭐ **Part One:** only consider horizontal and vertical lines and find how many points at least two lines overlap. <br />⭐ **Part Two:** same as before, but including diagonals.
| [📁 06](my_solutions/day_06)	| **Lanternfish**		| 📃 **Input:** a list of the ages of several hundred nearby lanternfish - a comma separated list of integers.<br />⭐ **Part One:** simulate lanternfish spawning to find how many lanternfish would there be after 80 days. <br />⭐ **Part Two:** same as before, but for 256 days.
| [📁 07](my_solutions/day_07)	| **The Treachery of Whales**		| 📃 **Input:** a list of the horizontal position of each crab - a comma separated list of integers.<br />⭐ **Part One:** find the least fuel possible used to align the crabs position. <br />⭐ **Part Two:** same as before, but with a new fuel cost rate.
| [📁 08](my_solutions/day_08)	| **Seven Segment Search**		| 📃 **Input:** a list of signal patterns and output values - a list of lowercase strings.<br />⭐ **Part One:** find how many times do digits 1, 4, 7, or 8 appear. <br />⭐ **Part Two:** decode the output values and add them all up.
| [📁 09](my_solutions/day_09)	| **Smoke Basin**		| 📃 **Input:** a heightmap of the floor of the nearby caves.<br />⭐ **Part One:** find the sum of the risk levels of all low points on the heightmap. <br />⭐ **Part Two:** find the product of the sizes of the three largest basins.
| [📁 10](my_solutions/day_10)	| **Syntax Scoring**		| 📃 **Input:** the navigation subsystem - a list of brackets and parenthesis.<br />⭐ **Part One:** find the total syntax error score of the navigation subsystem. <br />⭐ **Part Two:** find the middle score of the incomplete lines in the navigation subsystem.
| [📁 11](my_solutions/day_11)	| **Dumbo Octopus**		| 📃 **Input:** a grid of octopus' energy levels - a grid of single digit integers.<br />⭐ **Part One:** find the total flashes after simulating 100 steps. <br />⭐ **Part Two:** find the first step during which all octopuses flash.
| [📁 12](my_solutions/day_12)	| **Passage Pathing**		| 📃 **Input:** a map of the remaining caves - a list of connections between pairs of caves.<br />⭐ **Part One:** find how many paths through this cave system are there that visit small caves at most once. <br />⭐ **Part Two:** same as before, but now allowing to visit a single small cave twice.
| [📁 13](my_solutions/day_13)	| **Transparent Origami**		| 📃 **Input:** a list of coordinates of the dots marked in the transparent paper and a list of folding instructions.<br />⭐ **Part One:** find how many dots are visible after completing just the first fold instruction on the transparent paper. <br />⭐ **Part Two:** finish folding the transparent paper according to the instructions to find the eight capital letters code to activate the infrared thermal imaging camera system.
<!--
| [📁 14](my_solutions/day_14)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 15](my_solutions/day_15)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 16](my_solutions/day_16)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 17](my_solutions/day_17)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 18](my_solutions/day_18)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 19](my_solutions/day_19)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 20](my_solutions/day_20)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 21](my_solutions/day_21)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 22](my_solutions/day_22)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 23](my_solutions/day_23)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 24](my_solutions/day_24)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 25](my_solutions/day_25)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
 -->