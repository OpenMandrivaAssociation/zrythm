Name:          zrythm
Version:       1.0.0
Release:       0.beta.2.1.1.0
Summary:       A highly automated, intuitive, Digital Audio Workstation (DAW)
Group:         Sound/Editors and Converters
License:       GPLv3
URL:           https://www.zrythm.org
Source0:       https://github.com/zrythm/zrythm/archive/v%{version}-beta.2.1.1/%{name}-%{version}-beta.2.1.1.tar.gz

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
BuildRequires: pkgconfig(libcyaml)
BuildRequires: pkgconfig(samplerate)
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
%autosetup -n %{name}-%{version}-beta.2.1.1 -p1

%build
%meson \
       -Drtmidi=enabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Dlsp_dsp=enabled \
       -Dgraphviz=enabled \
       --buildtype=release

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_sysconfdir}/bash_completion.d/zrythm
%{_bindir}/%{name}
%{_bindir}/zrythm_launch
%{_datadir}/applications/%{name}.desktop
%{_datadir}/fonts/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/org.zrythm.Zrythm-mime.xml
%{_mandir}/man1/zrythm.1.*
