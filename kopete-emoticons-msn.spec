Summary:	Kopete MSN 6.0 emoticons
Name:		kopete-emoticons-msn
Version:	2.01
Release:	0.1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/6721-crystal_v2.tar.gz
# Source0-md5:	a5584a5f300b7efd647904da023e286b
URL:		http://www.kde-look.org/content/show.php?content=6721
Requires:	kdenetwork-kopete
Requires:	kdenetwork-kopete-protocol-msn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kopetedir	%{_datadir}/apps/kopete/pics/emoticons
%define		_themedir	%{_kopetedir}/MSN

%description
MSN 6.0 emoticons for Kopete.

%prep
%setup -q -n crystal_v2

%install
rm -rf $RPM_BUILD_ROOT%{_themedir}
install -d $RPM_BUILD_ROOT%{_themedir}
cp -a * $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themedir}
