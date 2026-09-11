#
# spec file for package kmeteo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           kmeteo
Version:        0.1.0
Release:        0
Summary:        Program to show the weather forecast of the next hours and days
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://gitlab.com/bitseater/kmeteo
Source:         https://gitlab.com/bitseater/kmeteo/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-PyQt6
BuildRequires:  python3-PyQt6-WebEngine
BuildRequires:  python3-requests
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
Provides:       kmeteo = %{version}
Obsoletes:      kmeteo < %{version}

%description
A program which displays current weather, with information about temperature,
pressure, wind speed and direction, as well as sunrise and sunset times.

%package lang
Summary:        Translations for %{name}
Group:          Productivity/Other
Requires:       %{name} = %{version}-%{release}

%description lang
Translation files for %{name}.

%prep
%setup -q -n kmeteo-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang io.gitlab.bitseater.kmeteo %{name}.lang

# dirlist HiDPI icons (see: hicolor/index.theme)
_dirlist=$PWD/dir.lst
pushd %{buildroot}
find ./ | while read _list; do
    echo $_list | grep '[0-9]\@[0-9]' || continue
    _path=$(echo $_list | sed 's/[^/]//')
    if ! ls ${_path%/*}; then
        grep -xqs "\%dir\ ${_path%/*}" $_dirlist || echo "%dir ${_path%/*}" >> $_dirlist
    fi
done
popd

%files -f dir.lst
%license COPYING
%doc AUTHORS README.md
%{_bindir}/io.gitlab.bitseater.kmeteo
%{_datadir}/applications/io.gitlab.bitseater.kmeteo.desktop
%{_datadir}/icons/hicolor/*/*/io.gitlab.bitseater.kmeteo*.??g
%{_datadir}/metainfo/io.gitlab.bitseater.kmeteo.appdata.xml
%{_mandir}/man?/io.gitlab.bitseater.kmeteo.?%{ext_info}

%files lang -f %{name}.lang

%changelog
