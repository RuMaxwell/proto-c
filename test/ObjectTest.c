#include "../src/Object.h"

int main() {
  void* obj = new(Object);

  printf("%s\n", show(obj));

  printf("%s\n", instanceof(obj, Object) ? "true" : "false");

  return 0;
}
