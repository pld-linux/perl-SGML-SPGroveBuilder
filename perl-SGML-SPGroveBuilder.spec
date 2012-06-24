%include	/usr/lib/rpm/macros.perl
%define		pdir	SGML
%define		pnam	SPGroveBuilder
Summary:	SGML::SPGroveBuilder Perl module
Summary(cs):	Modul SGML::SPGroveBuilder pro Perl
Summary(da):	Perlmodul SGML::SPGroveBuilder
Summary(de):	SGML::SPGroveBuilder Perl Modul
Summary(es):	M�dulo de Perl SGML::SPGroveBuilder
Summary(fr):	Module Perl SGML::SPGroveBuilder
Summary(it):	Modulo di Perl SGML::SPGroveBuilder
Summary(ja):	SGML::SPGroveBuilder Perl �⥸�塼��
Summary(ko):	SGML::SPGroveBuilder �� ����
Summary(no):	Perlmodul SGML::SPGroveBuilder
Summary(pl):	Modu� Perla SGML::SPGroveBuilder
Summary(pt):	M�dulo de Perl SGML::SPGroveBuilder
Summary(pt_BR):	M�dulo Perl SGML::SPGroveBuilder
Summary(ru):	������ ��� Perl SGML::SPGroveBuilder
Summary(sv):	SGML::SPGroveBuilder Perlmodul
Summary(uk):	������ ��� Perl SGML::SPGroveBuilder
Summary(zh_CN):	SGML::SPGroveBuilder Perl ģ��
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	8
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-opensp.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	opensp-devel >= 1.5pre5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SGML::SPGrove module links with James Clark's SGML Parser (SP) to
load SGML, XML, and HTML document instances into SGML::Grove objects.

%description -l pl
Modu� SGML::SPGrove jest konsolidowany z SP - parserem SGML Jamesa
Clarka. Dzi�ki temu mo�na wczytywa� instancje dokument�w SGML, XML i
HTML do obiekt�w SGML::Grove.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes ChangeLog README ToDo
%{perl_sitearch}/SGML
%dir %{perl_sitearch}/auto/SGML
%dir %{perl_sitearch}/auto/SGML/SPGroveBuilder
%{perl_sitearch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.bs
%attr(755,root,root) %{perl_sitearch}/auto/SGML/SPGroveBuilder/SPGroveBuilder.so
%{_mandir}/man3/*
