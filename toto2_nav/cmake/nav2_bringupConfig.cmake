# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_toto2_navigation_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED toto2_navigation_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(toto2_navigation_FOUND FALSE)
  elseif(NOT toto2_navigation_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(toto2_navigation_FOUND FALSE)
  endif()
  return()
endif()
set(_toto2_navigation_CONFIG_INCLUDED TRUE)

# output package information
if(NOT toto2_navigation_FIND_QUIETLY)
  message(STATUS "Found toto2_navigation: 1.1.6 (${toto2_navigation_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'toto2_navigation' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${toto2_navigation_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(toto2_navigation_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${toto2_navigation_DIR}/${_extra}")
endforeach()
