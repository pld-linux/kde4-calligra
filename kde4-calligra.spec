# TODO:
#-----------------------------------------------------------------------------
#-- The following OPTIONAL packages could NOT be located on your system.
#-- Consider installing them to enable more features from this software.
#-----------------------------------------------------------------------------
#   * OpenCTL (0.9.10 or higher)  <http://www.opengtl.org>
#     Free Color Transformation Language implementation (part of OpenGTL)
#     Required for High Dynamic Range Color Spaces, YCbCr and LMS support
#   * OpenShiva  <http://www.opengtl.org>
#     OpenShiva interpreter for the Shiva Kernel Language (part of OpenGTL)
#     Required for Shiva based Generators and Filters
#   * QtShiva  <http://www.opengtl.org>
#     Qt bindings for the OpenShiva interpreter (part of libQtGTL)
#     Required for Shiva based Generators and Filters
#   * Spnav  <http://spacenav.sourceforge.net/>
#     3Dconnexion device driver and SDK
#     Required by SpaceNavigator 3D mouse plugin
#
# - enable pqxx bcond when calligra updates to libpqx 4.0
#
# Conditional build:
%bcond_without	pdf		# build without PDF support
%bcond_with	pqxx		# build postgresql driver for kexi

%define		_state		stable
%define		orgname		calligra
%define		kdever		4.9.0
%define		qtver		4.8.2

Summary:	Calligra - powerful office suite for KDE
Summary(pl.UTF-8):	Calligra - potężny pakiet biurowy dla KDE
Name:		kde4-calligra
Version:	2.5.3
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}-%{version}/%{orgname}-%{version}.tar.bz2
# Source0-md5:	83e2679b7ecb923b953ace06db7ca4c2
URL:		http://www.calligra-suite.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	attica-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	doxygen
BuildRequires:	eigen >= 1:2.0.12-3
BuildRequires:	exiv2-devel
BuildRequires:	fftw3-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetds-devel
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	glew-devel
BuildRequires:	gmm-devel
BuildRequires:	gsl-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	kde4-libkdcraw-devel >= %{kdever}
BuildRequires:	kde4-libkexiv2-devel >= %{kdever}
BuildRequires:	kde4-libkipi-devel >= %{kdever}
BuildRequires:	kde4-libksane-devel >= %{kdever}
BuildRequires:	kde4-marble-devel >= %{kdever}
BuildRequires:	kde4-okular-devel >= %{kdever}
BuildRequires:	lcms2-devel
BuildRequires:	libexif-devel >= 0.6.12
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
%{?with_pqxx:BuildRequires:	libpqxx-devel >= 3.0.0}
BuildRequires:	libtiff-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
BuildRequires:	libwps-devel
BuildRequires:	libxml2-devel >= 0:2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mysql-devel
BuildRequires:	openjpeg-devel >= 1.3
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
%{?with_pdf:BuildRequires:	poppler-Qt-devel >= 0.6}
BuildRequires:	pstoedit-devel
BuildRequires:	pstoedit-drv-lplot
BuildRequires:	python-devel >= 2.2
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	soprano-devel
BuildRequires:	sqlite3-devel >= 3.7.13-2
BuildRequires:	xbase-devel
BuildRequires:	zlib-devel
Obsoletes:	kde4-koffice
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calligra is an integrated office suite for K Desktop Environment.
Calligra contains:
- Words - word processor
- Sheets - spreadsheet
- Stage - presentations
- Flow - An easy to use diagramming and flowcharting application
- Karbon - A vector-based drawing application
- Krita - A pixel-based drawing application like The GIMP
- Braindump - A notes and idea gathering application
- Kexi - A visual database creator
- Plan - A project management application

%description -l pl.UTF-8
Calligra jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet zawiera:
- Words - procesor tekstu
- Sheets - arkusz kalkulacyjny
- Stage - tworzenie prezentacji
- Flow - aplikacja do tworzenia diagramów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej
- Braindump - narzędzie do ogranizacji pomysłow i notatek
- Kexi - narzędzie do tworzenia baz danych
- Plan - aplikacja do zarządzania projektami

%package devel
Summary:	Calligra - header files
Summary(pl.UTF-8):	Calligra - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-devel

%description devel
This package includes the header files you will need to compile
applications that use calligra libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy kompilowaniu
programów używających bibliotek Calligra.

%package common
Summary:	Calligra - common files and libraries
Summary(pl.UTF-8):	Calligra - wspólne pliki i biblioteki
Group:		X11/Applications
Requires:	kde4-kdebase-workspace >= %{kdever}
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
Obsoletes:	kde4-koffice-common
Obsoletes:	kde4-koffice-kformula

%description common
Calligra is an integrated office suite for K Desktop Environment.
Calligra contains:
- Words - word processor
- Sheets - spreadsheet
- Stage - presentations
- Flow - An easy to use diagramming and flowcharting application
- Karbon - A vector-based drawing application
- Krita - A pixel-based drawing application like The GIMP
- Braindump - A tool to dump and organize the content of your brain
- Kexi - A visual database creator
- Plan - A project management application

Package contains common files and libraries needs by Calligra
applications.

%description common -l pl.UTF-8
Calligra jest zintegrowanym pakietem biurowym dla środowiska KDE.
Pakiet zawiera:
- Words - procesor tekstu
- Sheets - arkusz kalkulacyjny
- Stage - tworzenie prezentacji
- Flow - aplikacja do tworzenia diagramów
- Karbon - aplikacja do edycji grafiki wektorowej
- Krita - aplikacja do edycji grafiki bitmapowej
- Braindump - narzędzie do ogranizacji pomysłow
- Kexi - narzędzie do tworzenia baz danych
- Plan - aplikacja do zarządzania projektami

Pakiet zawiera wspólne pliki i biblioteki wymagane przez aplikacje
Calligra.

%package karbon
Summary:	Calligra - Karbon
Summary(pl.UTF-8):	Calligra - Karbon
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	pstoedit
Requires:	pstoedit-drv-lplot
Obsoletes:	kde4-koffice-karbon

%description karbon
Karbon is a vector graphics application within Calligra.

%description karbon -l pl.UTF-8
Karbon to aplikacja służąca do rysowania grafiki wektorowej,

%package kexi
Summary:	Calligra - Kexi
Summary(pl.UTF-8):	Calligra - Kexi
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kexi

%description kexi
Kexi is Calligra part for using database system such as MySQL.

%description kexi -l pl.UTF-8
Kexi jest aplikacją służącą do korzystania z systemów baz danych
takich jak MySQL.

%package flow
Summary:	Calligra - Flow
Summary(pl.UTF-8):	Calligra - Flow
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kchart
Obsoletes:	kde4-koffice-kivio

%description flow
Flow on the surface is your everyday flowcharting program. Underneath
this skin, however, lies much more. Flow will offer basic flowcharting
abilities, but with a twist. Objects are scriptable, and a backend
plugin system will offer the ability to make objects do just about
anything. Feed it a directory of C++ header files, or even Java files,
and let it generate a graphical class map for you. Give it a network
and let it explore and map out the network for you. All this is
possible through the scripting/plugin architecture Flow will possess.

%description flow -l pl.UTF-8
Flow jest programem typu flowcharting. Pod tym pojęciem jednak kryje
się znacznie więcej. Flow dostarcza najpotrzebniejsze funkcje, ale
wszystkie obiekty można rozszerzać za pomocą języka skryptowego, a
system wtyczek backendowych oferuje możliwość tworzenia obiektów
dotyczących prawie wszystkiego. Flow można nakarmić katalogiem plików
nagłówkowych C++ lub plików Javy i pozwolić wygenerować graficzną mapę
klas. Po podaniu sieci przejrzy ją i stworzy jej mapę. Wszystko to
jest możliwe poprzez architekturę skryptów i wtyczek Flow.

%package braindump
Summary:	Calligra - Braindump
Summary(pl.UTF-8):	Calligra - Braindump
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description braindump
Braindump is a notes and idea gathering application.

%package plan
Summary:	Calligra - Plan
Summary(pl.UTF-8):	Calligra - Plan
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kplato

%description plan
Plan is a project management application.

%package stage
Summary:	Calligra - Stage
Summary(pl.UTF-8):	Calligra - Stage
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kpresenter

%description stage
Stage is a presentation application of the Calligra, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description stage -l pl.UTF-8
Stage jest aplikacją Calligra do tworzenia prezentacji, podobną do MS
PowerPoint. Możesz użyć jej do tworzenia wizualnych prezentacji.

%package krita
Summary:	Calligra - Krita
Summary(pl.UTF-8):	Calligra - Krita
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-krita

%description krita
Krita is a painting and image editing application for Calligra. It
supports many color spaces like RGB, grayscale, CMYK, Lab, YCBCR and
LMS, in 8 and 16 bits per channel

%description krita -l pl.UTF-8
Krita jest aplikacją do edycji grafiki bitmapowej. Wspiera różne
przestrzenie barw, jak np. RGB, skala szarości, CMYK, Lab, YCBCR oraz
LMS - zarówno w trybie 8 jak i 16 bitowym na kanał.

%package sheets
Summary:	Calligra - Sheets
Summary(pl.UTF-8):	Calligra - Sheets
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kspread

%description sheets
Sheets is the spread sheet of the Calligra, similar to MS Excel.

%description sheets -l pl.UTF-8
Sheets jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%package words
Summary:	Calligra - Words
Summary(pl.UTF-8):	Calligra - Words
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	kde4-koffice-kword

%description words
Words is a FrameMaker-like wordprocessor application for Calligra. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description words -l pl.UTF-8
Words jest ramkowym procesorem tekstu. Może być użyty do DTP, ale
również do zwykłej edycji tekstu (jak pisanie listów, raportów, itp.).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBUILD_cstester:BOOL=OFF \
	-DBUILD_active:BOOL=OFF \
	-DBUILD_koabstraction:BOOL=OFF \
	-DBUILD_mobile:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# where they get this size from?
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/45x45

%clean
rm -rf $RPM_BUILD_ROOT

%post common
/sbin/ldconfig
%update_icon_cache hicolor
%update_icon_cache oxygen
%update_desktop_database

%postun common
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_icon_cache hicolor
	%update_icon_cache oxygen
	%update_desktop_database
fi

%post karbon
/sbin/ldconfig
%update_desktop_database

%postun karbon
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post flow
/sbin/ldconfig
%update_desktop_database

%postun flow
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post kexi
/sbin/ldconfig
%update_desktop_database

%postun kexi
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post plan
/sbin/ldconfig
%update_desktop_database

%postun plan
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post stage
/sbin/ldconfig
%update_desktop_database

%postun stage
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post krita
/sbin/ldconfig
%update_desktop_database

%postun krita
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post sheets
/sbin/ldconfig
%update_desktop_database

%postun sheets
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post words
/sbin/ldconfig
%update_desktop_database

%postun words
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%post braindump
/sbin/ldconfig
%update_desktop_database

%postun braindump
/sbin/ldconfig
if [ "$1" = 0 ]; then
	%update_desktop_database
fi

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligra
%attr(755,root,root) %{_bindir}/calligraconverter
%attr(755,root,root) %{_libdir}/libRtfReader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libRtfReader.so.10
%attr(755,root,root) %{_libdir}/libchartshapelib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchartshapelib.so.10
%attr(755,root,root) %{_libdir}/libflake.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflake.so.10
%attr(755,root,root) %{_libdir}/libkformulalib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformulalib.so.10
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdchart.so.10
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkochart.so.10
%attr(755,root,root) %{_libdir}/libkokross.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkokross.so.10
%attr(755,root,root) %{_libdir}/libkomain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkomain.so.10
%attr(755,root,root) %{_libdir}/libkoodf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodf.so.10
%attr(755,root,root) %{_libdir}/libkopageapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopageapp.so.10
%attr(755,root,root) %{_libdir}/libkoplugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoplugin.so.10
%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoproperty.so.10
%attr(755,root,root) %{_libdir}/libkoreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoreport.so.10
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotext.so.10
%attr(755,root,root) %{_libdir}/libkowidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowidgets.so.10
%attr(755,root,root) %{_libdir}/libkowv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowv2.so.9
%attr(755,root,root) %{_libdir}/libkundo2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkundo2.so.10
%attr(755,root,root) %{_libdir}/liblibwmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblibwmf.so.10
%attr(755,root,root) %{_libdir}/libmsooxml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmsooxml.so.10
%attr(755,root,root) %{_libdir}/libpigmentcms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigmentcms.so.10
%attr(755,root,root) %{_libdir}/libtextlayout.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtextlayout.so.10
%attr(755,root,root) %{_libdir}/kde4/artistictextshape.so
%attr(755,root,root) %{_libdir}/kde4/autocorrect.so
%attr(755,root,root) %{_libdir}/kde4/calligradockers.so
%attr(755,root,root) %{_libdir}/kde4/calligragoogledocs.so
%attr(755,root,root) %{_libdir}/kde4/calligrathumbnail.so
%attr(755,root,root) %{_libdir}/kde4/changecase.so
%attr(755,root,root) %{_libdir}/kde4/chartshape.so
%attr(755,root,root) %{_libdir}/kde4/commentshape.so
%attr(755,root,root) %{_libdir}/kde4/defaulttools.so
%attr(755,root,root) %{_libdir}/kde4/formulashape.so
%attr(755,root,root) %{_libdir}/kde4/kodocinfopropspage.so
%attr(755,root,root) %{_libdir}/kde4/kolcmsengine.so
%attr(755,root,root) %{_libdir}/kde4/kopabackgroundtool.so
%attr(755,root,root) %{_libdir}/kde4/koreport_barcodeplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_chartplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_mapsplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_webplugin.so
%attr(755,root,root) %{_libdir}/kde4/musicshape.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_odp.so
%attr(755,root,root) %{_libdir}/kde4/pathshapes.so
%attr(755,root,root) %{_libdir}/kde4/pictureshape.so
%attr(755,root,root) %{_libdir}/kde4/pluginshape.so
%attr(755,root,root) %{_libdir}/kde4/spellcheck.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape.so
%attr(755,root,root) %{_libdir}/kde4/textshape.so
%attr(755,root,root) %{_libdir}/kde4/textvariables.so
%attr(755,root,root) %{_libdir}/kde4/thesaurustool.so
%attr(755,root,root) %{_libdir}/kde4/vectorshape.so
%attr(755,root,root) %{_libdir}/kde4/videoshape.so
%attr(755,root,root) %{_libdir}/kde4/webshape.so
%{_desktopdir}/kde4/calligra.desktop
%{_desktopdir}/kde4/okularApplication_odp.desktop
%{_datadir}/kde4/services/artistictextshape.desktop
%{_datadir}/kde4/services/autocorrect.desktop
%{_datadir}/kde4/services/calligradockers.desktop
%{_datadir}/kde4/services/calligrastageeventactions.desktop
%{_datadir}/kde4/services/calligrastagetoolanimation.desktop
%{_datadir}/kde4/services/calligrathumbnail.desktop
%{_datadir}/kde4/services/changecase.desktop
%{_datadir}/kde4/services/chartshape.desktop
%{_datadir}/kde4/services/commentshape.desktop
%{_datadir}/kde4/services/defaulttools.desktop
%{_datadir}/kde4/services/formulashape.desktop
%{_datadir}/kde4/services/kchartpart.desktop
%{_datadir}/kde4/services/kexirelationdesignshape.desktop
%{_datadir}/kde4/services/kformulapart.desktop
%{_datadir}/kde4/services/kodocinfopropspage.desktop
%{_datadir}/kde4/services/kolcmsengine.desktop
%{_datadir}/kde4/services/kopabackgroundtool.desktop
%{_datadir}/kde4/services/koreport_barcodeplugin.desktop
%{_datadir}/kde4/services/koreport_chartplugin.desktop
%{_datadir}/kde4/services/koreport_mapsplugin.desktop
%{_datadir}/kde4/services/koreport_webplugin.desktop
%{_datadir}/kde4/services/libokularGenerator_odp.desktop
%{_datadir}/kde4/services/musicshape.desktop
%{_datadir}/kde4/services/okularOdp.desktop
%{_datadir}/kde4/services/pathshapes.desktop
%{_datadir}/kde4/services/pictureshape.desktop
%{_datadir}/kde4/services/pluginshape.desktop
%{_datadir}/kde4/services/spellcheck.desktop
%{_datadir}/kde4/services/spreadsheetshape-deferred.desktop
%{_datadir}/kde4/services/spreadsheetshape.desktop
%{_datadir}/kde4/services/textshape.desktop
%{_datadir}/kde4/services/textvariables.desktop
%{_datadir}/kde4/services/thesaurustool.desktop
%{_datadir}/kde4/services/vectorshape.desktop
%{_datadir}/kde4/services/videoshape.desktop
%{_datadir}/kde4/services/webshape.desktop
%{_datadir}/kde4/servicetypes/calligra_application.desktop
%{_datadir}/kde4/servicetypes/calligra_deferred_plugin.desktop
%{_datadir}/kde4/servicetypes/calligradocker.desktop
%{_datadir}/kde4/servicetypes/calligrapart.desktop
%{_datadir}/kde4/servicetypes/filtereffect.desktop
%{_datadir}/kde4/servicetypes/flake*.desktop
%{_datadir}/kde4/servicetypes/inlinetextobject.desktop
%{_datadir}/kde4/servicetypes/kochart.desktop
%{_datadir}/kde4/servicetypes/kofilter*.desktop
%{_datadir}/kde4/servicetypes/koplugin.desktop
%{_datadir}/kde4/servicetypes/koreport_itemplugin.desktop
%{_datadir}/kde4/servicetypes/pigment*.desktop
%{_datadir}/kde4/servicetypes/texteditingplugin.desktop
%{_datadir}/kde4/servicetypes/textvariableplugin.desktop
%{_datadir}/kde4/servicetypes/widgetfactory.desktop
%{_datadir}/apps/calligra
%{_datadir}/apps/formulashape
%{_datadir}/apps/koproperty
%{_datadir}/apps/musicshape
%{_datadir}/mime/packages/msooxml-all.xml
%{_datadir}/color/icc/pigment
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/oxygen/*/*/*
%{_kdedocdir}/en/calligra
%dir %{_datadir}/templates/.source

%files karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%attr(755,root,root) %{_libdir}/libkdeinit4_karbon.so
%attr(755,root,root) %{_libdir}/libkarboncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.10
%attr(755,root,root) %{_libdir}/libkarbonui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarbonui.so.10
%attr(755,root,root) %{_libdir}/kde4/*karbon*.*
%attr(755,root,root) %{_libdir}/kde4/wmfexport.*
%attr(755,root,root) %{_libdir}/kde4/wmfimport.*
%{_desktopdir}/kde4/*karbon.desktop
%{_datadir}/apps/karbon
%{_datadir}/config/karbonrc
%{_datadir}/kde4/services/karbon*
%{_datadir}/kde4/services/ServiceMenus/karbon_konqi.desktop
%{_datadir}/kde4/servicetypes/karbon_module.desktop
%{_datadir}/templates/Illustration.desktop
%{_datadir}/templates/.source/Illustration.*
#{_kdedocdir}/en/karbon/

%files flow
%defattr(644,root,root,755)
%doc flow/AUTHORS flow/CHANGE* flow/NOTES flow/README
%attr(755,root,root) %{_bindir}/calligraflow
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraflow.so
%attr(755,root,root) %{_libdir}/libflowprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflowprivate.so.10
%attr(755,root,root) %{_libdir}/kde4/*flow*.*
%attr(755,root,root) %{_libdir}/kde4/vsdximport.so
%{_desktopdir}/kde4/flow.desktop
%{_datadir}/apps/flow
%{_datadir}/config/flowrc
%{_datadir}/config/flow_stencils.knsrc
%{_datadir}/kde4/services/flow*.desktop
%{_datadir}/kde4/services/ServiceMenus/flow_konqi.desktop
%{_datadir}/kde4/servicetypes/flow_dock.desktop
#{_kdedocdir}/en/flow/

%files kexi
%defattr(644,root,root,755)
%doc kexi/CHANGES kexi/README
%attr(755,root,root) %{_bindir}/kexi*
%attr(755,root,root) %{_libdir}/libkexi*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexi*.so.10
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformdesigner.so.10
%attr(755,root,root) %{_libdir}/kde4/kexidb_sqlite3driver.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_sqlite3_icu.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_*.*
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mdb.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_txt.so
%attr(755,root,root) %{_libdir}/kde4/kexirelationdesignshape.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_containers.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_kexidbwidgets.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_stdwidgets.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_webbrowser.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekexidb.so
%{_datadir}/apps/kexi
%{_desktopdir}/kde4/*kexi.desktop
%{_datadir}/config/kexirc
%{_datadir}/kde4/servicetypes/kexi*.desktop
%{_datadir}/kde4/services/kexi
%{_datadir}/kde4/services/keximigrate_mdb.desktop
%{_datadir}/kde4/services/keximigrate_txt.desktop
%{_datadir}/kde4/services/kexidb_sqlite3driver.desktop
%dir %{_datadir}/kde4/services/kformdesigner
%{_datadir}/kde4/services/kformdesigner/kformdesigner_containers.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_kexidbfactory.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_stdwidgets.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_webbrowser.desktop
%{_kdedocdir}/en/kexi/
# kexi-driver-mysql
%attr(755,root,root) %{_libdir}/kde4/kexidb_mysqldriver.*
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mysql.*
%{_datadir}/kde4/services/kexidb_mysqldriver.desktop
%{_datadir}/kde4/services/keximigrate_mysql.desktop
# kexi-driver-postgresql
%if %{with pqxx}
%attr(755,root,root) %{_libdir}/kde4/kexidb_pqxxsqldriver.*
%attr(755,root,root) %{_libdir}/kde4/keximigrate_pqxx.*
%{_datadir}/kde4/services/kexidb_pqxxsqldriver.desktop
%{_datadir}/kde4/services/keximigrate_pqxx.desktop
%endif
# kexi-driver-sybase
%attr(755,root,root) %{_libdir}/kde4/kexidb_sybasedriver.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_sybase.so
%{_datadir}/kde4/services/kexidb_sybasedriver.desktop
%{_datadir}/kde4/services/keximigrate_sybase.desktop
# kexi-map-form-widget
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_mapbrowser.so
%{_datadir}/kde4/services/kformdesigner/kformdesigner_mapbrowser.desktop
# kexi-spreadsheet-import
%attr(755,root,root) %{_libdir}/kde4/keximigrate_spreadsheet.so
%{_datadir}/kde4/services/keximigrate_spreadsheet.desktop
# kexi-driver-xbase
%attr(755,root,root) %{_libdir}/kde4/kexidb_xbasedriver.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_xbase.so
%{_datadir}/kde4/services/kexidb_xbasedriver.desktop
%{_datadir}/kde4/services/keximigrate_xbase.desktop

%files plan
%defattr(644,root,root,755)
%doc plan/CHANGELOG plan/TODO
%attr(755,root,root) %{_bindir}/calligraplan
%attr(755,root,root) %{_bindir}/calligraplanwork
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraplan.so
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraplanwork.so
%attr(755,root,root) %{_libdir}/libkplatokernel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatokernel.so.10
%attr(755,root,root) %{_libdir}/libkplatomodels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatomodels.so.10
%attr(755,root,root) %{_libdir}/libkplatoui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoui.so.10
%attr(755,root,root) %{_libdir}/libplanprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanprivate.so.10
%attr(755,root,root) %{_libdir}/libplanworkapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanworkapp.so.10
%attr(755,root,root) %{_libdir}/libplanworkfactory.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanworkfactory.so.10
%attr(755,root,root) %{_libdir}/librcps_plan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librcps_plan.so.10
%attr(755,root,root) %{_libdir}/kde4/kplatorcpsscheduler.so
%attr(755,root,root) %{_libdir}/kde4/krossmoduleplan.so
%attr(755,root,root) %{_libdir}/kde4/planicalexport.so
%attr(755,root,root) %{_libdir}/kde4/plankplatoimport.so
%attr(755,root,root) %{_libdir}/kde4/planpart.so
%attr(755,root,root) %{_libdir}/kde4/plantjscheduler.so
%attr(755,root,root) %{_libdir}/kde4/planworkpart.so
%{_desktopdir}/kde4/plan.desktop
%{_desktopdir}/kde4/planwork.desktop
%{_datadir}/apps/plan
%{_datadir}/apps/planwork
%{_datadir}/config.kcfg/plansettings.kcfg
%{_datadir}/config.kcfg/planworksettings.kcfg
%{_datadir}/config/planrc
%{_datadir}/config/planworkrc
%{_datadir}/kde4/services/krossmoduleplan.desktop
%{_datadir}/kde4/services/plan*.desktop
%{_datadir}/kde4/servicetypes/plan_schedulerplugin.desktop

%files stage
%defattr(644,root,root,755)
%doc stage/AUTHORS stage/CHANGES
%attr(755,root,root) %{_bindir}/calligrastage
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrastage.so
%attr(755,root,root) %{_libdir}/libcalligrastageprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrastageprivate.so.10
%attr(755,root,root) %{_libdir}/kde4/Filterkpr2odf.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_*.so
%attr(755,root,root) %{_libdir}/kde4/kpr_shapeanimation_*.so
%attr(755,root,root) %{_libdir}/kde4/kprvariables.so
%attr(755,root,root) %{_libdir}/kde4/powerpointimport.so
%attr(755,root,root) %{_libdir}/kde4/pptximport.so
%attr(755,root,root) %{_libdir}/kde4/*stage*.so
%{_desktopdir}/kde4/*stage.desktop
%{_datadir}/apps/stage
%{_datadir}/config/stagerc
%{_datadir}/kde4/services/Filterkpr2odf.desktop
%{_datadir}/kde4/services/kpr*.desktop
%{_datadir}/kde4/services/ServiceMenus/kpresenter_konqi.desktop
%{_datadir}/kde4/services/stagepart.desktop
%{_datadir}/kde4/servicetypes/kpr*.desktop
%{_datadir}/kde4/servicetypes/presentationeventaction.desktop
%{_datadir}/kde4/servicetypes/scripteventaction.desktop
%{_datadir}/templates/Presentation.desktop
%{_datadir}/templates/.source/Presentation.*
%{_kdedocdir}/en/stage/

%files krita
%defattr(644,root,root,755)
%doc krita/AUTHORS krita/ChangeLog krita/README
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_libdir}/libkdeinit4_krita.so
%attr(755,root,root) %{_libdir}/libkrita*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrita*.so.10
%attr(755,root,root) %{_libdir}/kde4/*krita*.so
%{_desktopdir}/kde4/*krita*.desktop
%{_datadir}/apps/color-schemes/Krita*.colors
%{_datadir}/apps/krita
%{_datadir}/apps/kritaplugins
%{_datadir}/color/icc/krita
%{_datadir}/config/krita*.knsrc
%{_datadir}/config/kritarc
%{_datadir}/kde4/services/krita*.desktop
%{_datadir}/kde4/services/ServiceMenus/krita_konqi.desktop
%{_datadir}/kde4/servicetypes/krita*.desktop
%{_datadir}/mime/packages/krita_ora.xml

%files sheets
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligrasheets
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrasheets.so
%attr(755,root,root) %{_libdir}/libcalligrasheetscommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrasheetscommon.so.10
%attr(755,root,root) %{_libdir}/libcalligrasheetsodf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrasheetsodf.so.10
%attr(755,root,root) %{_libdir}/kde4/applixspreadimport.so
%attr(755,root,root) %{_libdir}/kde4/calligrasheets*.so
%attr(755,root,root) %{_libdir}/kde4/csvexport.so
%attr(755,root,root) %{_libdir}/kde4/csvimport.so
%attr(755,root,root) %{_libdir}/kde4/dbaseimport.so
%attr(755,root,root) %{_libdir}/kde4/excelimporttodoc.so
%attr(755,root,root) %{_libdir}/kde4/gnumericexport.so
%attr(755,root,root) %{_libdir}/kde4/gnumericimport.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekspread.so
%attr(755,root,root) %{_libdir}/kde4/kspread*export.so
%attr(755,root,root) %{_libdir}/kde4/kspread*import.so
%attr(755,root,root) %{_libdir}/kde4/kspread*module.so
%attr(755,root,root) %{_libdir}/kde4/kspread_plugin_tool_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kspreadsolver.so
%attr(755,root,root) %{_libdir}/kde4/opencalcexport.so
%attr(755,root,root) %{_libdir}/kde4/opencalcimport.so
%attr(755,root,root) %{_libdir}/kde4/qproimport.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape-deferred.so
%attr(755,root,root) %{_libdir}/kde4/xlsximport.so
%{_desktopdir}/kde4/sheets.desktop
%{_datadir}/apps/sheets/
%{_datadir}/config.kcfg/sheets.kcfg
%{_datadir}/config/sheetsrc
%{_datadir}/kde4/services/krossmodulekspread.desktop
%{_datadir}/kde4/services/kspread_*_export.desktop
%{_datadir}/kde4/services/kspread_*_import.desktop
%{_datadir}/kde4/services/kspread*module.desktop
%{_datadir}/kde4/services/kspread_plugin_tool_calendar.desktop
%{_datadir}/kde4/services/ServiceMenus/kspread_konqi.desktop
%{_datadir}/kde4/services/sheetspart.desktop
%{_datadir}/kde4/services/spreadsheetshape-deferred.desktop
%{_datadir}/kde4/servicetypes/sheets_plugin.desktop
%{_datadir}/templates/.source/SpreadSheet.*
%{_datadir}/templates/SpreadSheet.desktop
%{_kdedocdir}/en/sheets/

%files words
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligrawords
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrawords.so
%attr(755,root,root) %{_libdir}/libwordsprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwordsprivate.so.10
%attr(755,root,root) %{_libdir}/kde4/applixwordimport.so
%attr(755,root,root) %{_libdir}/kde4/asciiimport.so
%attr(755,root,root) %{_libdir}/kde4/docximport.so
%attr(755,root,root) %{_libdir}/kde4/htmlodf_export.so
%attr(755,root,root) %{_libdir}/kde4/mswordodf_import.so
%attr(755,root,root) %{_libdir}/kde4/rtfimport.so
%attr(755,root,root) %{_libdir}/kde4/wordspart.so
%attr(755,root,root) %{_libdir}/kde4/wpgimport.so
%attr(755,root,root) %{_libdir}/kde4/wpsimport.so
%{_desktopdir}/kde4/words.desktop
%{_datadir}/apps/words
%{_datadir}/config/wordsrc
%{_datadir}/kde4/services/html-odf_export.desktop
%{_datadir}/kde4/services/ServiceMenus/words_konqi.desktop
%{_datadir}/kde4/services/words_*_import.desktop
%{_datadir}/kde4/services/wordspart.desktop
%{_datadir}/templates/.source/TextDocument.*
%{_datadir}/templates/TextDocument.desktop

%files braindump
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/braindump
%attr(755,root,root) %{_libdir}/libbraindumpcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbraindumpcore.so.10
%attr(755,root,root) %{_libdir}/kde4/stateshape.so
%{_desktopdir}/kde4/braindump.desktop
%{_datadir}/apps/braindump
%{_datadir}/apps/stateshape
%{_datadir}/kde4/servicetypes/braindump_extensions.desktop
%{_datadir}/kde4/services/stateshape.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit4_*.so
%{_includedir}/*.h
%{_includedir}/KoTextSoftPageBreak.cpp
%{_includedir}/changetracker
%{_includedir}/kexi
%{_includedir}/sheets
%{_includedir}/stage
%{_includedir}/styles
%{_includedir}/words
%{_datadir}/apps/cmake/modules/FindCalligraLibs.cmake
