%include	/usr/lib/rpm/macros.perl
Summary:	SGML-SPGroveBuilder perl module
Summary(pl):	Modu³ perla SGML-SPGroveBuilder
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SGML/SGML-SPGroveBuilder-%{version}.tar.gz
Patch0:		perl-SGML-SPGroveBuilder-opensp.patch
Patch1:		perl-SGML-SPGroveBuilder-perl-5.6.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	opensp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SGML::SPGrove module links with James Clark's SGML Parser (SP)
to load SGML, XML, and HTML document instances into SGML::Grove
objects.

%prep
%setup -q -n SGML-SPGroveBuilder-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes ChangeLog README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/SGML/*.pm
%{perl_sitearch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.bs
%attr(755,root,root) %{perl_sitearch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.so
%{_mandir}/man3/*
