#include "proto.h"

void* owner(size_t size) {
  return calloc(1, size);
}
