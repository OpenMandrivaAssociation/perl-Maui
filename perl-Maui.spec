%define name	perl-Maui
%define version 0.0.5
%define release %mkrel 11

Summary:  	Perl5 modules for Maui Scheduler
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://hepwww.ph.qmul.ac.uk/	
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Maui Scheduler is Free Software licensed under the GNU General Public
License. It is designed for parallel batch scheduling
(custom message-passing or MPI-based jobs) on medium to
large clusters. The Maui Scheduler is meant to be a complete
replacement for proprietary schedulers like LSF or PBS.
Check http://mauischeduler.sourceforge.net/

This is Perl5 modules for using the scheduler.
 
%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install

rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root) 
%doc README doc/* MANIFEST LICENSE Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

