#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audacious-plugins
Version  : 4.2
Release  : 8
URL      : https://distfiles.audacious-media-player.org/audacious-plugins-4.2.tar.bz2
Source0  : https://distfiles.audacious-media-player.org/audacious-plugins-4.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT
Requires: audacious-plugins-data = %{version}-%{release}
Requires: audacious-plugins-lib = %{version}-%{release}
Requires: audacious-plugins-license = %{version}-%{release}
Requires: audacious-plugins-locales = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : gtk+-dev
BuildRequires : libnotify-dev
BuildRequires : libogg-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsndfile-dev
BuildRequires : mpg123-dev
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(audacious)
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(fluidsynth)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libcddb)
BuildRequires : pkgconfig(libcdio)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libmodplug)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(vorbis)
BuildRequires : wavpack-dev

%description
psf2 plugin
-----------
What is this?
It's a PSF2 plugin based on:
* UPSE
* Audio Overload
* Highly Experimental

%package data
Summary: data components for the audacious-plugins package.
Group: Data

%description data
data components for the audacious-plugins package.


%package lib
Summary: lib components for the audacious-plugins package.
Group: Libraries
Requires: audacious-plugins-data = %{version}-%{release}
Requires: audacious-plugins-license = %{version}-%{release}

%description lib
lib components for the audacious-plugins package.


%package license
Summary: license components for the audacious-plugins package.
Group: Default

%description license
license components for the audacious-plugins package.


%package locales
Summary: locales components for the audacious-plugins package.
Group: Default

%description locales
locales components for the audacious-plugins package.


%prep
%setup -q -n audacious-plugins-4.2
cd %{_builddir}/audacious-plugins-4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657907786
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dneon=false \
-Dffaudio=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/audacious-plugins
cp %{_builddir}/audacious-plugins-4.2/COPYING %{buildroot}/usr/share/package-licenses/audacious-plugins/058bcaa71216cd5b7746964ef0779648d9125860
cp %{_builddir}/audacious-plugins-4.2/src/aosd/ghosd-license %{buildroot}/usr/share/package-licenses/audacious-plugins/fa2506ef781ada584042824cc343dfad55883a5a
cp %{_builddir}/audacious-plugins-4.2/src/psf/peops/License.txt %{buildroot}/usr/share/package-licenses/audacious-plugins/cb6fc634bdc848142aa51dec793f7068a5a5efad
cp %{_builddir}/audacious-plugins-4.2/src/psf/peops2/License.txt %{buildroot}/usr/share/package-licenses/audacious-plugins/317b721a1cbbba5e4678ebad188f1161fcb356d7
cp %{_builddir}/audacious-plugins-4.2/src/xsf/desmume/COPYING %{buildroot}/usr/share/package-licenses/audacious-plugins/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang audacious-plugins

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/audacious/Skins/Classic/balance.png
/usr/share/audacious/Skins/Classic/cbuttons.png
/usr/share/audacious/Skins/Classic/eq_ex.png
/usr/share/audacious/Skins/Classic/eqmain.png
/usr/share/audacious/Skins/Classic/main.png
/usr/share/audacious/Skins/Classic/monoster.png
/usr/share/audacious/Skins/Classic/nums_ex.png
/usr/share/audacious/Skins/Classic/playpaus.png
/usr/share/audacious/Skins/Classic/pledit.png
/usr/share/audacious/Skins/Classic/pledit.txt
/usr/share/audacious/Skins/Classic/posbar.png
/usr/share/audacious/Skins/Classic/shufrep.png
/usr/share/audacious/Skins/Classic/skin-classic.hints
/usr/share/audacious/Skins/Classic/skin.hints
/usr/share/audacious/Skins/Classic/text.png
/usr/share/audacious/Skins/Classic/titlebar.png
/usr/share/audacious/Skins/Classic/viscolor.txt
/usr/share/audacious/Skins/Classic/volume.png
/usr/share/audacious/Skins/Classic1.3/balance.png
/usr/share/audacious/Skins/Classic1.3/cbuttons.png
/usr/share/audacious/Skins/Classic1.3/eq_ex.png
/usr/share/audacious/Skins/Classic1.3/eqmain.png
/usr/share/audacious/Skins/Classic1.3/main.png
/usr/share/audacious/Skins/Classic1.3/monoster.png
/usr/share/audacious/Skins/Classic1.3/nums_ex.png
/usr/share/audacious/Skins/Classic1.3/playpaus.png
/usr/share/audacious/Skins/Classic1.3/pledit.png
/usr/share/audacious/Skins/Classic1.3/pledit.txt
/usr/share/audacious/Skins/Classic1.3/posbar.png
/usr/share/audacious/Skins/Classic1.3/shufrep.png
/usr/share/audacious/Skins/Classic1.3/skin-classic.hints
/usr/share/audacious/Skins/Classic1.3/skin.hints
/usr/share/audacious/Skins/Classic1.3/text.png
/usr/share/audacious/Skins/Classic1.3/titlebar.png
/usr/share/audacious/Skins/Classic1.3/viscolor.txt
/usr/share/audacious/Skins/Classic1.3/volume.png
/usr/share/audacious/Skins/Default/cbuttons.png
/usr/share/audacious/Skins/Default/eq_ex.png
/usr/share/audacious/Skins/Default/eqmain.png
/usr/share/audacious/Skins/Default/gtk-2.0/Arrows/arrow-down.png
/usr/share/audacious/Skins/Default/gtk-2.0/Arrows/arrow-insens.png
/usr/share/audacious/Skins/Default/gtk-2.0/Arrows/arrow-left.png
/usr/share/audacious/Skins/Default/gtk-2.0/Arrows/arrow-right.png
/usr/share/audacious/Skins/Default/gtk-2.0/Arrows/arrow-up.png
/usr/share/audacious/Skins/Default/gtk-2.0/Buttons/button-insensitive.png
/usr/share/audacious/Skins/Default/gtk-2.0/Buttons/button-normal.png
/usr/share/audacious/Skins/Default/gtk-2.0/Buttons/button-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check1.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check2.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check3.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check4.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check5.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/check6.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option1.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option2.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option3.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option4.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option5.png
/usr/share/audacious/Skins/Default/gtk-2.0/Check-Radio/option6.png
/usr/share/audacious/Skins/Default/gtk-2.0/Frame-Gap/frame-gap-end.png
/usr/share/audacious/Skins/Default/gtk-2.0/Frame-Gap/frame-gap-start.png
/usr/share/audacious/Skins/Default/gtk-2.0/Frame-Gap/frame.png
/usr/share/audacious/Skins/Default/gtk-2.0/Handles/handle-h.png
/usr/share/audacious/Skins/Default/gtk-2.0/Handles/handle-v.png
/usr/share/audacious/Skins/Default/gtk-2.0/Lines/line-h.png
/usr/share/audacious/Skins/Default/gtk-2.0/Lines/line-v.png
/usr/share/audacious/Skins/Default/gtk-2.0/ListHeaders/list_header-insens.png
/usr/share/audacious/Skins/Default/gtk-2.0/ListHeaders/list_header-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/ListHeaders/list_header-pressed.png
/usr/share/audacious/Skins/Default/gtk-2.0/ListHeaders/list_header.png
/usr/share/audacious/Skins/Default/gtk-2.0/Menu-Menubar/menu.png
/usr/share/audacious/Skins/Default/gtk-2.0/Menu-Menubar/menubar-item-active.png
/usr/share/audacious/Skins/Default/gtk-2.0/Menu-Menubar/menubar-item.png
/usr/share/audacious/Skins/Default/gtk-2.0/Menu-Menubar/menubar.png
/usr/share/audacious/Skins/Default/gtk-2.0/Others/null.png
/usr/share/audacious/Skins/Default/gtk-2.0/Others/ruler.png
/usr/share/audacious/Skins/Default/gtk-2.0/Panel/panel-bg.png
/usr/share/audacious/Skins/Default/gtk-2.0/ProgressBar/progressbar-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/ProgressBar/trough-progressbar-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/slider-horiz-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/slider-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/slider-vert-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/slider-vert.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/trough-horizontal.png
/usr/share/audacious/Skins/Default/gtk-2.0/Range/trough-vertical.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/scroll-thumb-horiz-pre.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/scroll-thumb-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/scroll-thumb-vert-pre.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/scroll-thumb-vert.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/slider-horiz-pre.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/slider-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/slider-vert-pre.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/slider-vert.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-down-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-down.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-left-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-left.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-right-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-right.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-up-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/stepper-up.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/trough-scrollbar-horiz.png
/usr/share/audacious/Skins/Default/gtk-2.0/Scrollbars/trough-scrollbar-vert.png
/usr/share/audacious/Skins/Default/gtk-2.0/Shadows/shadow-in.png
/usr/share/audacious/Skins/Default/gtk-2.0/Shadows/shadow-out.png
/usr/share/audacious/Skins/Default/gtk-2.0/Shadows/text-.png
/usr/share/audacious/Skins/Default/gtk-2.0/Shadows/text-entry.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-down-disable.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-down-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-down.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-up-disable.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-up-prelight.png
/usr/share/audacious/Skins/Default/gtk-2.0/Spin/spin-up.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-bottom-left.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-bottom-right.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-left-bottom.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-left-top.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-right-bottom.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-right-top.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-top-current.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-top-left.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/gap-top-right.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/notebook.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-bottom-active.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-bottom.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-left-active.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-left.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-right-active.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-right.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-top-active.png
/usr/share/audacious/Skins/Default/gtk-2.0/Tabs/tab-top.png
/usr/share/audacious/Skins/Default/gtk-2.0/Toolbar/toolbar.png
/usr/share/audacious/Skins/Default/gtk-2.0/gtkrc
/usr/share/audacious/Skins/Default/gtk-2.0/panel.rc
/usr/share/audacious/Skins/Default/main.png
/usr/share/audacious/Skins/Default/monoster.png
/usr/share/audacious/Skins/Default/nums_ex.png
/usr/share/audacious/Skins/Default/playpaus.png
/usr/share/audacious/Skins/Default/pledit.png
/usr/share/audacious/Skins/Default/pledit.txt
/usr/share/audacious/Skins/Default/posbar.png
/usr/share/audacious/Skins/Default/shufrep.png
/usr/share/audacious/Skins/Default/skin-classic.hints
/usr/share/audacious/Skins/Default/skin.hints
/usr/share/audacious/Skins/Default/text.png
/usr/share/audacious/Skins/Default/titlebar.png
/usr/share/audacious/Skins/Default/viscolor.txt
/usr/share/audacious/Skins/Default/volume.png
/usr/share/audacious/Skins/Ivory/balance.png
/usr/share/audacious/Skins/Ivory/cbuttons.png
/usr/share/audacious/Skins/Ivory/eq_ex.png
/usr/share/audacious/Skins/Ivory/eqmain.png
/usr/share/audacious/Skins/Ivory/main.png
/usr/share/audacious/Skins/Ivory/monoster.png
/usr/share/audacious/Skins/Ivory/nums_ex.png
/usr/share/audacious/Skins/Ivory/playpaus.png
/usr/share/audacious/Skins/Ivory/pledit.png
/usr/share/audacious/Skins/Ivory/pledit.txt
/usr/share/audacious/Skins/Ivory/posbar.png
/usr/share/audacious/Skins/Ivory/shufrep.png
/usr/share/audacious/Skins/Ivory/skin.hints
/usr/share/audacious/Skins/Ivory/text.png
/usr/share/audacious/Skins/Ivory/titlebar.png
/usr/share/audacious/Skins/Ivory/viscolor.txt
/usr/share/audacious/Skins/Ivory/volume.png
/usr/share/audacious/Skins/Osmosis/balance.png
/usr/share/audacious/Skins/Osmosis/cbuttons.png
/usr/share/audacious/Skins/Osmosis/eq_ex.png
/usr/share/audacious/Skins/Osmosis/eqmain.png
/usr/share/audacious/Skins/Osmosis/main.png
/usr/share/audacious/Skins/Osmosis/monoster.png
/usr/share/audacious/Skins/Osmosis/nums_ex.png
/usr/share/audacious/Skins/Osmosis/playpaus.png
/usr/share/audacious/Skins/Osmosis/pledit.png
/usr/share/audacious/Skins/Osmosis/pledit.txt
/usr/share/audacious/Skins/Osmosis/posbar.png
/usr/share/audacious/Skins/Osmosis/shufrep.png
/usr/share/audacious/Skins/Osmosis/skin.hints
/usr/share/audacious/Skins/Osmosis/text.png
/usr/share/audacious/Skins/Osmosis/titlebar.png
/usr/share/audacious/Skins/Osmosis/viscolor.txt
/usr/share/audacious/Skins/Osmosis/volume.png
/usr/share/audacious/Skins/Refugee/cbuttons.png
/usr/share/audacious/Skins/Refugee/eq_ex.png
/usr/share/audacious/Skins/Refugee/eqmain.png
/usr/share/audacious/Skins/Refugee/main.png
/usr/share/audacious/Skins/Refugee/monoster.png
/usr/share/audacious/Skins/Refugee/nums_ex.png
/usr/share/audacious/Skins/Refugee/playpaus.png
/usr/share/audacious/Skins/Refugee/pledit.png
/usr/share/audacious/Skins/Refugee/pledit.txt
/usr/share/audacious/Skins/Refugee/posbar.png
/usr/share/audacious/Skins/Refugee/shufrep.png
/usr/share/audacious/Skins/Refugee/skin.hints
/usr/share/audacious/Skins/Refugee/text.png
/usr/share/audacious/Skins/Refugee/titlebar.png
/usr/share/audacious/Skins/Refugee/viscolor.txt
/usr/share/audacious/Skins/Refugee/volume.png
/usr/share/audacious/Skins/TinyPlayer/balance.png
/usr/share/audacious/Skins/TinyPlayer/cbuttons.png
/usr/share/audacious/Skins/TinyPlayer/eq_ex.png
/usr/share/audacious/Skins/TinyPlayer/eqmain.png
/usr/share/audacious/Skins/TinyPlayer/main.png
/usr/share/audacious/Skins/TinyPlayer/monoster.png
/usr/share/audacious/Skins/TinyPlayer/nums_ex.png
/usr/share/audacious/Skins/TinyPlayer/playpaus.png
/usr/share/audacious/Skins/TinyPlayer/pledit.png
/usr/share/audacious/Skins/TinyPlayer/pledit.txt
/usr/share/audacious/Skins/TinyPlayer/posbar.png
/usr/share/audacious/Skins/TinyPlayer/shufrep.png
/usr/share/audacious/Skins/TinyPlayer/skin.hints
/usr/share/audacious/Skins/TinyPlayer/text.png
/usr/share/audacious/Skins/TinyPlayer/titlebar.png
/usr/share/audacious/Skins/TinyPlayer/viscolor.txt
/usr/share/audacious/Skins/TinyPlayer/volume.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/audacious/Container/asx.so
/usr/lib64/audacious/Container/asx3.so
/usr/lib64/audacious/Container/audpl.so
/usr/lib64/audacious/Container/m3u.so
/usr/lib64/audacious/Container/pls.so
/usr/lib64/audacious/Container/xspf.so
/usr/lib64/audacious/Effect/bitcrusher.so
/usr/lib64/audacious/Effect/compressor.so
/usr/lib64/audacious/Effect/crossfade.so
/usr/lib64/audacious/Effect/crystalizer.so
/usr/lib64/audacious/Effect/echo.so
/usr/lib64/audacious/Effect/ladspa.so
/usr/lib64/audacious/Effect/mixer.so
/usr/lib64/audacious/Effect/resample.so
/usr/lib64/audacious/Effect/silence-removal.so
/usr/lib64/audacious/Effect/speed-pitch.so
/usr/lib64/audacious/Effect/stereo.so
/usr/lib64/audacious/Effect/voice_removal.so
/usr/lib64/audacious/General/alarm.so
/usr/lib64/audacious/General/albumart-qt.so
/usr/lib64/audacious/General/albumart.so
/usr/lib64/audacious/General/aosd.so
/usr/lib64/audacious/General/delete-files.so
/usr/lib64/audacious/General/gtkui.so
/usr/lib64/audacious/General/hotkey.so
/usr/lib64/audacious/General/lyricwiki-qt.so
/usr/lib64/audacious/General/mpris2.so
/usr/lib64/audacious/General/notify.so
/usr/lib64/audacious/General/playlist-manager-qt.so
/usr/lib64/audacious/General/playlist-manager.so
/usr/lib64/audacious/General/qtui.so
/usr/lib64/audacious/General/scrobbler.so
/usr/lib64/audacious/General/search-tool-qt.so
/usr/lib64/audacious/General/search-tool.so
/usr/lib64/audacious/General/skins-qt.so
/usr/lib64/audacious/General/skins.so
/usr/lib64/audacious/General/song-info-qt.so
/usr/lib64/audacious/General/song_change.so
/usr/lib64/audacious/General/statusicon-qt.so
/usr/lib64/audacious/General/statusicon.so
/usr/lib64/audacious/Input/amidi-plug.so
/usr/lib64/audacious/Input/console.so
/usr/lib64/audacious/Input/flacng.so
/usr/lib64/audacious/Input/madplug.so
/usr/lib64/audacious/Input/metronom.so
/usr/lib64/audacious/Input/modplug.so
/usr/lib64/audacious/Input/psf2.so
/usr/lib64/audacious/Input/sndfile.so
/usr/lib64/audacious/Input/tonegen.so
/usr/lib64/audacious/Input/vorbis.so
/usr/lib64/audacious/Input/vtx.so
/usr/lib64/audacious/Input/wavpack.so
/usr/lib64/audacious/Input/xsf.so
/usr/lib64/audacious/Output/alsa.so
/usr/lib64/audacious/Output/filewriter.so
/usr/lib64/audacious/Output/oss4.so
/usr/lib64/audacious/Output/pulse_audio.so
/usr/lib64/audacious/Output/sdlout.so
/usr/lib64/audacious/Transport/gio.so
/usr/lib64/audacious/Visualization/blur_scope-qt.so
/usr/lib64/audacious/Visualization/blur_scope.so
/usr/lib64/audacious/Visualization/cairo-spectrum.so
/usr/lib64/audacious/Visualization/gl-spectrum-qt.so
/usr/lib64/audacious/Visualization/gl-spectrum.so
/usr/lib64/audacious/Visualization/qt-spectrum.so
/usr/lib64/audacious/Visualization/vumeter-qt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/audacious-plugins/058bcaa71216cd5b7746964ef0779648d9125860
/usr/share/package-licenses/audacious-plugins/317b721a1cbbba5e4678ebad188f1161fcb356d7
/usr/share/package-licenses/audacious-plugins/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/audacious-plugins/cb6fc634bdc848142aa51dec793f7068a5a5efad
/usr/share/package-licenses/audacious-plugins/fa2506ef781ada584042824cc343dfad55883a5a

%files locales -f audacious-plugins.lang
%defattr(-,root,root,-)

