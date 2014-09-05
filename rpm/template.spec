Name:           ros-hydro-rosbag-image-compressor
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS rosbag_image_compressor package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python-pillow
Requires:       python-pillow-qt
Requires:       ros-hydro-rosbag
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-rosbag
BuildRequires:  ros-hydro-sensor-msgs

%description
The rosbag_image_compressor package. This package has a script to compress and
decompress images inside a bag file.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Sep 04 2014 Tully Foote <tfoote@osrfoundation.org> - 0.1.3-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Tully Foote <tfoote@osrfoundation.org> - 0.1.1-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Tully Foote <tfoote@osrfoundation.org> - 0.1.2-0
- Autogenerated by Bloom

