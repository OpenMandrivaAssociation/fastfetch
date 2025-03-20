Name:           fastfetch
Version:        2.39.0
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
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libnm)
# In contrib repo, so lets disable it for now
#BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(yyjson)

Recommends:     %{_lib}drm2
Recommends:     elfutils
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
Recommends:     hwdata

# Neofetch is not in development anymore, no new commit from years and now archived repo. So lets replace it by fastfetch.
Obsoletes:     neofetch
 
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

%package zsh-completion
Summary: Zsh completion files for %{name}
Requires: zsh
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description zsh-completion
%{summary}

%package fish-completion
Summary: Fish completion files for %{name}
# as Fish is currently in contrib repository, let's make only soft dependency on it.
Recommends: fish
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description fish-completion
%{summary}
 
%prep
%autosetup -p1

%build
%cmake
%make_build
install -Dm644 completions/fish %{buildroot}/usr/share/fish/completions/fastfetch.fish

%install
%make_install -C build

ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/neofetch
 
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/flashfetch
%{_bindir}/neofetch
%{_datadir}/%{name}/
%{_mandir}/man1/fastfetch.1.*
 
%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/fastfetch.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_fastfetch
