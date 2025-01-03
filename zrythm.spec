Name:          zrythm
Version:       1.0.0
Release:       2
Summary:       A highly automated, intuitive, Digital Audio Workstation (DAW)
Group:         Sound/Editors and Converters
License:       GPLv3
URL:           https://www.zrythm.org
Source0:       https://github.com/zrythm/zrythm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: appstream
BuildRequires: appstream-util
BuildRequires: git
BuildRequires: gettext
BuildRequires: python
BuildRequires: sed
BuildRequires: sassc
BuildRequires: backstrace-devel
BuildRequires: boost-devel
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: graphviz-devel
#BuildRequires: carla-devel
BuildRequires: pkgconfig(carla-host-plugin)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(audec)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libchromaprint)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libfl)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libsass)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(yyjson)
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(reproc)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libxdot)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(pypandoc)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lsp-dsp-lib)
BuildRequires: pkgconfig(vamp)
BuildRequires: libxml2-utils
BuildRequires: jq-devel
BuildRequires: help2man
BuildRequires: texi2html
BuildRequires: xdg-utils
BuildRequires: meson
Requires:      carla
Requires:      ladspa
Requires:      lilv
Requires:      lv2
Requires:      fftw
Requires:      jackit
Requires:      %{_lib}lsp-dsp-lib

%description
Zrythm is a native GNU/Linux application built with
the GTK+3 toolkit and using the JACK Connection Kit for audio I/O.
Zrythm can automate plugin parameters using built in LFOs and envelopes
and is designed to be intuitive to use.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson \
       -Drtmidi=disabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Dlsp_dsp=disabled \
       -Dgraphviz=enabled \
       -Dbuild_plugins_with_static_libs=false \
       --buildtype=release

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/%{name}*
%{_libdir}/zrythm/carla/
%{_libdir}/zrythm/lv2
%{_datadir}/applications/org.zrythm.Zrythm.desktop
%{_datadir}/fonts/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/scalable/apps/org.zrythm.Zrythm.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/org.zrythm.Zrythm-mime.xml
%{_datadir}/bash-completion/completions/zrythm
%{_datadir}/fish/vendor_completions.d/zrythm.fish
%{_datadir}/metainfo/org.zrythm.Zrythm.appdata.xml
%{_mandir}/man1/zrythm.1.*
