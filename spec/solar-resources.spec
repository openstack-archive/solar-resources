%define name solar-resources
%{!?version: %define version 0.1.0}
%{!?release: %define release 1}

Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Summary: solar-resources
URL:     http://mirantis.com
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%description
Solar-resources are resources definitions and example deployments for solar project.

%prep
%setup -q -n %{name}-%{version}

%install
#copy resources
install -d -m 755 %{buildroot}%{_datadir}/solar-resources/
cp -a %{_builddir}/%{name}-%{version}/examples %{buildroot}%{_datadir}/solar-resources/
cp -a %{_builddir}/%{name}-%{version}/resources %{buildroot}%{_datadir}/solar-resources/
cp -a %{_builddir}/%{name}-%{version}/templates %{buildroot}%{_datadir}/solar-resources/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_datadir}/solar-resources/*

