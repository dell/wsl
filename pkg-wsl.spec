Name:		wsl
Version:	1.0.0
Release:	1%{?dist}
Summary:	Wsman Shell Command Line "whistle"

Group:		Applications/System
License:	BSD
URL:		http://linux.dell.com/files/%{name}
Source0:	http://linux.dell.com/files/%{name}/%{name}-%{version}.tar.gz

Requires:	bash curl libxml2
Requires:	gpg
BuildArch:	noarch

%description
WSL (aka "whistle") contains various scripts that serve as a client interface 
to WSMAN or Web Services for Management protocol base on DMTF standard 
specification. WSMAN provides standards based messaging for systems management 
CIM-style objects.



%prep
%setup -q

%build


%install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 644 %{_builddir}/%{name}-%{version}/wsl-functions $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
install -m 644 %{_builddir}/%{name}-%{version}/wsl-ws2textc.xsl $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}


mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wsl $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslcred $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslecn $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslenum $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslget $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslid $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslinvoke $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslput $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wxmlgetvalue $RPM_BUILD_ROOT/%{_bindir}



mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{_builddir}/%{name}-%{version}/wsl.1 $RPM_BUILD_ROOT%{_mandir}/man1




%files
%{_bindir}/*
%{_sysconfdir}/%{name}


%doc LICENSE README-wsl VERSION wsl-config
%{_mandir}/man1/%{name}.1.*




%changelog
* Mon Oct  8 2012 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.1.8-2
- Removing the explicit installation of the doc files as the %doc macro will handle the same
- Not zipping the man file, as the package build will handle it.

* Mon Oct  8 2012 Praveen K Paladugu <praveen_paladugu@dell.com>- 0.1.8-1
- Minor changes to spec file, following Fedora reviewer's suggestions.


* Tue Oct  2 2012 Chris Poblete <chris_poblete@dell.com> - 0.1.7c-1
- Added a man page for wsl

* Tue Sep 25 2012 Chris Poblete <chris_poblete@dell.com> - 0.1.0-1
- initial version of WSL.

