%define	pdir	SGML
%define	pnam	SPGroveBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	SGML-SPGroveBuilder perl module
Summary(pl):	Modu� perla SGML-SPGroveBuilder
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	5
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	�r�unart�l/Forritunarm�l/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Spr�k/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-opensp.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	opensp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SGML::SPGrove module links with James Clark's SGML Parser (SP) to
load SGML, XML, and HTML document instances into SGML::Grove objects.

%description -l pl
Modu� SGML::SPGrove linkuje si� z SP - parserem SGML Jamesa Clarka,
aby wczytywa� instancje dokument�w SGML, XML i HTML do obiekt�w
SGML::Grove.

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
