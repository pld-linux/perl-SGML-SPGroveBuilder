%include	/usr/lib/rpm/macros.perl
%define		pdir	SGML
%define		pnam	SPGroveBuilder
Summary:	SGML::SPGroveBuilder Perl module - load an SGML, XML, or HTML document
Summary(pl):	Modu³ Perla SGML::SPGroveBuilder - wczytywanie dokumentów SGML, XML i HTML
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	11
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ecd47bf15af12b868c8260f21cd93cf
Patch0:		%{name}-opensp.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	gcc-c++
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	opensp-devel >= 2:1.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML::SPGrove is a Perl 5 module for loading SGML, XML, and HTML
document instances into SGML::Grove objects using SP - James Clark's
SGML Parser.

%description -l pl
Modu³ Perla SGML::SPGrove s³u¿y do wczytywania dokumentów SGML, XML
oraz HTML do obiektów SGML::Grove, korzystaj±c z SP - parsera SGML
Jamesa Clarka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes ChangeLog README ToDo
%{perl_vendorarch}/SGML
%dir %{perl_vendorarch}/auto/SGML
%dir %{perl_vendorarch}/auto/SGML/SPGroveBuilder
%{perl_vendorarch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.so
%{_mandir}/man3/*
