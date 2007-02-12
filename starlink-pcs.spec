Summary:	PCS - Parameter and Communications Subsystems
Summary(pl.UTF-8):   PCS - podsystemy parametrów i komunikacji
Name:		starlink-pcs
Version:	4.1_1.218
Release:	2
License:	non-commercial use and distribution (see PCS_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/pcs/pcs.tar.Z
# Source0-md5:	7a3710a40b158bc06e3e9f6895c68edf
Patch0:		%{name}-make.patch
Patch1:		%{name}-alpha.patch
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_PCS.html
BuildRequires:	gcc-g77
BuildRequires:	ncurses-devel
BuildRequires:	starlink-hds-devel
BuildRequires:	starlink-hlp-devel
BuildRequires:	starlink-psx-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
Application programs often need to obtain parameter values from a
variety of sources and to communicate with other programs. The
Parameter and Communication Subsystems (PCS) are a set of
closely-related subroutine libraries which provide these facilities
for many Starlink applications and the associated user-interfaces.

The PCS libraries will not generally be called directly by application
programs, but form a basic part of the Starlink Software Environment.

%description -l pl.UTF-8
Aplikacje zwykle potrzebują uzyskać wartości parametrów z różnych
źródeł oraz komunikować się z innymi programami. PCS (Parameter and
Communication Subsystems - podsystemy parametrów i komunikacji) to
zbiór blisko związanych bibliotek funkcji dostarczających te
możliwości dla wielu aplikacji Starlinka i związanych interfejsów
użytkownika.

Biblioteki PCS w ogólności nie są wywoływane bezpośrednio przez
aplikację, ale tworzą podstawową część środowiska programistycznego
Starlink.

%package devel
Summary:	Header files for PCS libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek PCS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-hds-devel
Requires:	starlink-hlp-devel
Requires:	starlink-psx-devel

%description devel
Header files for PCS libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek PCS.

%package static
Summary:	Static Starlink PCS libraries
Summary(pl.UTF-8):   Statyczne biblioteki Starlink PCS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink PCS libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Starlink PCS.

%prep
%setup -q -c
%patch0 -p1
cd dtask
mkdir tmp
cd tmp
tar xf ../dtask_source.tar
%patch1 -p0
tar cf ../dtask_source.tar *
cd ../..

%build
PATH="$PATH:%{stardir}/bin" \
OPT="%{rpmcflags}" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc PCS_CONDITIONS pcs.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/ssn*
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/*_dev
%attr(755,root,root) %{stardir}/bin/*_link*
%attr(755,root,root) %{stardir}/bin/alink
%attr(755,root,root) %{stardir}/bin/ilink
%attr(755,root,root) %{stardir}/bin/compifl
%dir %{stardir}/etc
%{stardir}/etc/dtask_main.txt
%{stardir}/include/*
%{stardir}/lib/dtask_main.o

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
