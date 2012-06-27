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
# Conditional build:
%bcond_without	pdf		# build without PDF support

%define		_state		stable
%define		orgname		calligra
%define		kdever		4.8.0
%define		qtver		4.8.2

Summary:	Calligra - powerful office suite for KDE
Summary(pl.UTF-8):	Calligra - potężny pakiet biurowy dla KDE
Name:		kde4-calligra
Version:	2.4.2
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}-%{version}/%{orgname}-%{version}.tar.bz2
# Source0-md5:	31b0c44ad4ee27017580c7c2fc8e87a9
URL:		http://www.calligra-suite.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	attica-devel
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
BuildRequires:	libpqxx-devel
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
%if %{with pdf}
BuildRequires:	poppler-Qt-devel >= 0.6
%endif
BuildRequires:	pstoedit
BuildRequires:	python-devel >= 2.2
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	rpm-pythonprov
BuildRequires:	soprano-devel
BuildRequires:	sqlite3-devel >= 3.7.13-2
BuildRequires:	xbase-devel
BuildRequires:	zlib-devel
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
- Braindump - A tool to dump and organize the content of your brain
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
- Braindump - narzędzie do ogranizacji pomysłow
- Kexi - narzędzie do tworzenia baz danych
- Plan - aplikacja do zarządzania projektami

%package devel
Summary:	Calligra - header files
Summary(pl.UTF-8):	Calligra - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

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
Obsoletes:	kde4-koffice-karbon

%description karbon
Karbon is a vector graphics application within Calligra.

%description karbon -l pl.UTF-8
Karbon to aplikacja koffice służąca do rysowania grafiki wektorowej,

%package kchart
Summary:	KOffice - KChart
Summary(pl.UTF-8):	KOffice - KChart
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kchart
KChart is KOffice part for generating diagrams from data, e.g. pie and
bar charts.

%description kchart -l pl.UTF-8
KChart jest aplikacją służącą do generowania wykresów.

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

%package kformula
Summary:	KOffice - kformula
Summary(pl.UTF-8):	KOffice - kformula
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kformula
KFormula is KOffice part for creating formulas, equations, etc...

%description kformula -l pl.UTF-8
KFormula jest aplikacją służącą do tworzenia wzorów, równań itp.

%package kivio
Summary:	KOffice - kivio
Summary(pl.UTF-8):	KOffice - kivio
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kivio
Kivio on the surface is your everyday flowcharting program. Underneath
this skin, however, lies much more. Kivio will offer basic
flowcharting abilities, but with a twist. Objects are scriptable, and
a backend plugin system will offer the ability to make objects do just
about anything. Feed it a directory of C++ header files, or even Java
files, and let it generate a graphical class map for you. Give it a
network and let it explore and map out the network for you. All this
is possible through the scripting/plugin architecture Kivio will
possess.

%description kivio -l pl.UTF-8
Kivio jest programem typu flowcharting. Pod tym pojęciem jednak kryje
się znacznie więcej. Kivio dostarcza najpotrzebniejsze funkcje, ale
wszystkie obiekty można rozszerzać za pomocą języka skryptowego, a
system wtyczek backendowych oferuje możliwość tworzenia obiektów
dotyczących prawie wszystkiego. Kivio można nakarmić katalogiem plików
nagłówkowych C++ lub plików Javy i pozwolić wygenerować graficzną mapę
klas. Po podaniu sieci przejrzy ją i stworzy jej mapę. Wszystko to
jest możliwe poprzez architekturę skryptów i wtyczek Kivio.

%package kplato
Summary:	KOffice - KPlato
Summary(pl.UTF-8):	KOffice - KPlato
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kplato
KPlato is a project management application.

%package kpresenter
Summary:	KOffice - KPresenter
Summary(pl.UTF-8):	KOffice - KPresenter
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kpresenter
KPresenter is a presentation application of the KOffice, similar to MS
PowerPoint in the windows world. You can use it for doing screen
presentations or transparencies.

%description kpresenter -l pl.UTF-8
KPresenter jest aplikacją KOffice do tworzenia prezentacji, podobną do
MS PowerPoint. Możesz użyć jej do tworzenia wizualnych prezentacji.

%package krita
Summary:	KOffice - Krita
Summary(pl.UTF-8):	KOffice - Krita
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description krita
Krita is a painting and image editing application for KOffice. It
supports many color spaces like RGB, grayscale, CMYK, Lab, YCBCR and
LMS, in 8 and 16 bits per channel

%description krita -l pl.UTF-8
Krita jest aplikacją do edycji grafiki bitmapowej. Wspiera różne
przestrzenie barw, jak np. RGB, skala szarości, CMYK, Lab, YCBCR oraz
LMS - zarówno w trybie 8 jak i 16 bitowym na kanał.

%package kspread
Summary:	KOffice - KSpread
Summary(pl.UTF-8):	KOffice - KSpread
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kspread
KSpread is the spread sheet of the KOffice, similar to MS Excel.

%description kspread -l pl.UTF-8
KSpread jest arkuszem kalkulacyjnym, podobnym do MS Excel.

%package kword
Summary:	KOffice - KWord
Summary(pl.UTF-8):	KOffice - KWord
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description kword
KWord is a FrameMaker-like wordprocessor application for KOffice. So
it can be used for DTP, but also for "normal" wordprocessing (like
writing letters, reports, etc.).

%description kword -l pl.UTF-8
KWord jest ramkowym procesorem tekstu. Może być użyty do DTP, ale
również do zwykłej edycji tekstu (jak pisanie listów, raportów, itp.).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	common	-p /sbin/ldconfig
%postun	common	-p /sbin/ldconfig

%post	karbon	-p /sbin/ldconfig
%postun	karbon	-p /sbin/ldconfig

%post	kchart	-p /sbin/ldconfig
%postun	kchart	-p /sbin/ldconfig

%post	kexi	-p /sbin/ldconfig
%postun	kexi	-p /sbin/ldconfig

%post	kformula	-p /sbin/ldconfig
%postun	kformula	-p /sbin/ldconfig

%post	kplato	-p /sbin/ldconfig
%postun	kplato	-p /sbin/ldconfig

%post	kpresenter	-p /sbin/ldconfig
%postun	kpresenter	-p /sbin/ldconfig

%post	krita	-p /sbin/ldconfig
%postun	krita	-p /sbin/ldconfig

%post	kspread	-p /sbin/ldconfig
%postun	kspread	-p /sbin/ldconfig

%post	kword	-p /sbin/ldconfig
%postun	kword	-p /sbin/ldconfig

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligraconverter
%attr(755,root,root) %{_libdir}/libkdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdchart.so.?
%attr(755,root,root) %{_libdir}/libkochart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkochart.so.?
%attr(755,root,root) %{_libdir}/libkopageapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopageapp.so.?
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotext.so.?
%attr(755,root,root) %ghost %{_libdir}/libkoproperty.so.?
%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoreport.so.?
%attr(755,root,root) %{_libdir}/libkoreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowv2.so.?
%attr(755,root,root) %{_libdir}/libkowv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmsooxml.so.?
%attr(755,root,root) %{_libdir}/libmsooxml.so.*.*.*
%attr(755,root,root) %{_libdir}/libkowmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowmf.so.?
%attr(755,root,root) %{_libdir}/libkwmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwmf.so.?
%attr(755,root,root) %{_libdir}/libkwordexportfilters.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
%attr(755,root,root) %ghost %{_libdir}/libkoplugin.so.?
%attr(755,root,root) %{_libdir}/libkoplugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowidgets.so.?
%attr(755,root,root) %{_libdir}/libkowidgets.so.*.*.*
%attr(755,root,root) %{_libdir}/libkarbonui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarbonui.so.?
%attr(755,root,root) %{_libdir}/libkpresenterprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpresenterprivate.so.?
%attr(755,root,root) %{_libdir}/kde4/kofficescan.so
%attr(755,root,root) %{_libdir}/kde4/kofficethumbnail.so
%attr(755,root,root) %{_libdir}/kde4/generickofilter.so
%attr(755,root,root) %{_libdir}/kde4/xslt*port*.so
%attr(755,root,root) %{_libdir}/kde4/kounavailpart.so
%attr(755,root,root) %{_libdir}/kde4/kofficedockers.so
%attr(755,root,root) %{_libdir}/kde4/kolcmsengine.so
%attr(755,root,root) %{_libdir}/kde4/kprvariables.so
%attr(755,root,root) %{_libdir}/kde4/koreport_barcodeplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_chartplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_shapeplugin.so
#%attr(755,root,root) %{_libdir}/kde4/vectorshape.so
%attr(755,root,root) %{_libdir}/kde4/videoshape.so
%{_datadir}/apps/koffice
%{_datadir}/kde4/services/kofficethumbnail.desktop
%{_datadir}/kde4/services/kofficedockers.desktop
%{_datadir}/kde4/services/kounavail.desktop
%{_datadir}/kde4/services/xslt_*.desktop
%{_datadir}/kde4/services/generic_filter.desktop
%{_datadir}/kde4/services/kolcmsengine.desktop
%{_datadir}/kde4/services/kprvariables.desktop
#%{_datadir}/kde4/services/vectorshape.desktop
%{_datadir}/kde4/services/videoshape.desktop
%{_datadir}/kde4/services/koreport_barcodeplugin.desktop
%{_datadir}/kde4/services/koreport_chartplugin.desktop
%{_datadir}/kde4/services/koreport_shapeplugin.desktop
%{_datadir}/mime/packages/msooxml-all.xml
%{_datadir}/kde4/servicetypes/*
%dir %{_datadir}/templates/.source
%{_desktopdir}/kde4/koffice.desktop
%{_iconsdir}/oxygen/*/actions/*.png
%exclude %{_iconsdir}/oxygen/scalable
%{_kdedocdir}/en/koffice
%{_datadir}/color/icc/pigment
#
# Files i dunno what to do with
#
%attr(755,root,root) %{_libdir}/kde4/artistictextshape.so
%attr(755,root,root) %{_libdir}/kde4/autocorrect.so
%attr(755,root,root) %{_libdir}/kde4/changecase.so
%attr(755,root,root) %{_libdir}/kde4/defaulttools.so
%attr(755,root,root) %{_libdir}/kde4/divineproportionshape.so
%attr(755,root,root) %{_libdir}/kde4/kopabackgroundtool.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekplato.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekspread.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekword.so
%attr(755,root,root) %{_libdir}/kde4/kspreadsolver.so
%attr(755,root,root) %{_libdir}/kde4/Filterkpr2odf.so
%attr(755,root,root) %{_libdir}/kde4/applixspreadimport.so
%attr(755,root,root) %{_libdir}/kde4/csvexport.so
%attr(755,root,root) %{_libdir}/kde4/csvimport.so
%attr(755,root,root) %{_libdir}/kde4/dbaseimport.so
%attr(755,root,root) %{_libdir}/kde4/gnumericexport.so
%attr(755,root,root) %{_libdir}/kde4/gnumericimport.so
%attr(755,root,root) %{_libdir}/kde4/opencalcexport.so
%attr(755,root,root) %{_libdir}/kde4/opencalcimport.so
%attr(755,root,root) %{_libdir}/kde4/qproimport.so
%attr(755,root,root) %{_libdir}/kde4/wpexport.so
%attr(755,root,root) %{_libdir}/kde4/wpimport.so
%attr(755,root,root) %{_libdir}/kde4/wpgimport.so
%attr(755,root,root) %{_libdir}/kde4/musicshape.so
%attr(755,root,root) %{_libdir}/kde4/pathshapes.so
%attr(755,root,root) %{_libdir}/kde4/pictureshape.so
%attr(755,root,root) %{_libdir}/kde4/spellcheck.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape.so
%attr(755,root,root) %{_libdir}/kde4/textshape.so
%attr(755,root,root) %{_libdir}/kde4/textvariables.so
%attr(755,root,root) %{_libdir}/kde4/commentshape.so
%attr(755,root,root) %{_libdir}/kde4/kodocinfopropspage.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_odp.so
%attr(755,root,root) %{_libdir}/kde4/pluginshape.so
%attr(755,root,root) %ghost %{_libdir}/libkokross.so.?
%attr(755,root,root) %{_libdir}/libkokross.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodf.so.?
%attr(755,root,root) %{_libdir}/libkoodf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkomain.so.?
%attr(755,root,root) %{_libdir}/libkomain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflake.so.?
%attr(755,root,root) %{_libdir}/libflake.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigmentcms.so.?
%attr(755,root,root) %{_libdir}/libpigmentcms.so.*.*.*
%{_datadir}/kde4/services/Filterkpr2odf.desktop
%{_datadir}/kde4/services/artistictextshape.desktop
%{_datadir}/kde4/services/autocorrect.desktop
%{_datadir}/kde4/services/changecase.desktop
%{_datadir}/kde4/services/defaulttools.desktop
%{_datadir}/kde4/services/divineproportionshape.desktop
%{_datadir}/kde4/services/kopabackgroundtool.desktop
%{_datadir}/kde4/services/krossmodulekplato.desktop
%{_datadir}/kde4/services/krossmodulekspread.desktop
%{_datadir}/kde4/services/krossmodulekword.desktop
%{_datadir}/kde4/services/musicshape.desktop
%{_datadir}/kde4/services/pathshapes.desktop
%{_datadir}/kde4/services/pictureshape.desktop
%{_datadir}/kde4/services/spellcheck.desktop
%{_datadir}/kde4/services/textshape.desktop
%{_datadir}/kde4/services/textvariables.desktop
%{_datadir}/kde4/services/commentshape.desktop
%{_datadir}/kde4/services/html-odf_export.desktop
%{_datadir}/kde4/services/kodocinfopropspage.desktop
%{_datadir}/kde4/services/libokularGenerator_odp.desktop
%{_datadir}/kde4/services/okularOdp.desktop
%{_datadir}/kde4/services/pluginshape.desktop
%{_desktopdir}/kde4/okularApplication_odp.desktop
# these libs actually need to be here, to prevent LOOPS
%attr(755,root,root) %{_libdir}/libkarboncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.?
%attr(755,root,root) %ghost %{_libdir}/libkritaimage.so.?
%attr(755,root,root) %{_libdir}/libkritaimage.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwordprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwordprivate.so.?
%attr(755,root,root) %ghost %{_libdir}/libkritaui.so.?
%attr(755,root,root) %{_libdir}/libkritaui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspreadcommon.so.?
%attr(755,root,root) %{_libdir}/libkspreadcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatokernel.so.?
%attr(755,root,root) %{_libdir}/libkplatokernel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatomodels.so.?
%attr(755,root,root) %{_libdir}/libkplatomodels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoprivate.so.?
%attr(755,root,root) %{_libdir}/libkplatoprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoui.so.?
%attr(755,root,root) %{_libdir}/libkplatoui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspreadodf.so.?
%attr(755,root,root) %{_libdir}/libkspreadodf.so.*.*.*

%files karbon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karbon
%attr(755,root,root) %{_libdir}/libkdeinit4_karbon.so
%attr(755,root,root) %{_libdir}/kde4/*karbon*.so
%{_datadir}/apps/karbon
%{_datadir}/config/karbonrc
%{_datadir}/kde4/services/karbon*
%{_datadir}/templates/.source/Illustration.karbon
%{_datadir}/templates/Illustration.desktop
%{_desktopdir}/kde4/karbon.desktop
%{_datadir}/kde4/services/ServiceMenus/karbon_konqi.desktop
%{_kdedocdir}/en/karbon

%files kchart
%defattr(644,root,root,755)
#%attr(755,root,root) %ghost %{_libdir}/kchartcommon.so.?
#%attr(755,root,root) %{_libdir}/kchartcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchartshapelib.so.?
%attr(755,root,root) %{_libdir}/libchartshapelib.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/kchart*.so
%attr(755,root,root) %{_libdir}/kde4/chartshape.so
#%{_datadir}/apps/kchart
%{_datadir}/kde4/services/kchart*.desktop
%{_datadir}/kde4/services/chartshape.desktop
%{_datadir}/kde4/services/ServiceMenus/kchart_konqi.desktop
#%{_iconsdir}/hicolor/*/apps/kchart.png
#%{_kdedocdir}/en/kchart

%files kexi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kexi
%attr(755,root,root) %ghost %{_libdir}/libkexicore.so.?
%attr(755,root,root) %{_libdir}/libkexicore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexidatatable.so.?
%attr(755,root,root) %{_libdir}/libkexidatatable.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexidb.so.?
%attr(755,root,root) %{_libdir}/libkexidb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiextendedwidgets.so.?
%attr(755,root,root) %{_libdir}/libkexiextendedwidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiformutils.so.?
%attr(755,root,root) %{_libdir}/libkexiformutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiguiutils.so.?
%attr(755,root,root) %{_libdir}/libkexiguiutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeximain.so.?
%attr(755,root,root) %{_libdir}/libkeximain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeximigrate.so.?
%attr(755,root,root) %{_libdir}/libkeximigrate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexirelationsview.so.?
%attr(755,root,root) %{_libdir}/libkexirelationsview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexiutils.so.?
%attr(755,root,root) %{_libdir}/libkexiutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformdesigner.so.?
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kexidb_mysqldriver.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_sqlite3driver.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_xbasedriver.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_csv_importexport.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_form.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_migration.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_query.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_report.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_script.so
%attr(755,root,root) %{_libdir}/kde4/kexihandler_table.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_kspread.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mdb.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mysql.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_txt.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_xbase.so
%attr(755,root,root) %{_libdir}/kde4/kexirelationdesignshape.so
%attr(755,root,root) %{_libdir}/kde4/kexidb_sybasedriver.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_sybase.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_containers.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_kexidbwidgets.so
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_stdwidgets.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulekexidb.so
%{_desktopdir}/kde4/kexi.desktop
%{_datadir}/apps/kexi
%{_datadir}/config/kexirc
%dir %{_datadir}/kde4/services/kexi
%{_datadir}/kde4/services/kexi/kexicsv_importexporthandler.desktop
%{_datadir}/kde4/services/kexi/kexiformhandler.desktop
%{_datadir}/kde4/services/kexi/keximigrationhandler.desktop
%{_datadir}/kde4/services/kexi/kexiqueryhandler.desktop
%{_datadir}/kde4/services/kexi/kexireporthandler.desktop
%{_datadir}/kde4/services/kexi/kexiscripthandler.desktop
%{_datadir}/kde4/services/kexi/kexitablehandler.desktop
%{_datadir}/kde4/services/kexidb_mysqldriver.desktop
%{_datadir}/kde4/services/kexidb_sqlite3driver.desktop
%{_datadir}/kde4/services/kexidb_xbasedriver.desktop
%{_datadir}/kde4/services/keximigrate_kspread.desktop
%{_datadir}/kde4/services/keximigrate_mdb.desktop
%{_datadir}/kde4/services/keximigrate_mysql.desktop
%{_datadir}/kde4/services/keximigrate_txt.desktop
%{_datadir}/kde4/services/keximigrate_xbase.desktop
%{_datadir}/kde4/services/kexirelationdesignshape.desktop
%{_datadir}/kde4/services/kexidb_sybasedriver.desktop
%{_datadir}/kde4/services/keximigrate_sybase.desktop
%dir %{_datadir}/kde4/services/kformdesigner
%{_datadir}/kde4/services/kformdesigner/kformdesigner_containers.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_kexidbfactory.desktop
%{_datadir}/kde4/services/kformdesigner/kformdesigner_stdwidgets.desktop
%{_kdedocdir}/en/kexi

%files kformula
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_bindir}/kformula
#%%attr(755,root,root) %{_libdir}/libkdeinit_kformula.so
%attr(755,root,root) %ghost %{_libdir}/libkformulalib.so.?
%attr(755,root,root) %{_libdir}/libkformulalib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformulaprivate.so.?
%attr(755,root,root) %{_libdir}/libkformulaprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/formulashape.so
%attr(755,root,root) %{_libdir}/kde4/excelimporttodoc.so
#%%attr(755,root,root) %{_libdir}/kde4/kformulapart.so
%attr(755,root,root) %{_libdir}/kde4/icalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/xlsximport.so
%attr(755,root,root) %{_libdir}/kde4/paragraphtool.so
#%%{_desktopdir}/kde4/kformula.desktop
%{_datadir}/kde4/services/ServiceMenus/kformula_konqi.desktop
%{_datadir}/kde4/services/formulashape.desktop
#%%{_datadir}/kde4/services/kformulapart.desktop
%{_datadir}/kde4/services/paragraphtool.desktop
%{_datadir}/apps/formulashape
#%%{_datadir}/apps/kformula
%{_kdedocdir}/en/kformula

%files kivio
%defattr(644,root,root,755)
%{_datadir}/kde4/services/ServiceMenus/kivio_konqi.desktop

%files kplato
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplato
%attr(755,root,root) %{_bindir}/kplatowork
%attr(755,root,root) %{_libdir}/libkdeinit4_kplatowork.so
%attr(755,root,root) %ghost %{_libdir}/libkplatoworkapp.so.?
%attr(755,root,root) %{_libdir}/libkplatoworkapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoworkfactory.so.?
%attr(755,root,root) %{_libdir}/libkplatoworkfactory.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kplato.so
%attr(755,root,root) %{_libdir}/kde4/kplatopart.so
%attr(755,root,root) %{_libdir}/kde4/kplatoworkpart.so
%{_desktopdir}/kde4/kplatowork.desktop
%{_datadir}/apps/kplato
%{_datadir}/apps/kplatowork
%{_datadir}/kde4/services/kplatopart.desktop
%{_datadir}/kde4/services/kplato_icalendar_export.desktop
%{_datadir}/kde4/services/kplatoworkpart.desktop
%{_desktopdir}/kde4/kplato.desktop
%{_datadir}/config/kplatorc
%{_datadir}/config.kcfg/kplatosettings.kcfg
%{_datadir}/config/kplatoworkrc
%{_iconsdir}/hicolor/*/apps/kplato.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-vnd.kde.kplato.png

%files kpresenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpresenter
%attr(755,root,root) %{_libdir}/libkdeinit4_kpresenter.so
%attr(755,root,root) %{_libdir}/kde4/kpresenter*.so
%attr(755,root,root) %{_libdir}/kde4/pptximport.so
%attr(755,root,root) %{_libdir}/kde4/powerpointimport.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_barwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_clockwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_edgewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_iriswipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_matrixwipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_slidewipe.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_fade.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_spacerotation.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_swapeffect.so
%attr(755,root,root) %{_libdir}/kde4/kpr_shapeanimation_example.so
%{_datadir}/apps/kpresenter
%{_datadir}/config/kpresenterrc
%{_datadir}/kde4/services/ServiceMenus/kpresenter_konqi.desktop
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/templates/Presentation.desktop
%{_datadir}/kde4/services/kpresenter*.desktop
%{_datadir}/kde4/services/kpr_pageeffect_barwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_clockwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_edgewipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_iriswipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_matrixwipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_slidewipe.desktop
%{_datadir}/kde4/services/kpr_pageeffect_fade.desktop
%{_datadir}/kde4/services/kpr_pageeffect_spacerotation.desktop
%{_datadir}/kde4/services/kpr_pageeffect_swapeffect.desktop
%{_datadir}/kde4/services/kpr_shapeanimation_example.desktop
%{_desktopdir}/kde4/kpresenter.desktop
%{_iconsdir}/hicolor/*/apps/kpresenter.png
%{_kdedocdir}/en/kpresenter

%files krita
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_libdir}/libkdeinit4_krita.so
%attr(755,root,root) %ghost %{_libdir}/libkritalibbrush.so.?
%attr(755,root,root) %{_libdir}/libkritalibbrush.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkritalibpaintop.so.?
%attr(755,root,root) %{_libdir}/libkritalibpaintop.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkrossmodulekrita.so.?
#%attr(755,root,root) %{_libdir}/libkrossmodulekrita.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/krita_colorspaces_extensions.so
%attr(755,root,root) %{_libdir}/kde4/kritabigbrother.so
%attr(755,root,root) %{_libdir}/kde4/kritablurfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritacolorgenerator.so
%attr(755,root,root) %{_libdir}/kde4/kritacolorrange.so
%attr(755,root,root) %{_libdir}/kde4/kritacolorselectorng.so
%attr(755,root,root) %{_libdir}/kde4/kritacolorsfilters.so
%attr(755,root,root) %{_libdir}/kde4/kritacolorspaceconversion.so
%attr(755,root,root) %{_libdir}/kde4/kritaconvolutionfilters.so
%attr(755,root,root) %{_libdir}/kde4/kritacurvepaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritadefaultdockers.so
%attr(755,root,root) %{_libdir}/kde4/kritadefaultpaintops.so
%attr(755,root,root) %{_libdir}/kde4/kritadefaulttools.so
%attr(755,root,root) %{_libdir}/kde4/kritadeformpaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritadigitalmixer.so
%attr(755,root,root) %{_libdir}/kde4/kritadodgeburn.so
%attr(755,root,root) %{_libdir}/kde4/kritadropshadow.so
%attr(755,root,root) %{_libdir}/kde4/kritadynapaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritaembossfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritaexample.so
%attr(755,root,root) %{_libdir}/kde4/kritaextensioncolorsfilters.so
%attr(755,root,root) %{_libdir}/kde4/kritaextensionsmanager.so
%attr(755,root,root) %{_libdir}/kde4/kritafastcolortransferfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritafilterop.so
%attr(755,root,root) %{_libdir}/kde4/kritagridpaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritahairypaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritahatchingpaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritahistogram.so
%attr(755,root,root) %{_libdir}/kde4/kritaimageenhancement.so
%attr(755,root,root) %{_libdir}/kde4/kritaimagesize.so
#%attr(755,root,root) %{_libdir}/kde4/kritakscolorspacesplugin.so
%attr(755,root,root) %{_libdir}/kde4/kritalayercompose.so
%attr(755,root,root) %{_libdir}/kde4/kritalevelfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritametadataeditor.so
%attr(755,root,root) %{_libdir}/kde4/kritamodifyselection.so
%attr(755,root,root) %{_libdir}/kde4/kritanoisefilter.so
%attr(755,root,root) %{_libdir}/kde4/kritaparticlepaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritapixelizefilter.so
%attr(755,root,root) %{_libdir}/kde4/kritaraindropsfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritarandompickfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritarotateimage.so
%attr(755,root,root) %{_libdir}/kde4/kritaroundcornersfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritarulerassistanttool.so
%attr(755,root,root) %{_libdir}/kde4/kritaselectiontools.so
%attr(755,root,root) %{_libdir}/kde4/kritaseparatechannels.so
%attr(755,root,root) %{_libdir}/kde4/kritashearimage.so
%attr(755,root,root) %{_libdir}/kde4/kritasketchpaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritasmallcolorselector.so
%attr(755,root,root) %{_libdir}/kde4/kritaspecificcolorselector.so
%attr(755,root,root) %{_libdir}/kde4/kritaspraypaintop.so
%attr(755,root,root) %{_libdir}/kde4/kritatogether.so
%attr(755,root,root) %{_libdir}/kde4/kritatonemapping.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolcrop.so
%attr(755,root,root) %{_libdir}/kde4/kritatooldyna.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolgrid.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolperspectivegrid.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolpolygon.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolpolyline.so
%attr(755,root,root) %{_libdir}/kde4/kritatoolstar.so
%attr(755,root,root) %{_libdir}/kde4/kritatooltransform.so
%attr(755,root,root) %{_libdir}/kde4/kritatrianglecolorselector.so
%attr(755,root,root) %{_libdir}/kde4/kritaunsharpfilter.so
%attr(755,root,root) %{_libdir}/kde4/kritawavefilter.so
%attr(755,root,root) %{_libdir}/kde4/krita_raw_import.so
%attr(755,root,root) %{_libdir}/kde4/kritabmpexport.so
%attr(755,root,root) %{_libdir}/kde4/kritabmpimport.so
%attr(755,root,root) %{_libdir}/kde4/kritagifimport.so
%attr(755,root,root) %{_libdir}/kde4/kritajp2export.so
%attr(755,root,root) %{_libdir}/kde4/kritajp2import.so
%attr(755,root,root) %{_libdir}/kde4/kritajpegexport.so
%attr(755,root,root) %{_libdir}/kde4/kritajpegimport.so
%attr(755,root,root) %{_libdir}/kde4/kritaoraexport.so
%attr(755,root,root) %{_libdir}/kde4/kritaoraimport.so
%attr(755,root,root) %{_libdir}/kde4/kritapart.so
%attr(755,root,root) %{_libdir}/kde4/kritapngexport.so
%attr(755,root,root) %{_libdir}/kde4/kritapngimport.so
%attr(755,root,root) %{_libdir}/kde4/kritappmexport.so
%attr(755,root,root) %{_libdir}/kde4/kritappmimport.so
%attr(755,root,root) %{_libdir}/kde4/kritatiffexport.so
%attr(755,root,root) %{_libdir}/kde4/kritatiffimport.so
%attr(755,root,root) %{_libdir}/kde4/kritaxcfimport.so
%if %{with pdf}
%attr(755,root,root) %{_libdir}/kde4/kritapdfimport.so
%{_desktopdir}/kde4/krita_pdf.desktop
%endif
%{_desktopdir}/kde4/krita_raw.desktop
%{_datadir}/kde4/services/ServiceMenus/krita_konqi.desktop
%{_datadir}/apps/krita
%{_datadir}/apps/kritaplugins
%{_desktopdir}/kde4/krita_gif.desktop
%{_desktopdir}/kde4/krita_ppm.desktop
%{_desktopdir}/kde4/krita_xcf.desktop
%{_desktopdir}/kde4/krita.desktop
%{_desktopdir}/kde4/krita_bmp.desktop
%{_desktopdir}/kde4/krita_jp2.desktop
%{_desktopdir}/kde4/krita_jpeg.desktop
%{_desktopdir}/kde4/krita_ora.desktop
%{_desktopdir}/kde4/krita_png.desktop
%{_desktopdir}/kde4/krita_tiff.desktop
%{_datadir}/config/kritarc
%{_datadir}/config/krita.knsrc
%{_datadir}/color/icc/krita
%{_datadir}/kde4/services/krita*.desktop
%{_datadir}/templates/Illustration.desktop
%{_datadir}/mime/packages/krita_ora.xml
%{_iconsdir}/hicolor/*/apps/krita.png

%files kspread
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspread
%attr(755,root,root) %{_libdir}/libkdeinit4_kspread.so
%attr(755,root,root) %{_libdir}/kde4/kspread_plugin_tool_calendar.so
%attr(755,root,root) %{_libdir}/kde4/kspreadbitopsmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadconversionmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreaddatabasemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreaddatetimemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadengineeringmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadfinancialmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadinformationmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadlogicmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadmathmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadreferencemodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadstatisticalmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadtextmodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadtrigonometrymodule.so
%attr(755,root,root) %{_libdir}/kde4/kspreadhtmlexport.so
%attr(755,root,root) %{_libdir}/kde4/kspreadhtmlimport.so
%attr(755,root,root) %{_libdir}/kde4/kspreadlatexexport.so
%attr(755,root,root) %{_libdir}/kde4/kspreadpart.so
%attr(755,root,root) %{_libdir}/kde4/spreadsheetshape.so
%{_datadir}/apps/kspread
%{_desktopdir}/kde4/kspread.desktop
%{_datadir}/kde4/services/ServiceMenus/kspread_konqi.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/kde4/services/kspread*.desktop
%{_datadir}/kde4/services/spreadsheetshape.desktop
%{_datadir}/config/kspreadrc
%{_datadir}/config.kcfg/kspread.kcfg
%{_iconsdir}/hicolor/*/apps/kspread.png
%{_kdedocdir}/en/kspread

%files kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kthesaurus
%attr(755,root,root) %{_bindir}/kword
%attr(755,root,root) %{_libdir}/libkdeinit4_kword.so
%attr(755,root,root) %{_libdir}/libkword*export*.so
%attr(755,root,root) %ghost %{_libdir}/libkwordexportfilters.so.?
%attr(755,root,root) %{_libdir}/libkdeinit4_kthesaurus.so
%attr(755,root,root) %{_libdir}/kde4/abiword*port.so
%attr(755,root,root) %{_libdir}/kde4/docximport.so
%attr(755,root,root) %{_libdir}/kde4/hancomwordimport.so
%attr(755,root,root) %{_libdir}/kde4/applixwordimport.so
%attr(755,root,root) %{_libdir}/kde4/ascii*port.so
%attr(755,root,root) %{_libdir}/kde4/docbookexport.so
%attr(755,root,root) %{_libdir}/kde4/html*port.so
%attr(755,root,root) %{_libdir}/kde4/palmdoc*port.so
%attr(755,root,root) %{_libdir}/kde4/amipro*port.so
%attr(755,root,root) %{_libdir}/kde4/wm*port.so
%attr(755,root,root) %{_libdir}/kde4/rtf*port.so
%attr(755,root,root) %{_libdir}/kde4/thesaurustool.so
%attr(755,root,root) %{_libdir}/kde4/mswordodf_import.so
%attr(755,root,root) %{_libdir}/kde4/kword*.so
%attr(755,root,root) %{_libdir}/kde4/oowriter*port.so
%{_datadir}/apps/kword
%dir %{_datadir}/apps/xsltfilter
%dir %{_datadir}/apps/xsltfilter/export
%dir %{_datadir}/apps/xsltfilter/export/kword
%dir %{_datadir}/apps/xsltfilter/export/kword/xslfo
%{_datadir}/apps/xsltfilter/export/kword/xslfo/*.xsl
%{_datadir}/config/kwordrc
%{_datadir}/kde4/services/ServiceMenus/kword_konqi.desktop
%{_datadir}/kde4/services/kword*.desktop
%{_datadir}/kde4/services/thesaurustool.desktop
# this is the mailmerge service info for qtsqldb and classic
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde4/KThesaurus.desktop
%{_desktopdir}/kde4/kword.desktop
%{_iconsdir}/hicolor/*/apps/kword.png
%{_kdedocdir}/en/thesaurus

%files devel
%defattr(644,root,root,755)
%exclude %{_libdir}/libkdeinit4_*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/KoTextSoftPageBreak.cpp
%{_includedir}/changetracker
%{_includedir}/office
%{_includedir}/sheets
%{_includedir}/stage
%{_includedir}/styles
%{_includedir}/words
%{_datadir}/apps/cmake/modules/FindCalligraLibs.cmake
