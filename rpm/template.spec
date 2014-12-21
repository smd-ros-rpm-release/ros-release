Name:           ros-indigo-ros
Version:        1.11.5
Release:        0%{?dist}
Summary:        ROS ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-catkin
Requires:       ros-indigo-mk
Requires:       ros-indigo-rosbash
Requires:       ros-indigo-rosboost-cfg
Requires:       ros-indigo-rosbuild
Requires:       ros-indigo-rosclean
Requires:       ros-indigo-roscreate
Requires:       ros-indigo-roslang
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rosmake
Requires:       ros-indigo-rosunit
BuildRequires:  ros-indigo-catkin

%description
ROS packaging system

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

