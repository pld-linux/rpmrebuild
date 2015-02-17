Summary:	A tool to build rpm file from rpm database
Name:		rpmrebuild
Version:	2.11
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz
# Source0-md5:	cb762d14484795986fd909b48f1207b9
Patch0:		locales.patch
URL:		http://rpmrebuild.sourceforge.net
Requires:	bash
Requires:	cpio
Requires:	grep
Requires:	rpm >= 4.0
Requires:	rpm-build
Requires:	textutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fix for .src without shebangs
chmod a+w $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src
awk '{if (NR==1) print "#!/bin/bash\n" $0; else print $0;}' < $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src > $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src.new
mv $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src.new $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src
chmod a-w $RPM_BUILD_ROOT%{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog COPYING COPYRIGHT News Todo README
%dir %{_prefix}/lib/rpmrebuild/
%dir %{_prefix}/lib/rpmrebuild/plugins/
%dir %{_prefix}/lib/rpmrebuild/locale/
%dir %{_prefix}/lib/rpmrebuild/locale/fr
%dir %{_prefix}/lib/rpmrebuild/locale/en
%attr(755,root,root) %{_bindir}/rpmrebuild
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/nodoc.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_extract_tags.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/processing_func.src
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_rpmqf.src
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_buildroot.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/spec_func.src
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_lib.src
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/uniq.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/un_prelink.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/unset_tag.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/demo.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/set_tag.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/file2pacDep.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/demofiles.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_ghost.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_files.sh
%attr(755,root,root) %{_prefix}/lib/rpmrebuild/plugins/compat_digest.sh
%{_prefix}/lib/rpmrebuild/VERSION
%{_prefix}/lib/rpmrebuild/plugins/set_tag.plug
%{_prefix}/lib/rpmrebuild/plugins/compat_digest.plug
%{_prefix}/lib/rpmrebuild/plugins/nodoc.plug
%{_prefix}/lib/rpmrebuild/plugins/demo.plug
%{_prefix}/lib/rpmrebuild/plugins/file2pacDep.plug
%{_prefix}/lib/rpmrebuild/plugins/uniq.plug
%{_prefix}/lib/rpmrebuild/plugins/demofiles.plug
%{_prefix}/lib/rpmrebuild/plugins/un_prelink.plug
%{_prefix}/lib/rpmrebuild/plugins/unset_tag.plug
%{_prefix}/lib/rpmrebuild/locale/en/rpmrebuild.lang
%{_prefix}/lib/rpmrebuild/locale/fr/rpmrebuild.lang
%{_mandir}/fr/man1/compat_digest.plug.1rrp*
%{_mandir}/fr/man1/demo.plug.1rrp*
%{_mandir}/fr/man1/demofiles.plug.1rrp*
%{_mandir}/fr/man1/file2pacDep.plug.1rrp*
%{_mandir}/fr/man1/nodoc.plug.1rrp*
%{_mandir}/fr/man1/rpmrebuild.1*
%{_mandir}/fr/man1/rpmrebuild_plugins.1*
%{_mandir}/fr/man1/set_tag.plug.1rrp*
%{_mandir}/fr/man1/un_prelink.plug.1rrp*
%{_mandir}/fr/man1/uniq.plug.1rrp*
%{_mandir}/fr/man1/unset_tag.plug.1rrp*
%{_mandir}/man1/compat_digest.plug.1rrp*
%{_mandir}/man1/demo.plug.1rrp*
%{_mandir}/man1/demofiles.plug.1rrp*
%{_mandir}/man1/file2pacDep.plug.1rrp*
%{_mandir}/man1/nodoc.plug.1rrp*
%{_mandir}/man1/rpmrebuild.1*
%{_mandir}/man1/rpmrebuild_plugins.1*
%{_mandir}/man1/set_tag.plug.1rrp*
%{_mandir}/man1/un_prelink.plug.1rrp*
%{_mandir}/man1/uniq.plug.1rrp*
%{_mandir}/man1/unset_tag.plug.1rrp*
