%define	name	kcheckers
%define	oname	Kcheckers
%define	version	0.6
%define	rel	4
%define	release	%mkrel	%{rel}
%define	Summary	Kcheckers - Draughts game for KDE

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
BuildRequires:	qt3-devel
Source0:	http://kcheckers.org/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}-fr.tar.bz2
Source2:	%{name}-48x48.png
Group:		Games/Boards
License:	GPL
URL:		http://kcheckers.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Qt version of the classic boardgame "checkers".
This game is also known as "draughts".

%prep
%setup -q -a 1

%build
perl -pi -e "s#target.path	= /usr/local/bin#target.path	= %{_gamesbindir}#" kcheckers.pro
perl -pi -e "s#/usr/local/share/kcheckers#%{_gamesdatadir}/%{name}#" config.h
qmake INSTALL_ROOT=%{buildroot}
perl -pi -e "s#-O2#%{optflags}#g" Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

#imenu and icons
mkdir -p %{buildroot}{%{_menudir},%{_miconsdir},%{_iconsdir},%{_liconsdir}}
install -m644 png/logo.png %{buildroot}%{_miconsdir}/%{name}.png
install -m644 png/biglogo.png %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): needs="x11" \
	section="More Applications/Games/Boards" \
	title="%{oname}" \
	longtitle="%{Summary}" \
	command="%{_gamesbindir}/%{name}" \
	icon="%{name}.png" \
	xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{oname}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;X-MandrivaLinux-MoreApplications-Games-Boards;
EOF

#to avoid having docs twice...
rm -f %{buildroot}%{_gamesdatadir}/%{name}/{AUTHORS,ChangeLog,COPYING,README,TODO}

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
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
