#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Cron
Summary:	POE::Component::Cron - Schedule POE Events using a cron spec
Summary(pl.UTF-8):	POE::Component::Cron - szeregowanie zdarzeń POE przy użyciu opisów crona
Name:		perl-POE-Component-Cron
Version:	0.019
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d19dcda613946c90846d3359ba2e628
URL:		http://search.cpan.org/dist/POE-Component-Cron/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Event-Cron
BuildRequires:	perl-DateTime-Event-Random
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component encapsulates a session that sends events to client
sessions on a schedule as defined by a DateTime::Set iterator. The
implementation is straight forward if a little limited.

%description -l pl.UTF-8
Ten komponent obudowuje sesję wysyłającą zdarzenia do sesji klienckich
zgodnie z planem określonym przez iterator DateTime::Set.
Implementacja jest bezpośrednia, choć nieco ograniczona.

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
%{_mandir}/man3/*
