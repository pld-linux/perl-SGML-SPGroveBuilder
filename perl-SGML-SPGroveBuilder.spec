%include	/usr/lib/rpm/macros.perl
Summary:	SGML-SPGroveBuilder perl module
Summary(pl):	Modu³ perla SGML-SPGroveBuilder
Name:		perl-SGML-SPGroveBuilder
Version:	2.01
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SGML/SGML-SPGroveBuilder-%{version}.tar.gz
Patch0:		%{name}-opensp.patch
Patch1:		%{name}-perl-5.6.patch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	opensp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SGML::SPGrove module links with James Clark's SGML Parser (SP) to
load SGML, XML, and HTML document instances into SGML::Grove objects.

%description -l pl
Modu³ SGML::SPGrove linkuje siê z SP - parserem SGML Jamesa Clarka,
aby wczytywaæ instancje dokumentów SGML, XML i HTML do obiektów
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
