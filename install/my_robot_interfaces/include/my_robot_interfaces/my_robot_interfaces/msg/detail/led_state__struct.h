// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE__STRUCT_H_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'led_state'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/LedState in the package my_robot_interfaces.
typedef struct my_robot_interfaces__msg__LedState
{
  rosidl_runtime_c__int64__Sequence led_state;
} my_robot_interfaces__msg__LedState;

// Struct for a sequence of my_robot_interfaces__msg__LedState.
typedef struct my_robot_interfaces__msg__LedState__Sequence
{
  my_robot_interfaces__msg__LedState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__msg__LedState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE__STRUCT_H_
