Summary:	Help files for use in the Red Hat Linux installer
Summary(pl.UTF-8):	Pliki pomocy dla instalatora systemu Red Hat Linux
Name:		anaconda-help
Version:	10.1.0
Release:	1
License:	distributable
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	54842b3a7b35cbd8f2fcff9f5b843d76
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-style-xsl
BuildRequires:	kdesdk-po2xml
BuildRequires:	openjade
BuildRequires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The anaconda-help package contains the help used in anaconda, the Red
Hat Linux installer.

%description -l pl.UTF-8
Ten pakiet zawiera pliki pomocy używane przez anacondę - instalator
systemu Red Hat Linux.

%prep
%setup -q

%build
export LANG=en_US.UTF-8
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/anaconda/help
