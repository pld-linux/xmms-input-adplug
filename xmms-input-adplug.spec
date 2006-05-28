Summary:	AdLib player plugin for XMMS
Summary(pl):	Wtyczka odtwarzaj±ca AdLib dla XMMS-a
Name:		xmms-input-adplug
Version:	1.2
Release:	1
License:	LGPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/adplug/adplug-xmms-%{version}.tar.bz2
# Source0-md5:	293808d1520d9d04c7909d4acb187943
URL:		http://adplug.sourceforge.net/
BuildRequires:	adplug-devel >= 2.0
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	xmms-devel >= 0.9.5.1
Requires:	adplug >= 2.0
Requires:	xmms >= 0.9.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdPlug/XMMS is an XMMS input plugin. XMMS is a cross-platform
multimedia player. AdPlug/XMMS uses the AdPlug AdLib sound player
library to play back a wide range of AdLib (OPL2) music file formats
on top of an OPL2 emulator. No OPL2 chip is required for playback.

%description -l pl
AdPlug/XMMS to wtyczka wej¶ciowa XMMS-a. XMMS to wieloplatformowy
odtwarzacz multimediów. AdPlug/XMMS wykorzystuje bibliotekê
odtwarzacza d¼wiêku AdLib AdPlug do odtwarzania wielu ró¿nych formatów
plików muzycznych AdLib (OPL2) przy u¿yciu emulatora OPL2. Uk³ad OPL2
nie jest wymagany do odtwarzania.

%prep
%setup -q -n adplug-xmms-%{version}

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
