Name:           ros-indigo-spin-hokuyo
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS spin_hokuyo package

Group:          Development/Libraries
License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-dynamixel-driver
Requires:       ros-indigo-dynamixel-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamixel-controllers
BuildRequires:  ros-indigo-dynamixel-driver
BuildRequires:  ros-indigo-dynamixel-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-hokuyo-node
BuildRequires:  ros-indigo-laser-assembler
BuildRequires:  ros-indigo-laser-geometry
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
This package enables a 2D Hokuyo laser, connected to a Dynamixel servo motor, to
produce a 3D point cloud that can be visualized in rviz and used to make an
octomap.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Jul 21 2017 Sarah Bertussi <sbertuss@stevens.edu> - 1.0.0-0
- Autogenerated by Bloom

