Summary:	Kopete MSN emoticons
Summary(pl.UTF-8):	Emotikony MSN dla Kopete
Name:		kopete-emoticons-msn
Version:	2.03
Release:	0.1
# distributable? I doubt...
License:	Downloaded from web; (c) Microsoft Corporation, all rights reserved
Group:		Themes
Source0:	http://glen.alkohol.ee/gaim-smileys/msn-emoticons-%{version}.tar.bz2
# Source0-md5:	406996b8263f5b57e03435112fae5968
#Source0:	http://www.kde-look.org/content/files/6721-crystal_v2.tar.gz
URL:		http://messenger.msn.com/Resource/Emoticons.aspx
#URL:		http://www.kde-look.org/content/show.php?content=6721
Requires:	kdenetwork-kopete
Requires:	kdenetwork-kopete-protocol-msn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	%{_datadir}/emoticons/MSN

%description
Emoticons are emotional graphics - visual ways to express the way you
feel when words alone just aren't enough.

This package contains MSN emoticons for Kopete.

%description -l pl.UTF-8
Emotikony to obrazki wyrażające uczucia, pozwalające wyrazić to, co
czuje użytkownik, kiedy nie wystarczają słowa.

Ten pakiet zawiera emotikony MSN dla Kopete.

%prep
%setup -q -n msn-emoticons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}
cp -a * $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themedir}
