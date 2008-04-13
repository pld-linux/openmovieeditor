# TODO:
#	- use system portaudio
#	- check Requires
#
# Conditional build: 
%bcond_with	ntsc	# Use NTSC framerate
#
Summary:	A Non Linear Movie Editor
Summary(pl.UTF-8):	Nieliniowy edytor filmów
Name:		openmovieeditor
Version:	0.0.20080209
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/openmovieeditor/%{name}-%{version}.tar.gz
# Source0-md5:	528f90d82f05fd0b25168f29e5b33c51
Patch0:		%{name}-as-needed.patch
Patch1:		%{name}-framerate.patch
URL:		http://openmovieeditor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-gl-devel
BuildRequires:	gavl-devel >= 0.2.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.101
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libquicktime-devel >= 0.9.7
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	rpmbuild(macros) >= 1.315
BuildRequires:	xorg-lib-libXft-devel
Requires:	faac
Requires:	faad2
Requires:	fltk
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
%if %{with ntsc}
%patch1 -p1
%endif

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS NEWS README TODO doc/images doc/style.css doc/tutorial.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/openmovieeditor.png
%{_desktopdir}/%{name}.desktop
