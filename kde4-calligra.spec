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
#
# Conditional build:
%bcond_without	pdf		# build without PDF support
%bcond_without	pqxx		# build postgresql driver for kexi

%define		_state		stable
%define		orgname		calligra
%define		kdever		4.10.0
%define		qtver		4.8.2
%define		kdeworkspacever	4.11.0

Summary:	Calligra - powerful office suite for KDE
Summary(pl.UTF-8):	Calligra - potężny pakiet biurowy dla KDE
Name:		kde4-calligra
Version:	2.8.6
Release:	5
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}-%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	fc6d40b7d8df62f6a890457e90aa0779
URL:		http://www.calligra-suite.org/
BuildRequires:	GraphicsMagick-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	OpenColorIO-devel
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
BuildRequires:	kde4-kactivities-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	kde4-libkdcraw-devel >= %{kdever}
BuildRequires:	kde4-libkexiv2-devel >= %{kdever}
BuildRequires:	kde4-libkipi-devel >= %{kdever}
BuildRequires:	kde4-libksane-devel >= %{kdever}
BuildRequires:	kde4-marble-devel >= %{kdever}
BuildRequires:	kde4-okular-devel >= %{kdever}
BuildRequires:	lcms2-devel
BuildRequires:	libetonyek-devel
BuildRequires:	libexif-devel >= 0.6.12
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libodfgen-devel
BuildRequires:	libpng-devel
%{?with_pqxx:BuildRequires:	libpqxx-devel >= 4.0.0}
BuildRequires:	libspnav-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvisio-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
BuildRequires:	libwps-devel
BuildRequires:	libxml2-devel >= 0:2.4.8
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mysql-devel
BuildRequires:	openjpeg2-devel >= 1.3
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
BuildRequires:	docbook-style-xsl
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
- Author - tool for serious writers

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
- Author - aplikacja dla autorów książek

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
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
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
- Author - tool for serious writers

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
- Author - aplikacja dla autorów książek

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

%package author
Summary:	Calligra - Author
Summary(pl.UTF-8):	Calligra - Author
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}

%description author
Author is a writing tool aimed at professional authors and is designed
to support the process of creating a new book from conception through
to its final publication.

%description author -l pl.UTF-8
Author jest narzędziem dla profesjonalnych autorów i jest
zaprojektowany by wspierać proces tworzenia książek od koncepcji po
finalną publikację.

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
	-DKDE4_BUILD_TESTS:BOOL=OFF \
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

%post author
/sbin/ldconfig
%update_desktop_database

%postun author
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
%attr(755,root,root) %ghost %{_libdir}/libRtfReader.so.13
%attr(755,root,root) %{_libdir}/libbasicflakes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbasicflakes.so.13
%attr(755,root,root) %{_libdir}/libcalligradb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligradb.so.13
%attr(755,root,root) %{_libdir}/libflake.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflake.so.13
%attr(755,root,root) %{_libdir}/libcalligrakdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrakdchart.so.13
%attr(755,root,root) %{_libdir}/libcalligrakdgantt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrakdgantt.so.13
%attr(755,root,root) %{_libdir}/libkokross.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkokross.so.13
%attr(755,root,root) %{_libdir}/libkomain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkomain.so.13
%attr(755,root,root) %{_libdir}/libkoodf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodf.so.13
%attr(755,root,root) %{_libdir}/libkopageapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopageapp.so.13
%attr(755,root,root) %{_libdir}/libkoplugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoplugin.so.13
%attr(755,root,root) %{_libdir}/libkoproperty.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoproperty.so.13
%attr(755,root,root) %{_libdir}/libkoreport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoreport.so.13
%attr(755,root,root) %{_libdir}/libkotext.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotext.so.13
%attr(755,root,root) %{_libdir}/libkowidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowidgets.so.13
%attr(755,root,root) %{_libdir}/libkowidgetutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowidgetutils.so.13
%attr(755,root,root) %{_libdir}/libkowv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkowv2.so.9
%attr(755,root,root) %{_libdir}/libkundo2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkundo2.so.13
%attr(755,root,root) %{_libdir}/libpigmentcms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigmentcms.so.13
%attr(755,root,root) %{_libdir}/libkformula.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformula.so.13
%attr(755,root,root) %{_libdir}/libkomsooxml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkomsooxml.so.13
%attr(755,root,root) %{_libdir}/libkoodf2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodf2.so.13
%attr(755,root,root) %{_libdir}/libkoodfreader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkoodfreader.so.13
%attr(755,root,root) %{_libdir}/libkotextlayout.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkotextlayout.so.13
%attr(755,root,root) %{_libdir}/libkovectorimage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkovectorimage.so.13
%attr(755,root,root) %{_libdir}/kde4/calligra_device_spacenavigator.so
%attr(755,root,root) %{_libdir}/kde4/calligradocinfopropspage.so
%attr(755,root,root) %{_libdir}/kde4/calligra_docker_defaults.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_pdf2svg.so
%attr(755,root,root) %{_libdir}/kde4/calligraimagethumbnail.so
%attr(755,root,root) %{_libdir}/kde4/calligra_semanticitem_contact.so
%attr(755,root,root) %{_libdir}/kde4/calligra_semanticitem_event.so
%attr(755,root,root) %{_libdir}/kde4/calligra_semanticitem_location.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_artistictext.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_chart.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_formular.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_music.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_paths.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_picture.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_plugin.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_spreadsheet-deferred.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_spreadsheet.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_text.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_threed.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_vector.so
%attr(755,root,root) %{_libdir}/kde4/calligra_shape_video.so
%attr(755,root,root) %{_libdir}/kde4/calligra_textediting_autocorrect.so
%attr(755,root,root) %{_libdir}/kde4/calligra_textediting_changecase.so
%attr(755,root,root) %{_libdir}/kde4/calligra_textediting_spellcheck.so
%attr(755,root,root) %{_libdir}/kde4/calligra_textediting_thesaurus.so
%attr(755,root,root) %{_libdir}/kde4/calligra_textinlineobject_variables.so
%attr(755,root,root) %{_libdir}/kde4/calligrathumbnail.so
%attr(755,root,root) %{_libdir}/kde4/calligra_tool_basicflakes.so
%attr(755,root,root) %{_libdir}/kde4/calligra_tool_defaults.so
%attr(755,root,root) %{_libdir}/kde4/kolcmsengine.so
%attr(755,root,root) %{_libdir}/kde4/kopabackgroundtool.so
%attr(755,root,root) %{_libdir}/kde4/koreport_barcodeplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_mapsplugin.so
%attr(755,root,root) %{_libdir}/kde4/koreport_webplugin.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_odp.so
%dir %{_libdir}/calligra
%dir %{_libdir}/calligra/imports
%dir %{_libdir}/calligra/imports/org
%{_desktopdir}/kde4/calligra.desktop
%{_desktopdir}/kde4/okularApplication_odp.desktop
%{_datadir}/kde4/services/calligra_device_spacenavigator.desktop
%{_datadir}/kde4/services/calligradocinfopropspage.desktop
%{_datadir}/kde4/services/calligra_docker_defaults.desktop
%{_datadir}/kde4/services/calligra_docker_textdocumentinspection.desktop
%{_datadir}/kde4/services/calligra_filter_pdf2svg.desktop
%{_datadir}/kde4/services/calligra_odg_thumbnail.desktop
%{_datadir}/kde4/services/calligra_semanticitem_contact.desktop
%{_datadir}/kde4/services/calligra_semanticitem_event.desktop
%{_datadir}/kde4/services/calligra_semanticitem_location.desktop
%{_datadir}/kde4/services/calligra_shape_artistictext.desktop
%{_datadir}/kde4/services/calligra_shape_chart.desktop
%{_datadir}/kde4/services/calligra_shape_formular.desktop
%{_datadir}/kde4/services/calligra_shape_music.desktop
%{_datadir}/kde4/services/calligra_shape_paths.desktop
%{_datadir}/kde4/services/calligra_shape_picture.desktop
%{_datadir}/kde4/services/calligra_shape_plugin.desktop
%{_datadir}/kde4/services/calligra_shape_spreadsheet-deferred.desktop
%{_datadir}/kde4/services/calligra_shape_spreadsheet.desktop
%{_datadir}/kde4/services/calligra_shape_text.desktop
%{_datadir}/kde4/services/calligra_shape_threed.desktop
%{_datadir}/kde4/services/calligra_shape_vector.desktop
%{_datadir}/kde4/services/calligra_shape_video.desktop
%{_datadir}/kde4/services/calligrastageeventactions.desktop
%{_datadir}/kde4/services/calligrastagetoolanimation.desktop
%{_datadir}/kde4/services/calligra_textediting_autocorrect.desktop
%{_datadir}/kde4/services/calligra_textediting_changecase.desktop
%{_datadir}/kde4/services/calligra_textediting_spellcheck.desktop
%{_datadir}/kde4/services/calligra_textediting_thesaurus.desktop
%{_datadir}/kde4/services/calligra_textinlineobject_variables.desktop
%{_datadir}/kde4/services/calligra_tool_basicflakes.desktop
%{_datadir}/kde4/services/calligra_tool_defaults.desktop
%dir %{_datadir}/kde4/services/calligra
%{_datadir}/kde4/services/calligra/koreport_barcodeplugin.desktop
%{_datadir}/kde4/services/calligra/koreport_mapsplugin.desktop
%{_datadir}/kde4/services/calligra/koreport_webplugin.desktop
%{_datadir}/kde4/services/kformulapart.desktop
%{_datadir}/kde4/services/kolcmsengine.desktop
%{_datadir}/kde4/services/kopabackgroundtool.desktop
%{_datadir}/kde4/services/libokularGenerator_odp.desktop
%{_datadir}/kde4/services/okularOdp.desktop
%{_datadir}/kde4/servicetypes/calligra_application.desktop
%{_datadir}/kde4/servicetypes/calligradb_driver.desktop
%{_datadir}/kde4/servicetypes/calligra_deferred_plugin.desktop
%{_datadir}/kde4/servicetypes/calligradocker.desktop
%{_datadir}/kde4/servicetypes/calligra_filter.desktop
%{_datadir}/kde4/servicetypes/calligra_part.desktop
%{_datadir}/kde4/servicetypes/calligra_semanticitem.desktop
%{_datadir}/kde4/servicetypes/filtereffect.desktop
%{_datadir}/kde4/servicetypes/flake*.desktop
%{_datadir}/kde4/servicetypes/inlinetextobject.desktop
%{_datadir}/kde4/servicetypes/koreport_itemplugin.desktop
%{_datadir}/kde4/servicetypes/pigment*.desktop
%{_datadir}/kde4/servicetypes/texteditingplugin.desktop
%{_datadir}/kde4/servicetypes/widgetfactory.desktop
%{_datadir}/apps/calligra
%{_datadir}/apps/formulashape
%{_datadir}/apps/koproperty
%{_datadir}/apps/musicshape
%{_datadir}/mime/packages/calligra_svm.xml
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
%attr(755,root,root) %ghost %{_libdir}/libkarboncommon.so.13
%attr(755,root,root) %{_libdir}/libkarbonui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarbonui.so.13
%attr(755,root,root) %{_libdir}/kde4/*karbon*.*
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_eps2svgai.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_wmf2svg.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_xfig2odg.so
%{_desktopdir}/kde4/*karbon.desktop
%{_datadir}/apps/karbon
%{_datadir}/config/karbonrc
%{_datadir}/kde4/services/calligra_filter_eps2svgai.desktop
%{_datadir}/kde4/services/calligra_filter_karbon1x2karbon.desktop
%{_datadir}/kde4/services/calligra_filter_karbon2jpg.desktop
%{_datadir}/kde4/services/calligra_filter_karbon2png.desktop
%{_datadir}/kde4/services/calligra_filter_karbon2svg.desktop
%{_datadir}/kde4/services/calligra_filter_karbon2wmf.desktop
%{_datadir}/kde4/services/calligra_filter_svg2karbon.desktop
%{_datadir}/kde4/services/calligra_filter_svgz2karbon.desktop
%{_datadir}/kde4/services/calligra_filter_wmf2svg.desktop
%{_datadir}/kde4/services/calligra_filter_xfig2odg.desktop
%{_datadir}/kde4/services/karbon*
%{_datadir}/kde4/services/ServiceMenus/karbon_print.desktop
%{_datadir}/kde4/servicetypes/karbon_dock.desktop
%{_datadir}/kde4/servicetypes/karbon_viewplugin.desktop
%{_datadir}/templates/Illustration.desktop
%{_datadir}/templates/.source/Illustration.*
#{_kdedocdir}/en/karbon/

%files flow
%defattr(644,root,root,755)
%doc flow/AUTHORS flow/CHANGE* flow/NOTES flow/README
%attr(755,root,root) %{_bindir}/calligraflow
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraflow.so
%attr(755,root,root) %{_libdir}/libflowprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflowprivate.so.13
%attr(755,root,root) %{_libdir}/kde4/*flow*.*
%{_desktopdir}/kde4/flow.desktop
%{_datadir}/apps/flow
%{_datadir}/config/flowrc
%{_datadir}/config/flow_stencils.knsrc
%{_datadir}/kde4/services/flow*.desktop
%{_datadir}/kde4/services/ServiceMenus/flow_print.desktop
%{_datadir}/kde4/servicetypes/flow_dock.desktop
#{_kdedocdir}/en/flow/

%files kexi
%defattr(644,root,root,755)
%doc kexi/CHANGES kexi/README
%attr(755,root,root) %{_bindir}/kexi*
%attr(755,root,root) %{_libdir}/libkexi*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkexi*.so.13
%attr(755,root,root) %{_libdir}/libkformdesigner.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkformdesigner.so.13
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
%{_kdedocdir}/en/kexi/
# kexi-driver-mysql
%attr(755,root,root) %{_libdir}/kde4/kexidb_mysqldriver.*
%attr(755,root,root) %{_libdir}/kde4/keximigrate_mysql.*
# kexi-driver-postgresql
%if %{with pqxx}
%attr(755,root,root) %{_libdir}/kde4/kexidb_pqxxsqldriver.*
%attr(755,root,root) %{_libdir}/kde4/keximigrate_pqxx.*
%{_datadir}/kde4/services/calligra/kexidb_pqxxsqldriver.desktop
%{_datadir}/kde4/services/calligra/keximigrate_pqxx.desktop
%endif
# kexi-driver-sybase
%attr(755,root,root) %{_libdir}/kde4/kexidb_sybasedriver.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_sybase.so
# kexi-map-form-widget
%attr(755,root,root) %{_libdir}/kde4/kformdesigner_mapbrowser.so
# kexi-spreadsheet-import
%attr(755,root,root) %{_libdir}/kde4/keximigrate_spreadsheet.so
# kexi-driver-xbase
%attr(755,root,root) %{_libdir}/kde4/kexidb_xbasedriver.so
%attr(755,root,root) %{_libdir}/kde4/keximigrate_xbase.so
%{_datadir}/kde4/services/calligra/kexicsv_importexporthandler.desktop
%{_datadir}/kde4/services/calligra/kexidb_mysqldriver.desktop
%{_datadir}/kde4/services/calligra/kexidb_sqlite3driver.desktop
%{_datadir}/kde4/services/calligra/kexidb_sybasedriver.desktop
%{_datadir}/kde4/services/calligra/kexidb_xbasedriver.desktop
%{_datadir}/kde4/services/calligra/kexiformhandler.desktop
%{_datadir}/kde4/services/calligra/keximigrate_mdb.desktop
%{_datadir}/kde4/services/calligra/keximigrate_mysql.desktop
%{_datadir}/kde4/services/calligra/keximigrate_spreadsheet.desktop
%{_datadir}/kde4/services/calligra/keximigrate_sybase.desktop
%{_datadir}/kde4/services/calligra/keximigrate_txt.desktop
%{_datadir}/kde4/services/calligra/keximigrate_xbase.desktop
%{_datadir}/kde4/services/calligra/keximigrationhandler.desktop
%{_datadir}/kde4/services/calligra/kexiqueryhandler.desktop
%{_datadir}/kde4/services/calligra/kexirelationdesignshape.desktop
%{_datadir}/kde4/services/calligra/kexireporthandler.desktop
%{_datadir}/kde4/services/calligra/kexiscripthandler.desktop
%{_datadir}/kde4/services/calligra/kexitablehandler.desktop
%{_datadir}/kde4/services/calligra/kformdesigner_containers.desktop
%{_datadir}/kde4/services/calligra/kformdesigner_kexidbfactory.desktop
%{_datadir}/kde4/services/calligra/kformdesigner_mapbrowser.desktop
%{_datadir}/kde4/services/calligra/kformdesigner_stdwidgets.desktop
%{_datadir}/kde4/services/calligra/kformdesigner_webbrowser.desktop

%files plan
%defattr(644,root,root,755)
%doc plan/CHANGELOG plan/TODO
%attr(755,root,root) %{_bindir}/calligraplan
%attr(755,root,root) %{_bindir}/calligraplanwork
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraplan.so
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraplanwork.so
%attr(755,root,root) %{_libdir}/libkplatokernel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatokernel.so.13
%attr(755,root,root) %{_libdir}/libkplatomodels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatomodels.so.13
%attr(755,root,root) %{_libdir}/libkplatoui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkplatoui.so.13
%attr(755,root,root) %{_libdir}/libplanprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanprivate.so.13
%attr(755,root,root) %{_libdir}/libplanworkapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanworkapp.so.13
%attr(755,root,root) %{_libdir}/libplanworkfactory.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplanworkfactory.so.13
%attr(755,root,root) %{_libdir}/librcps_plan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librcps_plan.so.13
%attr(755,root,root) %{_libdir}/kde4/kplatorcpsscheduler.so
%attr(755,root,root) %{_libdir}/kde4/krossmoduleplan.so
%{_libdir}/kde4/planconvert
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_mpxj2plan.so
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
%{_datadir}/kde4/services/calligra_filter_mpp2plan.desktop
%{_datadir}/kde4/services/calligra_filter_mpx2plan.desktop
%{_datadir}/kde4/services/calligra_filter_planner2plan.desktop
%{_datadir}/kde4/services/krossmoduleplan.desktop
%{_datadir}/kde4/services/plan*.desktop
%{_datadir}/kde4/servicetypes/plan_schedulerplugin.desktop
%{_datadir}/kde4/servicetypes/plan_viewplugin.desktop
%{_datadir}/mime/packages/calligra_planner_mpp.xml

%files stage
%defattr(644,root,root,755)
%doc stage/AUTHORS stage/CHANGES
%attr(755,root,root) %{_bindir}/calligrastage
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrastage.so
%attr(755,root,root) %{_libdir}/libcalligrastageprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrastageprivate.so.13
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_kpr2odp.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_ppt2odp.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_pptx2odp.so
%attr(755,root,root) %{_libdir}/kde4/kpr_pageeffect_*.so
%attr(755,root,root) %{_libdir}/kde4/kpr_shapeanimation_*.so
%attr(755,root,root) %{_libdir}/kde4/kprvariables.so
%attr(755,root,root) %{_libdir}/kde4/*stage*.so
%{_desktopdir}/kde4/*stage.desktop
%{_datadir}/apps/stage
%{_datadir}/config/stagerc
%{_datadir}/kde4/services/calligra_filter_kpr2odp.desktop
%{_datadir}/kde4/services/calligra_filter_ppt2odp.desktop
%{_datadir}/kde4/services/calligra_filter_pptx2odp.desktop
%{_datadir}/kde4/services/kpr*.desktop
%{_datadir}/kde4/services/ServiceMenus/stage_print.desktop
%{_datadir}/kde4/services/stagepart.desktop
%{_datadir}/kde4/services/stage_*_thumbnail.desktop
%{_datadir}/kde4/servicetypes/kpr*.desktop
%{_datadir}/kde4/servicetypes/presentationeventaction.desktop
%{_datadir}/kde4/servicetypes/scripteventaction.desktop
%{_datadir}/templates/Presentation.desktop
%{_datadir}/templates/.source/Presentation.*
%{_kdedocdir}/en/stage/

%files krita
%defattr(644,root,root,755)
%doc krita/AUTHORS krita/ChangeLog krita/README
%attr(755,root,root) %{_bindir}/gmicparser
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_bindir}/kritagemini
%attr(755,root,root) %{_bindir}/kritasketch
%attr(755,root,root) %{_libdir}/libkdeinit4_krita.so
%attr(755,root,root) %{_libdir}/libkrita*.so.*.*.*
%attr(755,root,root) %{_libdir}/libkritasketchlib.so
%attr(755,root,root) %ghost %{_libdir}/libkrita*.so.13
%attr(755,root,root) %{_libdir}/kde4/*krita*.so
%{_libdir}/calligra/imports/org/krita
%{_desktopdir}/kde4/*krita*.desktop
%{_datadir}/appdata/krita.appdata.xml
%{_datadir}/apps/color-schemes/Krita*.colors
%{_datadir}/apps/krita
%{_datadir}/apps/kritagemini
%{_datadir}/apps/kritaplugins
%{_datadir}/apps/kritasketch
%{_datadir}/color/icc/krita
%{_datadir}/config/krita*rc
%{_datadir}/kde4/services/krita*.desktop
%{_datadir}/kde4/services/ServiceMenus/krita_print.desktop
%{_datadir}/kde4/servicetypes/krita*.desktop
%{_datadir}/mime/packages/krita_ora.xml
%{_datadir}/mime/packages/krita.xml

%files sheets
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligrasheets
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrasheets.so
%attr(755,root,root) %{_libdir}/libcalligrasheetscommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrasheetscommon.so.13
%attr(755,root,root) %{_libdir}/libcalligrasheetsodf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcalligrasheetsodf.so.13
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_applixspread2kspread.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_csv2sheets.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_dbase2kspread.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_gnumeric2sheets.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_kspread2tex.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_opencalc2sheets.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_qpro2sheets.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_sheets2csv.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_sheets2gnumeric.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_sheets2html.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_sheets2opencalc.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_xls2ods.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_xlsx2ods.so
%attr(755,root,root) %{_libdir}/kde4/calligrasheets*.so
%attr(755,root,root) %{_libdir}/kde4/krossmodulesheets.so
%attr(755,root,root) %{_libdir}/kde4/kspread*module.so
%attr(755,root,root) %{_libdir}/kde4/kspread_plugin_tool_calendar.so
%attr(755,root,root) %{_libdir}/kde4/sheetspivottables.so
%attr(755,root,root) %{_libdir}/kde4/sheetssolver.so
%{_desktopdir}/kde4/sheets.desktop
%{_datadir}/apps/sheets/
%{_datadir}/config.kcfg/sheets.kcfg
%{_datadir}/config/sheetsrc
%{_datadir}/kde4/services/calligra_filter_applixspread2kspread.desktop
%{_datadir}/kde4/services/calligra_filter_csv2sheets.desktop
%{_datadir}/kde4/services/calligra_filter_dbase2kspread.desktop
%{_datadir}/kde4/services/calligra_filter_gnumeric2sheets.desktop
%{_datadir}/kde4/services/calligra_filter_kspread2tex.desktop
%{_datadir}/kde4/services/calligra_filter_opencalc2sheets.desktop
%{_datadir}/kde4/services/calligra_filter_qpro2sheets.desktop
%{_datadir}/kde4/services/calligra_filter_sheets2csv.desktop
%{_datadir}/kde4/services/calligra_filter_sheets2gnumeric.desktop
%{_datadir}/kde4/services/calligra_filter_sheets2html.desktop
%{_datadir}/kde4/services/calligra_filter_sheets2opencalc.desktop
%{_datadir}/kde4/services/calligra_filter_xls2ods.desktop
%{_datadir}/kde4/services/calligra_filter_xlsx2ods.desktop
%{_datadir}/kde4/services/krossmodulesheets.desktop
%{_datadir}/kde4/services/kspread*module.desktop
%{_datadir}/kde4/services/kspread_plugin_tool_calendar.desktop
%{_datadir}/kde4/services/ServiceMenus/sheets_print.desktop
%{_datadir}/kde4/services/sheetspart.desktop
%{_datadir}/kde4/services/sheetspivottables.desktop
%{_datadir}/kde4/services/sheetsscripting.desktop
%{_datadir}/kde4/services/sheetssolver.desktop
%{_datadir}/kde4/services/sheets_*_thumbnail.desktop
%{_datadir}/kde4/servicetypes/sheets_plugin.desktop
%{_datadir}/kde4/servicetypes/sheets_viewplugin.desktop
%{_datadir}/templates/.source/SpreadSheet.*
%{_datadir}/templates/SpreadSheet.desktop
%{_kdedocdir}/en/sheets/

%files words
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligrawords
%attr(755,root,root) %{_libdir}/libkdeinit4_calligrawords.so
%attr(755,root,root) %{_libdir}/libkordf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkordf.so.13
%attr(755,root,root) %{_libdir}/libwordsprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwordsprivate.so.13
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_applixword2odt.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_ascii2words.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_doc2odt.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_docx2odt.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_html2ods.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_odt2ascii.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_odt2epub2.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_odt2html.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_odt2mobi.so
%attr(755,root,root) %{_libdir}/kde4/calligra_filter_rtf2odt.so
%attr(755,root,root) %{_libdir}/kde4/wordspart.so
%{_datadir}/apps/words
%{_datadir}/config/wordsrc
%{_datadir}/kde4/services/calligra_filter_applixword2odt.desktop
%{_datadir}/kde4/services/calligra_filter_ascii2words.desktop
%{_datadir}/kde4/services/calligra_filter_doc2odt.desktop
%{_datadir}/kde4/services/calligra_filter_docx2odt.desktop
%{_datadir}/kde4/services/calligra_filter_html2ods.desktop
%{_datadir}/kde4/services/calligra_filter_odt2ascii.desktop
%{_datadir}/kde4/services/calligra_filter_odt2epub2.desktop
%{_datadir}/kde4/services/calligra_filter_odt2html.desktop
%{_datadir}/kde4/services/calligra_filter_odt2mobi.desktop
%{_datadir}/kde4/services/calligra_filter_rtf2odt.desktop
%{_datadir}/kde4/services/ServiceMenus/words_print.desktop
%{_datadir}/kde4/services/wordspart.desktop
%{_datadir}/kde4/services/words_*_thumbnail.desktop
%{_datadir}/templates/.source/TextDocument.*
%{_datadir}/templates/TextDocument.desktop
%{_desktopdir}/kde4/calligrawords_ascii.desktop
%{_desktopdir}/kde4/words.desktop

%files author
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calligraauthor
%attr(755,root,root) %{_libdir}/libkdeinit4_calligraauthor.so
%attr(755,root,root) %{_libdir}/kde4/authorpart.so
%{_desktopdir}/kde4/author.desktop
%{_datadir}/apps/author
%{_datadir}/config/authorrc
%{_datadir}/kde4/services/authorpart.desktop

%files braindump
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/braindump
%attr(755,root,root) %{_libdir}/libbraindumpcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbraindumpcore.so.13
%attr(755,root,root) %{_libdir}/kde4/braindump_shape_state.so
%attr(755,root,root) %{_libdir}/kde4/braindump_shape_web.so
%{_desktopdir}/kde4/braindump.desktop
%{_datadir}/apps/braindump
%{_datadir}/apps/stateshape
%{_datadir}/kde4/services/braindump_shape_state.desktop
%{_datadir}/kde4/services/braindump_shape_web.desktop
%{_datadir}/kde4/servicetypes/braindump_extensions.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit4_*.so
%exclude %{_libdir}/libkritasketchlib.so
%{_includedir}/*.h
%{_includedir}/calligra
%{_includedir}/kexi
%{_includedir}/krita
%{_includedir}/sheets
%{_includedir}/stage
%{_includedir}/words
%{_datadir}/apps/cmake/modules/FindCalligraLibs.cmake
