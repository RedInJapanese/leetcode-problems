all:
	gcc -Wall -Werror -Wextra -Wpedantic -o k kth.c -g
tidy_objects:
	$(RM) $(OBJS)
tidy: tidy_objects
clean: tidy
	$(RM) LCP
format:
	clang-format -i -style=file *.[ch]
