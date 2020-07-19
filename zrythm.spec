Name:          zrythm
Version:       0.8.694
Release:       1
Summary:       A highly automated, intuitive, Digital Audio Workstation (DAW)
Group:         Sound/Editors and Converters
License:       GPLv3
URL:           https://www.zrythm.org
Source0:       https://github.com/zrythm/zrythm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: python
BuildRequires: sed
BuildRequires: ffmpeg-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libxdot)
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
       -Denable_qt5=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/fonts/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/