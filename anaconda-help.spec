Summary:	Help files for use in the Red Hat Linux installer
Name:		anaconda-help
Version:	10.1.0
Release:	1
License:	distributable
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	54842b3a7b35cbd8f2fcff9f5b843d76
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-style-xsl
BuildRequires:	kdesdk-po2xml
BuildRequires:	openjade
BuildRequires:	xmlto
BuildArch:	noarch

%description
The anaconda-help package contains the help used in anaconda, the Red
Hat Linux installer.

%prep
%setup -q

%build
export LANG=en_US.UTF-8
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_datadir}/anaconda/
%{_datadir}/anaconda/help
