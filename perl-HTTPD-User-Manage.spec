%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTPD
%define	pnam	User-Manage
Summary:	HTTPD-User-Manage perl module
Summary(pl):	Modu³ perla HTTPD-User-Manage
Name:		perl-HTTPD-User-Manage
Version:	1.58
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl >= 5.005_03-10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-HTTPD-Tools

%description
HTTPD-User-Manage perl module.

%description -l pl
Modu³ perla HTTPD-User-Manage.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTTPD/*.pm
%{perl_sitelib}/HTTPD/GroupAdmin/*.pm
%{perl_sitelib}/HTTPD/GroupAdmin/DBM/apache.pm
%{perl_sitelib}/HTTPD/GroupAdmin/Text/cern.pm
%{perl_sitelib}/HTTPD/UserAdmin/*.pm
%{perl_sitelib}/HTTPD/UserAdmin/DBM/netscape.pm
%{perl_sitelib}/HTTPD/UserAdmin/Text/cern.pm
%{_mandir}/man3/*
