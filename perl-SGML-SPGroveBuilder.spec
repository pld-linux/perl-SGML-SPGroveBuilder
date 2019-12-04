#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	SGML
%define		pnam	SPGroveBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	SGML::SPGroveBuilder Perl module - load an SGML, XML, or HTML document
Summary(pl.UTF-8):	Moduł Perla SGML::SPGroveBuilder - wczytywanie dokumentów SGML, XML i HTML
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	23
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ecd47bf15af12b868c8260f21cd93cf
Patch0:		%{name}-opensp.patch
Patch1:		%{name}-perl-5.6.patch
URL:		http://search.cpan.org/dist/SGML-SPGroveBuilder/
BuildRequires:	opensp-devel >= 2:1.5.1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML::SPGrove is a Perl 5 module for loading SGML, XML, and HTML
document instances into SGML::Grove objects using SP - James Clark's
SGML Parser.

%description -l pl.UTF-8
Moduł Perla SGML::SPGrove służy do wczytywania dokumentów SGML, XML
oraz HTML do obiektów SGML::Grove, korzystając z SP - parsera SGML
Jamesa Clarka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes ChangeLog README ToDo
%{perl_vendorarch}/SGML
%dir %{perl_vendorarch}/auto/SGML
%dir %{perl_vendorarch}/auto/SGML/SPGroveBuilder
%attr(755,root,root) %{perl_vendorarch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.so
%{_mandir}/man3/*
