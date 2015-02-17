# TODO
# - broken because rpm5 still does not support BuildArch: %{_target_cpu} on top level package (rpm4 works fine)
#   http://comments.gmane.org/gmane.comp.package-management.rpm.devel/2681 (reported in 16 Jun 2008)
Summary:	A tool to build rpm file from rpm database
Name:		rpmrebuild
Version:	2.11
Release:	0.1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz
# Source0-md5:	cb762d14484795986fd909b48f1207b9
Patch0:		locales.patch
URL:		http://rpmrebuild.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	cpio
Requires:	grep
Requires:	rpm >= 4.0
Requires:	rpm-build
Requires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}

%description
A tool to build an RPM file from a package that has already been
installed.

%prep
%setup -qc
%patch0 -p1

# remove non-UTF8 man files
rm -rf locale/fr_FR
rm -rf man/fr_FR
rm -rf plugins/man/fr_FR

# move UTF8 man files to the correct location
mv locale/{fr_FR.UTF-8,fr}
mv man/{fr_FR.UTF-8,fr}
mv plugins/man/{fr_FR.UTF-8,fr}

# fix for .src without shebangs
%{__sed} -i -e '1i#!/bin/bash' rpmrebuild_parser.src

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog COPYING COPYRIGHT News Todo README
%attr(755,root,root) %{_bindir}/rpmrebuild
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%dir %{_appdir}
%{_appdir}/VERSION
%attr(755,root,root) %{_appdir}/*.sh
%attr(755,root,root) %{_appdir}/*.src
%dir %{_appdir}/plugins
%{_appdir}/plugins/*.plug
%attr(755,root,root) %{_appdir}/plugins/*.sh
%dir %{_appdir}/locale
%dir %{_appdir}/locale/en
%{_appdir}/locale/en/rpmrebuild.lang
%lang(fr) %dir %{_appdir}/locale/fr
%lang(fr) %{_appdir}/locale/fr/rpmrebuild.lang
