%include	/usr/lib/rpm/macros.perl
%define		pdir	HTTPD
%define		pnam	User-Manage
Summary:	Managing access control with the Apache, NCSA httpd, CERN and Netscape servers
Summary(pl.UTF-8):	Kontrola dostępu w serwerach Apache, NCSA httpd, CERN i Netscape
Name:		perl-HTTPD-User-Manage
Version:	1.62
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92442d6d04cf09b3b26b79b0f6bfafa5
Patch0:		%{name}-module_names.patch
Patch1:		%{name}-version_tweak.patch
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-HTTPD-Tools

# SQL access is used conditionally
%define		_noautoreq 'perl(Mysql)' 'perl(NDBM_File)'

%description
HTTPD-User-Manage package contains a script and set of Perl modules
for managing access control with the Apache, NCSA httpd, CERN and
Netscape servers (and maybe some others).

%description -l pl.UTF-8
Pakiet HTTPD-User-Manage zawiera skrypt i zestaw modułów Perla do
zarządzania kontrolą dostępu w serwerach Apache, NCSA httpd, CERN i
Netscape (a być może także kilku innych).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/HTTPD
%{perl_vendorlib}/HTTPD/*.pm
%dir %{perl_vendorlib}/HTTPD/GroupAdmin
%{perl_vendorlib}/HTTPD/GroupAdmin/*.pm
%dir %{perl_vendorlib}/HTTPD/GroupAdmin/DBM
%{perl_vendorlib}/HTTPD/GroupAdmin/DBM/apache.pm
%dir %{perl_vendorlib}/HTTPD/GroupAdmin/Text
%{perl_vendorlib}/HTTPD/GroupAdmin/Text/cern.pm
%dir %{perl_vendorlib}/HTTPD/UserAdmin
%{perl_vendorlib}/HTTPD/UserAdmin/*.pm
%dir %{perl_vendorlib}/HTTPD/UserAdmin/DBM
%{perl_vendorlib}/HTTPD/UserAdmin/DBM/netscape.pm
%dir %{perl_vendorlib}/HTTPD/UserAdmin/Text
%{perl_vendorlib}/HTTPD/UserAdmin/Text/cern.pm
%{_mandir}/man3/*
