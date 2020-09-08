#ifndef _PROTO_C_OBJECT_H_
#define _PROTO_C_OBJECT_H_

#include "proto.h"

struct ObjectProto {
  __SIZE__
  __PROTO__
  __CONSTRUCTOR__
  char* (*show)(Ptr(Object) this);
  bool (*instanceof)(Ptr(Object) this, Prototype type);
}* Object;

char* show(Ptr(Object) this);

bool instanceof(Ptr(Object) this, Prototype type);

#endif
