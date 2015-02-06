%define name	perl-Maui
%define version 0.0.5
%define release 15

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



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.0.5-13mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0.5-12mdv2011.0
+ Revision: 556004
- rebuild for perl 5.12

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.5-11mdv2010.0
+ Revision: 430502
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-10mdv2009.0
+ Revision: 257819
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-9mdv2009.0
+ Revision: 245875
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-7mdv2008.1
+ Revision: 152128
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.5-6mdv2008.0
+ Revision: 86638
- rebuild


* Thu May 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.0.5-5mdk
- Fix Build
- use mkrel

* Tue Nov 16 2004 Michael Scherer <misc@mandrake.org> 0.0.5-4mdk
- Rebuild for new perl
- fix spec

* Mon Aug 18 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 0.0.5-3mdk
- add description, buildrequires (scherer.michael@free.fr)

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.5-2mdk
- rebuild for new auto{prov,req}

