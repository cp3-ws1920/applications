project(applications LANGUAGES CXX)
cmake_minimum_required(VERSION 3.0)

add_subdirectory(include/triangulator)

add_executable(triangulate_poly triangulate_poly.cpp)
target_link_libraries(triangulate_poly PRIVATE triangulator)
target_include_directories(triangulate_poly PUBLIC include/triangulator)