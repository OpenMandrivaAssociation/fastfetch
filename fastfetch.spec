Name:           fastfetch
Version:        2.2.1
Release:        1%{?dist}
Summary:        Like neofetch, but much faster because written in c
 
License:        MIT
URL:            https://github.com/fastfetch-cli/fastfetch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pciutils-devel
BuildRequires:  wayland-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  dconf-devel
BuildRequires:  dbus-devel
BuildRequires:  sqlite-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  zlib-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  xfconf-devel
BuildRequires:  glib2-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  rpm-devel
# not available on s390x
%if "%{_arch}" != "s390x"
BuildRequires:  libddcutil-devel
%endif
# vulkan-loader not available in el8 on some arches
%if 0%{?rhel} == 8
  %if "%{_arch}" != "s390x" && "%{_arch}" != "ppc64le"
BuildRequires:  vulkan-loader-devel
  %endif
%else
BuildRequires:  vulkan-loader-devel
%endif
BuildRequires:  chafa-devel
 
Recommends:     pciutils
Recommends:     libxcb
Recommends:     libXrandr
Recommends:     dconf
Recommends:     sqlite
Recommends:     zlib
Recommends:     libglvnd-glx
Recommends:     ImageMagick
Recommends:     glib2
Recommends:     ocl-icd
Recommends:     chafa
Recommends:     ddcutil
 
%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.
 
 
%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
 
%description bash-completion
%{summary}
 
 
%prep
%autosetup -p1
 
 
%build
%cmake -D BUILD_TESTS=ON
%cmake_build
 
%check
%ctest
 
%install
%cmake_install
 
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/flashfetch
%{_datadir}/%{name}/
 
%files bash-completion
%{_datadir}/bash-completion/completions/%{name}
