%define upstream_name    Object-MultiType
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl Objects as Hash, Array, Scalar, Code and Glob at the same time
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module return an object that works like a Hash, Array,
Scalar, Code and Glob object at the same time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 'tr /\r//d' Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Object
%{_mandir}/*/*
