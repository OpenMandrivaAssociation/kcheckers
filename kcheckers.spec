%define	name	kcheckers
%define	oname	Kcheckers
%define	version	0.8.1
%define	rel	5
%define	release	%mkrel	%{rel}
%define	Summary	Kcheckers - Draughts game for KDE

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
BuildRequires:	qt4-devel
Source0:	http://downloads.sourceforge.net/qcheckers/%{name}-%{version}.tar.gz
Source2:	%{name}-48x48.png
Patch1:		kcheckers-0.8.1-fix-prefix.patch
Patch2:		kcheckers-0.8.1-no-doc.patch
Patch3:		kcheckers-0.8.1-fix-target.patch
Patch4:		kcheckers-0.8.1-fix-translations-path.patch
Group:		Games/Boards
License:	GPLv2+
URL:		http://sourceforge.net/projects/qcheckers
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Qt version of the classic boardgame "checkers".
This game is also known as "draughts".

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

#imenu and icons
mkdir -p %{buildroot}{%{_menudir},%{_miconsdir},%{_iconsdir},%{_liconsdir}}
install -m644 icons/logo.png %{buildroot}%{_miconsdir}/%{name}.png
install -m644 icons/biglogo.png %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;X-MandrivaLinux-MoreApplications-Games-Boards;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
