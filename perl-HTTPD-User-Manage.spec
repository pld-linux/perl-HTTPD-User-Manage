%include	/usr/lib/rpm/macros.perl
Summary:	HTTPD-User-Manage perl module
Summary(pl):	Modu³ perla HTTPD-User-Manage
Name:		perl-HTTPD-User-Manage
Version:	1.53
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTPD/HTTPD-User-Manage-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-HTTPD-Tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTPD-User-Manage perl module

%description -l pl
Modu³ perla HTTPD-User-Manage

%prep
%setup -q -n HTTPD-User-Manage-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTTPD-User-Manage
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/HTTPD/*.pm
%{perl_sitelib}/HTTPD/GroupAdmin/*.pm
%{perl_sitelib}/HTTPD/GroupAdmin/DBM/apache.pm
%{perl_sitelib}/HTTPD/GroupAdmin/Text/cern.pm
%{perl_sitelib}/HTTPD/UserAdmin/*.pm
%{perl_sitelib}/HTTPD/UserAdmin/DBM/netscape.pm
%{perl_sitelib}/HTTPD/UserAdmin/Text/cern.pm
%{perl_sitearch}/auto/HTTPD-User-Manage

%{_mandir}/man3/*
