%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTPD
%define	pnam	User-Manage
Summary:	HTTPD::User::Manage Perl module
Summary(cs):	Modul HTTPD::User::Manage pro Perl
Summary(da):	Perlmodul HTTPD::User::Manage
Summary(de):	HTTPD::User::Manage Perl Modul
Summary(es):	M�dulo de Perl HTTPD::User::Manage
Summary(fr):	Module Perl HTTPD::User::Manage
Summary(it):	Modulo di Perl HTTPD::User::Manage
Summary(ja):	HTTPD::User::Manage Perl �⥸�塼��
Summary(ko):	HTTPD::User::Manage �� ����
Summary(no):	Perlmodul HTTPD::User::Manage
Summary(pl):	Modu� Perla HTTPD::User::Manage
Summary(pt):	M�dulo de Perl HTTPD::User::Manage
Summary(pt_BR):	M�dulo Perl HTTPD::User::Manage
Summary(ru):	������ ��� Perl HTTPD::User::Manage
Summary(sv):	HTTPD::User::Manage Perlmodul
Summary(uk):	������ ��� Perl HTTPD::User::Manage
Summary(zh_CN):	HTTPD::User::Manage Perl ģ��
Name:		perl-HTTPD-User-Manage
Version:	1.59
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-module_names.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-HTTPD-Tools

# SQL access is used conditionally
%define		_noautoreq "perl(Mysql)"

%description
HTTPD::User::Manage Perl module.

%description -l cs
Modul HTTPD::User::Manage pro Perl.

%description -l da
Perlmodul HTTPD::User::Manage.

%description -l de
HTTPD::User::Manage Perl Modul.

%description -l es
M�dulo de Perl HTTPD::User::Manage.

%description -l fr
Module Perl HTTPD::User::Manage.

%description -l it
Modulo di Perl HTTPD::User::Manage.

%description -l ja
HTTPD::User::Manage Perl �⥸�塼��

%description -l ko
HTTPD::User::Manage �� ����.

%description -l no
Perlmodul HTTPD::User::Manage.

%description -l pl
Modu� Perla HTTPD::User::Manage.

%description -l pt
M�dulo de Perl HTTPD::User::Manage.

%description -l pt_BR
M�dulo Perl HTTPD::User::Manage.

%description -l ru
������ ��� Perl HTTPD::User::Manage.

%description -l sv
HTTPD::User::Manage Perlmodul.

%description -l uk
������ ��� Perl HTTPD::User::Manage.

%description -l zh_CN
HTTPD::User::Manage Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%doc README
%dir %{perl_sitelib}/HTTPD
%{perl_sitelib}/HTTPD/*.pm
%dir %{perl_sitelib}/HTTPD/GroupAdmin
%{perl_sitelib}/HTTPD/GroupAdmin/*.pm
%dir %{perl_sitelib}/HTTPD/GroupAdmin/DBM
%{perl_sitelib}/HTTPD/GroupAdmin/DBM/apache.pm
%dir %{perl_sitelib}/HTTPD/GroupAdmin/Text
%{perl_sitelib}/HTTPD/GroupAdmin/Text/cern.pm
%dir %{perl_sitelib}/HTTPD/UserAdmin
%{perl_sitelib}/HTTPD/UserAdmin/*.pm
%dir %{perl_sitelib}/HTTPD/UserAdmin/DBM
%{perl_sitelib}/HTTPD/UserAdmin/DBM/netscape.pm
%dir %{perl_sitelib}/HTTPD/UserAdmin/Text
%{perl_sitelib}/HTTPD/UserAdmin/Text/cern.pm
%{_mandir}/man3/*
