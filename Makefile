all:
	clang -Wall -Werror -Wextra -Wpedantic -o LCP LCP.c -g
tidy_objects:
	$(RM) $(OBJS)
tidy: tidy_objects
clean: tidy
	$(RM) LCP
format:
	clang-format -i -style=file *.[ch]
