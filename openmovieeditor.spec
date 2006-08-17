
%bcond_with	ntsc # Use NTSC framerate

Summary:	A Non Linear Movie Editor
Name:		openmovieeditor
Version:	0.0.20060712
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://openmovieeditor.sourceforge.net
Source0:	http://dl.sourceforge.net/openmovieeditor/%{name}-%{version}.tar.gz
# Source0-md5:	f460529700944c6e4d90efb4b5a5feaa
Patch0:		%{name}-configure.diff
Patch1:		%{name}-configure.ac.diff
Patch2:		%{name}-framerate.patch
BuildRequires:	faac
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-gl-devel
BuildRequires:	gavl-devel >= 0.2.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.101
BuildRequires:	lame
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libquicktime-devel >= 0.9.7
BuildRequires:	libsndfile-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel
BuildRequires:	portaudio-devel
BuildRequires:	xvid-devel
BuildRequires:	zlib-devel
Requires:	faac
Requires:	faad2
Requires:	fltk
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   filterout_ld  (-Wl,)?--as-needed

%description
The Open Movie Editor ... is a Non Linear Movie Editor, it is in it's
very early stages of development.

Open Movie Editor is designed to be a simple tool, that provides basic
movie making capabilites. It aims to be powerful enough for the
amateur movie artist, yet easy to use.

See http://openmovieeditor.sourceforge.net/

Author Richard Spindler <richard.spindler@gmail.com>

%prep
%setup -q
%patch0
%patch1
%if %{with ntsc}
%patch2 -p1
%endif

%build
%configure \
	--prefix=%{_prefix}
%__make

%install
rm -rf $RPM_BUILD_ROOT

%__make install-strip \
	DESTDIR=$RPM_BUILD_ROOT

# icon
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install icons/openmovieeditor.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}

# menu-entry
cat > %{name}.desktop << EOF
[Desktop Entry]
Comment=A Non Linear Movie Editor
Name=%{name}
GenericName=
Type=Application
Exec=openmovieeditor
Icon=openmovieeditor.png
DocPath=
EOF

install -d $RPM_BUILD_ROOT%{_datadir}/applications
install %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications

%clean

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/openmovieeditor.png
%{_desktopdir}/%{name}.desktop
