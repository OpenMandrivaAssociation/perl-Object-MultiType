%define upstream_name    Object-MultiType
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl Objects as Hash, Array, Scalar, Code and Glob at the same time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module return an object that works like a Hash, Array,
Scalar, Code and Glob object at the same time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 'tr /\r//d' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Object
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401998
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-7mdv2009.0
+ Revision: 258143
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2009.0
+ Revision: 246257
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.05-4mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-4mdv2008.0
+ Revision: 86724
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-3mdv2007.0
- spec cleanup
- fix directory ownership

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdk
- rpmlint fixes

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdk
- initial Mandriva package

