#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Config-Any
Version  : 0.33
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Config-Any-0.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Config-Any-0.33.tar.gz
Summary  : 'Load configuration from different file formats, transparently'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Config-Any-license = %{version}-%{release}
Requires: perl-Config-Any-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Pluggable::Object)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Config::Any - Load configuration from different file formats,
transparently

%package dev
Summary: dev components for the perl-Config-Any package.
Group: Development
Provides: perl-Config-Any-devel = %{version}-%{release}
Requires: perl-Config-Any = %{version}-%{release}

%description dev
dev components for the perl-Config-Any package.


%package license
Summary: license components for the perl-Config-Any package.
Group: Default

%description license
license components for the perl-Config-Any package.


%package perl
Summary: perl components for the perl-Config-Any package.
Group: Default
Requires: perl-Config-Any = %{version}-%{release}

%description perl
perl components for the perl-Config-Any package.


%prep
%setup -q -n Config-Any-0.33
cd %{_builddir}/Config-Any-0.33

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-Any
cp %{_builddir}/Config-Any-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-Any/c21ba792acddf881776f37bf5090f4fa816bb50a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::Any.3
/usr/share/man/man3/Config::Any::Base.3
/usr/share/man/man3/Config::Any::General.3
/usr/share/man/man3/Config::Any::INI.3
/usr/share/man/man3/Config::Any::JSON.3
/usr/share/man/man3/Config::Any::Perl.3
/usr/share/man/man3/Config::Any::XML.3
/usr/share/man/man3/Config::Any::YAML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-Any/c21ba792acddf881776f37bf5090f4fa816bb50a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
