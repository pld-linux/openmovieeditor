#
# Conditional build: 
%bcond_with	ntsc	# Use NTSC framerate
#
Summary:	A Non Linear Movie Editor
Summary(pl.UTF-8):   Nieliniowy edytor filmów
Name:		openmovieeditor
Version:	0.0.20060712
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/openmovieeditor/%{name}-%{version}.tar.gz
# Source0-md5:	f460529700944c6e4d90efb4b5a5feaa
Patch0:		%{name}-configure.diff
Patch1:		%{name}-configure.ac.diff
Patch2:		%{name}-framerate.patch
URL:		http://openmovieeditor.sourceforge.net/
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-gl-devel
BuildRequires:	gavl-devel >= 0.2.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.101
# lame-libs-devel? (binary shouldn't be buildrequired)
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
BuildRequires:	rpmbuild(macros) >= 1.315
BuildRequires:	xvid-devel
BuildRequires:	zlib-devel
Requires:	faac
Requires:	faad2
Requires:	fltk
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   filterout_ld  (-Wl,)?--as-needed

%description
The Open Movie Editor... is a Non Linear Movie Editor, it is in it's
very early stages of development.

Open Movie Editor is designed to be a simple tool, that provides basic
movie making capabilites. It aims to be powerful enough for the
amateur movie artist, yet easy to use.

%description -l pl.UTF-8
Open Movie Editor to nieliniowy edytor filmów, będący we wczesnym
stadium rozwoju. Jest projektowany jako proste narzędzie
udostępniające podstawowe możliwości tworzenia filmów. Jednak ma być
wystarczająco potężny dla autorów amatorskich filmów, a jednocześnie
łatwy w użyciu.

%prep
%setup -q
%patch0
%patch1
%if %{with ntsc}
%patch2 -p1
%endif

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/openmovieeditor.png
%{_desktopdir}/%{name}.desktop
