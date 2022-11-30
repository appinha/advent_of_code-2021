all:
	@make -C my_solutions/aoc_framework day=$(d) part=$(p)

.PHONY: test
test:
	@make -C my_solutions/aoc_framework test day=$(d) part=$(p)

.PHONY: new
new:
	@make -C my_solutions/aoc_framework new day=$(d)

.PHONY: input
input:
	@make -C my_solutions/aoc_framework input day=$(d)