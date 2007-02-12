#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	CharWidth
Summary:	Text::CharWidth - Get number of occupied columns of a string on terminal
Summary(pl.UTF-8):	Text::CharWidth - obliczanie liczby kolumn zajmowanych przez łańcuch na terminalu
Name:		perl-Text-CharWidth
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37a723df0580c0758c0ee67b37336c15
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module to provide equivalent feature as wcwidth(3) and
wcswidth(3). This also provides mblen(3) equivalent subroutine.

%description -l pl.UTF-8
Ten moduł udostępnia funkcjonalność odpowiadającą wcwidth(3) i
wcswidth(3). Udostępnia także funkcję odpowiadającą mblen(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/Text/CharWidth.pm
%dir %{perl_vendorarch}/auto/Text/CharWidth
%{perl_vendorarch}/auto/Text/CharWidth/CharWidth.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/CharWidth/CharWidth.so
%{_mandir}/man3/*
