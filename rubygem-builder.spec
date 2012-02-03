%define gem_name builder

Name:		rubygem-%{gem_name}
Summary: 	Builders for MarkUp
Version: 	2.1.2
Release: 	9%{?dist}
Group: 		Development/Languages
License: 	MIT
URL: 		http://onestepback.org
# Source pulled from http://www.freshports.org/devel/rubygem-builder/, there's more listed
Source0:	http://rubyforge.rubyuser.de/%{gem_name}/%{gem_name}-%{version}.gem
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: 	rubygems
BuildRequires: rubygems-devel
BuildArch: 	noarch
Provides: 	rubygem(%{gem_name}) = %{version}

%description
Builder provides a number of builder objects that make creating structured
data simple to do.  Currently the following builder objects are supported:  *
XML Markup * XML Events

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0} || \
            echo 'Workaround FTBFS rhbz#712927'

for file in `find %{buildroot}/%{gem_instdir} -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!\"`" ] && chmod +x $file
done

# Convert README to utf8
strings %{buildroot}/%{gem_instdir}/README > %{buildroot}/%{gem_instdir}/README.strings

mv -f %{buildroot}/%{gem_instdir}/README.strings %{buildroot}/%{gem_instdir}/README

# Remove zero-length file
rm -rf %{buildroot}/%{gem_instdir}/%{gem_name}-%{version}.gem

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README
%doc %{gem_instdir}/doc/releases/builder-1.2.4.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.0.0.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.1.1.rdoc
%{gem_cache}
%{gem_spec}


%changelog
* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.2-9
- Fixed license.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.2-8
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.2-6
- Fix FTBFS rhbz#712927.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 2.1.2-2
- Rebuild for review

* Sun Jul 13 2008 root <root@oss1-repo.usersys.redhat.com> - 2.1.2-1
- Initial package
