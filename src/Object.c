#include "Object.h"

static Ptr(Object) __constr__(Prototype object, ...) {
  return owner(1UL);
}

struct ObjectProto _Object = {
  .__size__ = 1UL,
  .__proto__ = NULL,
  .__constr__ = __constr__,
  .show = show,
  .instanceof = instanceof
};

struct ObjectProto* Object = &_Object;

char* show(Ptr(Object) this) {
  return "Object";
}

bool instanceof(Ptr(Object) this, Prototype type) {
  return type == Object;
}
