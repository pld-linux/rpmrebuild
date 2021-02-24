Summary:	A tool to build rpm file from rpm database
Name:		rpmrebuild
Version:	2.16
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz
# Source0-md5:	f924f30767dd87ab321e887fcea1cc57
Patch0:		locales.patch
Patch1:		%{name}-spec-arch.patch
URL:		http://rpmrebuild.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	cpio
Requires:	grep
Requires:	rpm >= 1:4.0
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
%patch1 -p1

# remove non-UTF8 man files
%{__rm} -r locale/fr_FR
%{__rm} -r man/fr_FR
%{__rm} -r plugins/man/fr_FR

# move UTF8 man files to the correct location
%{__mv} locale/{fr_FR.UTF-8,fr}
%{__mv} man/{fr_FR.UTF-8,fr}
%{__mv} plugins/man/{fr_FR.UTF-8,fr}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+(bash|sh)(\s|$),#!/bin/bash\1,' \
      plugins/compat_digest.sh \
      plugins/demo.sh \
      plugins/demofiles.sh \
      plugins/file2pacDep.sh \
      plugins/nodoc.sh \
      plugins/set_tag.sh \
      plugins/un_prelink.sh \
      plugins/uniq.sh \
      plugins/unset_tag.sh \
      processing_func.src \
      rpmrebuild \
      rpmrebuild.sh \
      rpmrebuild_buildroot.sh \
      rpmrebuild_extract_tags.sh \
      rpmrebuild_files.sh \
      rpmrebuild_ghost.sh \
      rpmrebuild_lib.src \
      rpmrebuild_parser.src \
      rpmrebuild_rpmqf.src \
      spec_func.src

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
%dir %{_appdir}
%{_appdir}/Version
%{_appdir}/optional_tags.cfg
%attr(755,root,root) %{_appdir}/*.sh
%attr(755,root,root) %{_appdir}/*.src
%dir %{_appdir}/plugins
%{_appdir}/plugins/*.plug
%attr(755,root,root) %{_appdir}/plugins/*.sh
%dir %{_appdir}/locale
%dir %{_appdir}/locale/en
%{_appdir}/locale/en/rpmrebuild.lang
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(fr) %dir %{_appdir}/locale/fr
%lang(fr) %{_appdir}/locale/fr/rpmrebuild.lang
