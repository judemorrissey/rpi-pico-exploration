cmake_minimum_required(VERSION 3.13)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(blink C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

# C version
add_executable(blink_c blink.c)
target_link_libraries(blink_c pico_stdlib)
pico_add_extra_outputs(blink_c)

# C++ version
add_executable(blink_cpp blink.cpp)
target_link_libraries(blink_cpp pico_stdlib)
pico_add_extra_outputs(blink_cpp)
