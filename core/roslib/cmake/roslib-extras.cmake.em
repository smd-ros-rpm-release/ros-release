# generated from ros/core/roslib/cmake/roslib-extras.cmake.em

@[if DEVELSPACE]@
# set path to gendeps executable in develspace
set(gendeps_exe @(CMAKE_CURRENT_SOURCE_DIR)/scripts/gendeps)
@[else]@
# set path to gendeps executable in installspace
set(gendeps_exe @(CMAKE_INSTALL_PREFIX)/lib/roslib/gendeps)
@[end if]@
