%define module  Object-MultiType
%define name	perl-%{module}
%define version 0.05
%define release %mkrel 7

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Perl Objects as Hash, Array, Scalar, Code and Glob at the same time
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Object/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module return an object that works like a Hash, Array,
Scalar, Code and Glob object at the same time.

%prep
%setup -q -n %{module}-%{version} 
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


