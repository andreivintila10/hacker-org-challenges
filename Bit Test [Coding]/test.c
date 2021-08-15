#include <stdio.h>
#include <stdbool.h>


char* testIt(int x) {
  bool eval = (x & (x - 1)) == 0;
  if (eval == true)
  	return "YES";
  else
  	return "NO";
}


int main() {
  for (int index = 0; index < 256; index++)
  	printf("%d\t%s\n", index, testIt(index));

  return 0;
}
