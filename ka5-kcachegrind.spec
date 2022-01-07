%define		kdeappsver	21.12.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kcachegrind

Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl.UTF-8):	KCachegrind - wizualizacja ścieżek tworzonych przez profilowanie
Name:		ka5-kcachegrind
Version:	21.12.1
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a6b2b64fcf80fb9c7b39e7363362f14f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.600
Suggests:	%{name}-tools = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCachegrind visualizes traces generated by profiling.

%description -l pl.UTF-8
KCachegrind wizualizuje ślady tworzone przez profilowanie.

%package tools
Summary:	Tools to convert various profiling data to calltree format
Summary(pl.UTF-8):	Narzędzia do konwersji różnych danych profilujących do formatu calltree
Group:		Development/Tools

%description tools
Tools to convert various profiling data to calltree format, used by
Valgrind tools.

%description tools -l pl.UTF-8
Narzędzia do konwersji różnych danych profilujących do formatu
calltree, stosowanego przez narzędzia Valgrinda.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env php#/usr/bin/php#' '{}' +
find $RPM_BUILD_ROOT%{_bindir} -type f -exec sed -i -e 's#/usr/bin/env python#/usr/bin/python2#' '{}' +

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%{_desktopdir}/org.kde.kcachegrind.desktop
%{_iconsdir}/hicolor/128x128/apps/kcachegrind.png
%{_iconsdir}/hicolor/32x32/apps/kcachegrind.png
%{_iconsdir}/hicolor/48x48/apps/kcachegrind.png
%{_iconsdir}/hicolor/64x64/apps/kcachegrind.png
%dir %{_datadir}/kcachegrind
%dir %{_datadir}/kcachegrind/icons
%dir %{_datadir}/kcachegrind/icons/hicolor
%dir %{_datadir}/kcachegrind/icons/hicolor/16x16
%dir %{_datadir}/kcachegrind/icons/hicolor/16x16/actions
%{_datadir}/kcachegrind/icons/hicolor/16x16/actions/move.png
%{_datadir}/kcachegrind/icons/hicolor/16x16/actions/percent.png
%dir %{_datadir}/kcachegrind/icons/hicolor/22x22
%dir %{_datadir}/kcachegrind/icons/hicolor/22x22/actions
%{_datadir}/kcachegrind/icons/hicolor/22x22/actions/hidetemplates.png
%{_datadir}/kcachegrind/icons/hicolor/22x22/actions/move.png
%{_datadir}/kcachegrind/icons/hicolor/22x22/actions/percent.png
%dir %{_datadir}/kcachegrind/icons/hicolor/32x32
%dir %{_datadir}/kcachegrind/icons/hicolor/32x32/actions
%{_datadir}/kcachegrind/icons/hicolor/32x32/actions/percent.png
%{_datadir}/kcachegrind/tips
%{_datadir}/metainfo/org.kde.kcachegrind.appdata.xml

%files tools
%defattr(644,root,root,755)
%doc converters/README
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/pprof2calltree
