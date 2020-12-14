Name:          zrythm
Version:       0.8.982
Release:       1
Summary:       A highly automated, intuitive, Digital Audio Workstation (DAW)
Group:         Sound/Editors and Converters
License:       GPLv3
URL:           https://www.zrythm.org
Source0:       https://github.com/zrythm/zrythm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: git
BuildRequires: gettext
BuildRequires: python
BuildRequires: sed
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: graphviz-devel
BuildRequires: pkgconfig(carla-utils)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(audec)
BuildRequires: pkgconfig(libchromaprint)
BuildRequires: pkgconfig(libgtop-2.0)
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
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libxdot)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(pypandoc)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lsp-dsp-lib)
BuildRequires: help2man
BuildRequires: texi2html
BuildRequires: xdg-utils
BuildRequires: meson
Requires:      ladspa
Requires:      lilv
Requires:      lv2
Requires:      fftw
Requires:      jackit

%description
Zrythm is a native GNU/Linux application built with
the GTK+3 toolkit and using the JACK Connection Kit for audio I/O.
Zrythm can automate plugin parameters using built in LFOs and envelopes
and is designed to be intuitive to use.

%prep
%autosetup -p1

%build
%meson -Denable_tests=true \
       -Denable_ffmpeg=true \
       -Dffmpeg=enabled \
       -Drtmidi=enabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Dlsp_dsp=enabled \
       -Dcarla=enabled \
       -Dgraphviz=enabled \
       -Denable_qt5=true \
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
