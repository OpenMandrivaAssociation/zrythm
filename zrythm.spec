Summary:		A highly automated, intuitive, Digital Audio Workstation (DAW)
Name:	zrythm
Version:		1.0.0
Release:		7
License:		AGPL-3.0-or-later
Group:	Sound/Editors and Converters
Url:		https://www.zrythm.org
Source0:	https://github.com/zrythm/zrythm/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:	zrythm-1.0.0-fix-rtmidi-include-path.patch
Patch1:	zrythm-1.0.0-fix-env-shebangs.patch
BuildRequires: appstream
BuildRequires: appstream-util
BuildRequires: chrpath
BuildRequires: git
BuildRequires: gettext
BuildRequires: help2man
BuildRequires: libxml2-utils
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja
BuildRequires: python
BuildRequires: sed
BuildRequires: sassc
BuildRequires: texi2html
BuildRequires: xdg-utils
BuildRequires: atomic-devel
BuildRequires: backstrace-devel
BuildRequires: boost-devel
#BuildRequires: carla-devel
BuildRequires: ffmpeg-devel
BuildRequires: jq-devel
BuildRequires: ladspa-devel
BuildRequires: graphviz-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(audec)
BuildRequires: pkgconfig(carla-host-plugin)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libchromaprint)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(libfl)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libsass)
BuildRequires: pkgconfig(libxdot)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lsp-dsp-lib)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(reproc)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(sndfile)
# In Extra ATM
#BuildRequires: pkgconfig(soundio)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(vamp)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(yyjson)
BuildRequires: pkgconfig(x11)
BuildRequires: python%{pyver}dist(sphinx)
BuildRequires: python%{pyver}dist(pypandoc)
Requires:	carla
Requires:	ladspa
Requires:	lilv
Requires:	lv2
Requires:	fftw
Requires:	jackit
Requires:	%{_lib}lsp-dsp-lib

%description
Zrythm is a native GNU/Linux application built with the GTK+3 toolkit and
using the JACK Connection Kit for audio I/O.
Zrythm can automate plugin parameters using built in LFOs and envelopes
and is designed to be intuitive to use.

%files -f %{name}.lang
%license COPYING
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/%{name}*
%{_libdir}/%{name}/carla/
%{_libdir}/%{name}/lv2
%{_datadir}/applications/org.%{name}.Zrythm.desktop
%{_datadir}/fonts/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/scalable/apps/org.%{name}.Zrythm.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/org.%{name}.Zrythm-mime.xml
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/metainfo/org.%{name}.Zrythm.appdata.xml
%{_mandir}/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1


%build
%meson \
	-Drtmidi=enabled \
	-Drtaudio=enabled \
	-Dsdl=enabled \
	-Dlsp_dsp=enabled \
	-Dopus=true \
	-Dgraphviz=disabled \
	-Dcheck_updates=false \
	-Dbuild_plugins_with_static_libs=false \
	--buildtype=release

%meson_build


%install
%meson_install

# Fix rogue rpath
chrpath -d %{buildroot}%{_bindir}/%{name}

# Fix perms
chmod 0755 %{buildroot}%{_bindir}/%{name}*

%find_lang %{name}
