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
install -m 755 %{_builddir}/%{name}-%{version}/viwsl $RPM_BUILD_ROOT/%{_bindir}
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


%doc LICENSE README-wsl VERSION wslrc
%{_mandir}/man1/%{name}.1.*




%changelog
