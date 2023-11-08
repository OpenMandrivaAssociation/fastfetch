Name:           fastfetch
Version:        2.2.3
Release:        1
Summary:        Like neofetch, but much faster because written in c
Group:          Shells
License:        MIT
URL:            https://github.com/fastfetch-cli/fastfetch
Source0:        https://github.com/fastfetch-cli/fastfetch/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(osmesa)
# In contrib repo, so lets disable it for now
#BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(rpm)
#BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(vulkan)
#BuildRequires:  pkgconfig(chafa)
 
Recommends:     pciutils
Recommends:     %{_lib}xcb1
Recommends:     lib64xrandr2
Recommends:     dconf
Recommends:     sqlite-tools
Recommends:     lib64z1
Recommends:     lib64GLX0
Recommends:     imagemagick
Recommends:     glib2
Recommends:     lib64opencl1
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
%cmake
%make_build

%install
%make_install -C build
 
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/flashfetch
%{_datadir}/%{name}/
 
%files bash-completion
%{_datadir}/bash-completion/completions/%{name}
