Summary:	The LDP's System Administrators' Guide in HTML format
Name:		sag
Version:	0.7.0
Release:	%mkrel 12
License:	distributable
Group:		Books/Computer books
URL:		http://www.linuxdoc.org/LDP/sag/
Source:		sag-0.6.2-html.tar.bz2
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Linux Documentation Project's System Administrators' Guide, provided in
HTML format. This document provides a generic guide to Linux system
administration. Check the Linux Documentation Project's website at
http://www.metalab.unc.edu/LDP/ for other formats of this document or for any
updates.

Install the sag package if you'd like to use the HTML version of the LDP's
System Administrators' Guide on your own machine.

%prep

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_docdir}/LDP/sag
tar -jxf %{SOURCE0} -C $RPM_BUILD_ROOT%{_docdir}/LDP/sag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/LDP/sag




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-11mdv2011.0
+ Revision: 669955
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-10mdv2011.0
+ Revision: 607493
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-9mdv2010.1
+ Revision: 523958
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7.0-8mdv2010.0
+ Revision: 426971
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-7mdv2009.0
+ Revision: 225361
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.7.0-6mdv2008.1
+ Revision: 126937
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-6mdv2007.1
+ Revision: 145390
- Import sag

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-6mdv2007.1
- use the %%mrel macro

