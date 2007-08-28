%define	name	kcheckers
%define	oname	Kcheckers
%define	version	0.8.1
%define	rel	1
%define	release	%mkrel	%{rel}
%define	Summary	Kcheckers - Draughts game for KDE

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
BuildRequires:	qt4-devel
Source0:	http://kcheckers.org/%{name}-%{version}.tar.gz
#Source1:	%{name}-%{version}-fr.tar.bz2
Source2:	%{name}-48x48.png
Patch1:		kcheckers-0.8.1-fix-prefix.patch
Patch2:		kcheckers-0.8.1-no-doc.patch
Patch3:		kcheckers-0.8.1-fix-target.patch
Group:		Games/Boards
License:	GPL
URL:		http://wibix.de/viewpage.php?page_id=3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Qt version of the classic boardgame "checkers".
This game is also known as "draughts".

%prep
#%setup -q -a 1
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
#perl -pi -e "s#target.path	= /usr/local/bin#target.path	= %{_gamesbindir}#" kcheckers.pro
#perl -pi -e "s#/usr/local/share/kcheckers#%{_gamesdatadir}/%{name}#" config.h
%{qt4dir}/bin/qmake INSTALL_ROOT=%{buildroot}
#perl -pi -e "s#-O2#%{optflags}#g" Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

#imenu and icons
mkdir -p %{buildroot}{%{_menudir},%{_miconsdir},%{_iconsdir},%{_liconsdir}}
install -m644 icons/logo.png %{buildroot}%{_miconsdir}/%{name}.png
install -m644 icons/biglogo.png %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;X-MandrivaLinux-MoreApplications-Games-Boards;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

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
