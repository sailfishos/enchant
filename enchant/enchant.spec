%define name enchant
%define version 1.5.0
%define release 1

Summary: An Enchanting Spell Checking Library

Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Libraries
License: LGPL

Source: ftp://ftp.gnome.org/pub/GNOME/unstable/sources/libenchant/%{name}-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root
URL: http://www.abisource.com/

Requires: glib2 >= 2.0.0
BuildRequires: glib2-devel >= 2.0.0

%description
A library that wraps other spell checking backends.

%package devel
Summary: Support files necessary to compile applications with libenchant.
Group: Development/Libraries
Requires: enchant

%description devel
Libraries, headers, and support files necessary to compile applications using libenchant.

%prep

%setup

%build
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

if [ ! -f configure ]; then
CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%{_prefix}
fi
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} \
%{?_without_ispell:--disable-ispell} \
%{?_without_myspell:--disable-myspell} \
%{?_without_aspell:--disable-aspell} \
%{?_with_uspell:--enable-uspell}


if [ "$SMP" != "" ]; then
  (%__make "MAKE=%__make -k -j $SMP"; exit 0)
  %__make
else
%__make
fi

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%__make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT/%{_libdir} -name \*.la -exec rm -f \{\} \;

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.LIB README
%attr(755,root,root)%{_bindir}/*
%{_libdir}/lib*.so*
%{_prefix}/man/man1/enchant.1.gz
%{!?_without_ispell:%{_libdir}/enchant/*ispell.so*}
%{!?_without_myspell:%{_libdir}/enchant/*myspell.so*}
%{!?_without_aspell:%{_libdir}/enchant/*aspell.so*}
%{?_with_uspell:%{_libdir}/enchant/*uspell.so*}

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{!?_without_ispell:%{_libdir}/enchant/*ispell.a}
%{!?_without_myspell:%{_libdir}/enchant/*myspell.a}
%{!?_without_aspell:%{_libdir}/enchant/*aspell.a}
%{?_with_uspell:%{_libdir}/enchant/*uspell.a}
%{_libdir}/pkgconfig/enchant.pc
%{_includedir}/enchant/*

%clean
%__rm -r $RPM_BUILD_ROOT

%changelog
* Sun Aug 24 2003 Rui Miguel Seabra <rms@1407.org>
- update spec to current stat of affairs
- building from source rpm is now aware of --with and --without flags:
- --without aspell --without ispell --without myspell --with uspell

* Wed Jul 16 2003 Rui Miguel Seabra <rms@1407.org>
- take advantage of environment rpm macros

* Sun Jul 13 2003 Dom Lachowicz <cinamod@hotmail.com>
- Initial version
