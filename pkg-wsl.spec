Name:		wsl
Version:	1.0.0
Release:	1%{?dist}
Summary:	Wsman Shell Command Line "whistle"

Group:		System/Management
License:	BSD
URL:		http://linux.dell.com/files/%{name}
Source0:	http://linux.dell.com/files/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Vendor:		Dell Inc.

Requires:	bash wget libxml2
Requires:	gpg
BuildArch:	noarch

%description
WSL (aka "whistle") contains various scripts that serve as a client interface 
to WSMAN or Web Services for Management protocol base on DMTF standard 
specification. WSMAN provides standards based messaging for systems management 
CIM-style objects.



%prep
%setup -q




%install
rm -rf $RPM_BUILD_ROOT

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


mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
install -m 644 %{_builddir}/%{name}-%{version}/LICENSE $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
install -m 644 %{_builddir}/%{name}-%{version}/README-wsl $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
install -m 644 %{_builddir}/%{name}-%{version}/VERSION $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
install -m 644 %{_builddir}/%{name}-%{version}/wsl-config $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sysconfdir}/%{name}

%doc
%{_defaultdocdir}/%{name}-%{version}



%changelog
* Tue Sep 25 2012 Chris Poblete <chris_poblete@dell.com> - 1.0.0-1
- initial version of WSL.

