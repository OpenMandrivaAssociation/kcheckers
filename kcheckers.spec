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
URL:		https://sourceforge.net/projects/qcheckers
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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-5mdv2011.0
+ Revision: 612526
- the mass rebuild of 2010.1 packages

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 0.8.1-4mdv2010.1
+ Revision: 507515
- don't use makeinstall macro
- rediff

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 10 2008 Funda Wang <fwang@mandriva.org> 0.8.1-3mdv2009.0
+ Revision: 270155
- compile using new flags

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 22 2008 Guillaume Bedot <littletux@mandriva.org> 0.8.1-2mdv2009.0
+ Revision: 196448
- fixed path to translations

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Jun 26 2007 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 44341
- New version
- Import kcheckers



* Mon Aug 28 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.6-4mdv2007.0
- fix menu categoy

* Mon Aug 28 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.6-3mdv2007.0
- fix summary macro used in menu
- wipe out buildroot before installing
- place binary in %%{_gamesbindir}, data in %%{_gamesdatadir}
- compile with %%{optflags}
- fix non-standard-gid
- xdg menu
- silent setup
- cosmetics

* Wed Nov 09 2005 Guillaume Bedot <littletux@mandriva.org> 0.6-2mdk
- Fix menu entry

* Mon Oct 17 2005 Guillaume Bedot <littletux@mandriva.org> 0.6-1mdk
- Update to version 0.6
- Added french translation
- Changes from mcnl (Steffen Van Roosbroeck) : better description, menu-entry

* Sun Dec 19 2004 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.5-1mdk
- First package for contribs.
