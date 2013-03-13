Name: shinyapps

# Specify dynamic version with: --define "version 1.2.3"
Version:	%{version}
Release:	%{release}
Summary:	Shiny Apps

Group:		Web/Applications
License:	BSD
URL:		http://snap.uaf.edu:8080
Source0:	shinyapps.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch
ExclusiveArch:  noarch

BuildRequires:  R-core

%define inst_dir /var/shiny-server/www
%define hostname www.snap.uaf.edu

%description
This package contains the various R Shiny apps developed for the SNAP website.

%prep
%setup -c

%build
make javascript
make version

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}/%{inst_dir}
mkdir -p ${RPM_BUILD_ROOT}/home/jenkins/
mkdir -p ${RPM_BUILD_ROOT}/etc/cron.weekly/
mkdir -p ${RPM_BUILD_ROOT}/tmp

touch ${RPM_BUILD_ROOT}/var/log/httpd/%{hostname}-error_log
touch ${RPM_BUILD_ROOT}/var/log/httpd/%{hostname}-access_log
touch ${RPM_BUILD_ROOT}/var/log/httpd/%{hostname}-update_log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%ghost %attr(644,jenkins,jenkins) /var/log/httpd/%{hostname}-update_log

%post
/usr/local/bin/shiny-server
