Summary:	PCS - Parameter and Communications Subsystems
Summary(pl):	PCS - podsystemy parametrów i komunikacji
Name:		starlink-pcs
Version:	4.1_1.218
Release:	1
License:	non-commercial use and distribution (see PCS_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/pcs/pcs.tar.Z
# Source0-md5:	7a3710a40b158bc06e3e9f6895c68edf
Patch0:		%{name}-make.patch
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

%description -l pl
Aplikacje zwykle potrzebuj± uzyskaæ warto¶ci parametrów z ró¿nych
¼róde³ oraz komunikowaæ siê z innymi programami. PCS (Parameter and
Communication Subsystems - podsystemy parametrów i komunikacji) to
zbiór blisko zwi±zanych bibliotek funkcji dostarczaj±cych te
mo¿liwo¶ci dla wielu aplikacji Starlinka i zwi±zanych interfejsów
u¿ytkownika.

Biblioteki PCS w ogólno¶ci nie s± wywo³ywane bezpo¶rednio przez
aplikacjê, ale tworz± podstawow± czê¶æ ¶rodowiska programistycznego
Starlink.

%package devel
Summary:	Header files for PCS libraries
Summary(pl):	Pliki nag³ówkowe bibliotek PCS
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	starlink-hds-devel
Requires:	starlink-hlp-devel
Requires:	starlink-psx-devel

%description devel
Header files for PCS libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek PCS.

%package static
Summary:	Static Starlink PCS libraries
Summary(pl):	Statyczne biblioteki Starlink PCS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Starlink PCS libraries.

%description static -l pl
Statyczne biblioteki Starlink PCS.

%prep
%setup -q -c
%patch -p1

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
