#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Cron
Summary:	POE::Component::Cron - Schedule POE Events using a cron spec
#Summary(pl):	
Name:		perl-POE-Component-Cron
Version:	0.018
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c1952d80a41d7cd221f2410ede08d7b9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Event::Cron)
BuildRequires:	perl(DateTime::Event::Random)
BuildRequires:	perl(POE)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component encapsulates a session that sends events to client sessions
on a schedule as defined by a DateTime::Set iterator.	The implementation is 
straight forward if a little limited.

This is Beta code.  The API is close to jelling.  I'd love to
hear your ideas if you want to share them.


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
#%%{perl_vendorlib}/POE/Component/Cron
%{_mandir}/man3/*
