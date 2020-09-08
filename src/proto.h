#ifndef _PROTO_C_PROTO_H_
#define _PROTO_C_PROTO_H_

#include <malloc.h>
#include <stdarg.h>

#define Ptr(type) void*
#define Prototype void*

// Size of an instantiated object of the type. 0 if the type is not instantiatable.
#define __SIZE__  size_t __size__;
// __proto__ in Prototype stores the type this type inherits.
#define __PROTO__ Prototype __proto__;
// Every type has a constructor to instantiate objects. constructor = NULL if the type is not instantiatable.
#define __CONSTRUCTOR__ Ptr(any) (*__constr__)(Prototype proto, ...);
// Type-specific fields
#define FIELDS
// Type-specific methods
#define METHODS

#define new(proto, ...) proto->__constr__(proto, ##__VA_ARGS__)

#define bool int
#define false ((bool)0)
#define true (!false)

void* owner(size_t size);

#endif
