# 
# Do not Edit! Generated by:
# spectacle version 0.15
# 
# >> macros
# << macros

Name:       enchant
Summary:    An Enchanting Spell Checking Library
Version:    1.5.0
Release:    3
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.abisource.com/
Source0:    http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
Source100:  enchant.yaml
Patch0:     enchant-1.5.0-abi12160.searchdirs.patch
Patch1:     enchant-1.5.0-abi12173.leaks.patch
Patch2:     enchant-1.5.0-abi12174.fixbadmatch.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  automake
BuildRequires:  libtool

%description
A library that wraps other spell checking backends.


%package aspell
Summary:    Integration with aspell for libenchant
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description aspell
Libraries necessary to integrate applications using libenchant with aspell

%package devel
Summary:    Support files necessary to compile applications with libenchant
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Libraries, headers, and support files necessary to compile applications
using libenchant.



%prep
%setup -q -n %{name}-%{version}/enchant

# enchant-1.5.0-abi12160.searchdirs.patch
%patch0 -p1
# enchant-1.5.0-abi12173.leaks.patch
%patch1 -p1
# enchant-1.5.0-abi12174.fixbadmatch.patch
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --enable-myspell \
    --with-myspell-dir=/usr/share/myspell \
    --disable-ispell \
    --disable-hspell \
    --disable-zemberek

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig








%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING.LIB README
%{_bindir}/*
%{_libdir}/lib*.so.*
%dir %{_libdir}/enchant
%{_libdir}/enchant/lib*myspell.so*
%{_mandir}/man1/enchant.1.gz
%{_datadir}/enchant
# << files


%files aspell
%defattr(-,root,root,-)
# >> files aspell
%{_libdir}/enchant/lib*aspell.so*
# << files aspell

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/enchant.pc
%{_includedir}/enchant
# << files devel

