%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTPD
%define	pnam	User-Manage
Summary:	HTTPD::User::Manage perl module
Summary(pl):	Modu³ perla HTTPD::User::Manage
Name:		perl-HTTPD-User-Manage
Version:	1.59
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-HTTPD-Tools

%description
HTTPD::User::Manage perl module.

%description -l pl
Modu³ perla HTTPD::User::Manage.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
