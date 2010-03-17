Summary:	The LDP's System Administrators' Guide in HTML format
Name:		sag
Version:	0.7.0
Release:	%mkrel 9
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


