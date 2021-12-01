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
| [📁 01](my_solutions/day_01)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
<!--
| [📁 02](my_solutions/day_02)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 03](my_solutions/day_03)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 04](my_solutions/day_04)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 05](my_solutions/day_05)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 06](my_solutions/day_06)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 07](my_solutions/day_07)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 08](my_solutions/day_08)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 09](my_solutions/day_09)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 10](my_solutions/day_10)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 11](my_solutions/day_11)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 12](my_solutions/day_12)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 13](my_solutions/day_13)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
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