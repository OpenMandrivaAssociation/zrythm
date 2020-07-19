#
# spec file for package zrythm based on that for loopidity
#
# Copyright (c) 2012-2107 bill-auger bill-auger@programmer.net
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:          zrythm
Version:       0.6.003
Release:       %mkrel 4
Summary:       A highly automated, intuitive, Digital Audio Workstation (DAW)
Group:         Sound/Editors and Converters
License:       GPLv3
URL:           https://www.zrythm.org
Source0:       https://git.zrythm.org/cgit/%{name}/snapshot/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: python3
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
%autosetup

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
