%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

# Environment setup:
#
#       mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
#       echo | bzip2 -c > ~/rpmbuild/SOURCES/sugar-artwork-<version>.bz2
#       cd ~/build/ && git clone git://git.sugarlabs.org/dextrose/sugar-artwork.git
#       ln -s ~/build/sugar-artwork/dextrose/sugar-artwork.spec \
#             ~/rpmbuild/SPECS/sugar-artwork.spec
#       rpmbuild -ba ~/rpmbuild/SPECS/sugar-artwork.spec
#

%define git_repo sugar-artwork
%define git_head devel

%define git_repodir %(echo ~/build/)
%define git_gitdir %{git_repodir}/%{git_repo}/.git

%define git_get_source pushd %{git_repodir}/%{git_repo} ;\
	/usr/bin/git pull ;\
#        /usr/bin/git log > CHANGES ;\
#        /usr/bin/git add CHANGES ;\
#        /usr/bin/git commit -m "Updated CHANGES file" ;\
        /usr/bin/git archive --format=tar --prefix=%{name}-%{version}/ %{git_head} | \
                bzip2 -c > %{_sourcedir}/%{name}-%{version}.tar.bz2 ;\
        popd

%define git_clone_source if [ -d %{name}-%{version} ] ; then \
                cd %{name}-%{version} && git pull origin %{git_head} ; \
        else \
                git clone %{git_gitdir} %{name}-%{version} && \
                cd %{name}-%{version}/ ; \
        fi

%define git_submodule git submodule
%define git_prep_submodules %{git_submodule} init --cloned && %{git_submodule} update

%define git_version %(git --git-dir=%{git_gitdir} describe --tags 2> /dev/null || echo 0.0-`git --git-dir=%{git_gitdir} log --oneline | wc -l`-g`git --git-dir=%{git_gitdir} describe --always`)

# if the git repo has tags
%define git_get_ver %(echo %{git_version} | sed 's/^v\\?\\(.*\\)-\\([0-9]\\+\\)-g.*$/\\1/;s/-//')
%define git_get_rel %(echo %{git_version} | sed 's/^v\\?\\(.*\\)-\\([0-9]\\+-g.*\\)$/\\2/;s/-/_/')



Summary: Artwork for Sugar look-and-feel
Name: sugar-artwork
Epoch: 1
Version: %git_get_ver
Release: %git_get_rel
URL: http://sugarlabs.org
Group: User Interface/Desktops
License: LGPLv2+
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2 

BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: xorg-x11-apps
BuildRequires: perl-XML-Parser
BuildRequires: python
BuildRequires: python-empy
BuildRequires: icon-naming-utils
BuildRequires: icon-slicer

Requires: gtk2 gtk3

%description
sugar-artwork contains the themes and icons that make up the OLPC default 
look and feel.

%prep
%git_get_source
%setup -q

%build
sh autogen.sh
autoreconf -i
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%files
%defattr(-,root,root)
%doc README COPYING NEWS

%{_datadir}/icons/sugar
%{_datadir}/themes/sugar-100/gtk-2.0/gtkrc
%{_datadir}/themes/sugar-72/gtk-2.0/gtkrc
%{_datadir}/themes/sugar-100-contrast/gtk-2.0/gtkrc
%{_datadir}/themes/sugar-72-contrast/gtk-2.0/gtkrc
%{_libdir}/gtk-2.0/*/engines/*.so

#gtk3
%{_datadir}/themes/sugar-100/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-100/gtk-3.0/assets/*
%{_datadir}/themes/sugar-72/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-72/gtk-3.0/assets/*

%changelog
* Tue Oct 16 2012 Daniel Drake <dsd@laptop.org> 0.97.7-1
- 0.97.7 devel release

* Thu Oct 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.97.6-1
- 0.97.6 devel release

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.5-1
- 0.97.5 devel release

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.4-1
- 0.97.4 devel release

* Thu Sep 20 2012 Daniel Drake <dsd@laptop.org> - 0.97.3-1
- Ne development release

* Thu Sep 13 2012 Daniel Drake <dsd@laptop.org> - 0.97.2-1
- New development release

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.1-1
- 0.97.2 devel release

* Wed Aug 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.97.0-1
- 0.97.0 devel release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.4-1
- 0.96.4 stable release

* Sat Jun  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.3-1
- 0.96.3 stable release

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.2-1
- 0.96.2 stable release

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.1-1
- 0.96.1 stable release

* Tue Apr 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.96.0-1
- 0.96.0 stable release

* Thu Apr 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.5-1
- devel release 0.95.5

* Fri Mar 23 2012 Simon Schampijer <simon@laptop.org> - 0.95.4-1
- devel release 0.95.4

* Wed Mar 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.3-1
- devel release 0.95.3

* Mon Feb  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.2-3
- Update 0.95.2 tarball

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Simon Schampijer <simon@laptop.org> - 0.95.2-1
- include the gtk3 theme

* Tue Oct 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.95.1-1
- devel release 0.95.1

* Thu Sep 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.94.0-1
- 0.94.0 stable release

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.4-1
- 0.93.4 dev release

* Fri Aug 23 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.3-1
- 0.93.3 dev release

* Fri Aug 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.93.2-1
- 0.93.2 dev release

* Mon Feb 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.92.0-1
- 0.92.0 stable release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.0-2
- bump build

* Wed Sep 29 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.90.0-1
- 0.90.0 stable release

* Wed Aug 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.4-1
- New upstream devel 0.89.4 release

* Tue Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.3-1
- New upstream devel 0.89.3 release

* Thu Jul 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.2-1
- New upstream devel 0.89.2 release

* Wed Jul 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.89.1-1
- New upstream devel 0.89.1 release

* Thu Jun  3 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.1-1
- New upstream stable 0.88.1 release

* Tue Apr 13 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.0-2
- Add patch for deprecated gtk functions to fix borked sugar

* Tue Mar 20 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 0.88.0-1
- New upstream stable 0.88.0 release

* Wed Mar 10 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.3-1
- New upstream release

* Fri Feb 12 2010 Sebastian Dziallas <sebastian@when.com> - 0.87.2-1
- New upstream release

* Sat Dec 05 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 0.87.1-1
- New upstream release

* Thu Sep 24 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 0.86.0-1
- New upstream release

* Fri Sep 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.4-2
- Upload sources

* Fri Sep 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.4-1
- New upstream release

* Fri Sep 11 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.3-1
- New upstream release

* Fri Jul 31 2009 Mathieu Bridon (bochecha) <bochecha@fedoraproject.org> - 0.85.2-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.1-2
- Remove matchbox theme dir

* Sat Jul 18 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.85.1-1
- New upstream release

* Wed Apr 08 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-3
- Another rebuild for icon-slicer-0.3-12

* Wed Apr 08 2009 Simon Schampijer <simon@schampijer.de> - 0.84.1-2
- Rebuild for icon-slicer-0.3-12

* Wed Mar 11 2009 Tomeu Vizoso <tomeu@sugarlabs.org> - 0.84.1-1
- Add back some icons to the Makefile (Simon)

* Tue Mar 03 2009 Simon Schampijer <simon@schampijer.de> - 0.84.0-1
- Rebuild for 0.84

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Simon Schampijer <simon@schampijer.de> - 0.83.5-1
- Icon for a generic document, part of #360
- Add view source icon 

* Mon Feb 16 2009 Simon Schampijer <simon@schampijer.de> - 0.83.4-1
- Add documend-send icon (Gary C Martin) #227
- Add application-x-generic as a copy of application-octet-stream #13
- Add icons drive-harddisk and drive 

* Fri Feb 06 2009 Simon Schampijer <simon@schampijer.de> - 0.83.3-2.20090206giteb39d7b3b2b
- Add documend-send icon (Gary C Martin) #227
- Add application-x-generic as a copy of application-octet-stream #13
- Add icons drive-harddisk and drive

* Tue Jan 20 2009 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.3-1
- add activity-journal icon to artwork
- add system-logout icon (part of #207)
- add everything needed for the colorpicker. That is a small icon and a bit in the gtkrc.
- fix triangular arrows by looking at the parent_bg_color option
- add icons for object transfers 

* Sun Jan 04 2009 Simon Schampijer <simon@laptop.org> - 0.83.2-1
- New icon for the wired network

* Tue Nov  4 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.83.1-1
- Update to 0.83.1

* Tue Sep 23 2008 Simon Schampijer <simon@laptop.org> - 0.82.3-1
- Fix corrupted network-wireless-060.svg

* Sat Sep 20 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.2-1
- #7685 Alternate home layouts; fixed ring scaling; better modularization of layouts
- #8554 Indicate connected AP in Neighborhood view.
- #8198 Use a plainer "wrench" for the Settings icon
- #7987 Home view XO icon palette for Control Panel has wrong icon

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.82.1-2
- fix license tag

* Thu Aug 28 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.1-1
- #4312 need volume button icons for totem player
- #7939 Missing stock icons

* Thu Aug 07 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.82.0-1
- 7641 Install GTK compatibility symlinks using icon-naming-utils package

* Wed Jul 09 2008 Simon Schampijer <simon@laptop.org> - 0.81.6-2.20080709gitc77b345c02
- git snapshot
- 7385 Add view-freeform icon (eben)

* Sat Jun 21 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.81.1
- Some improvements to the gtk theme (benzea)

* Fri Jun 13 2008 Simon Schampijer <simon@laptop.org> - 0.79.3-1
- Update to 0.79.3

* Wed Apr 09 2008 Tomeu Vizoso <tomeu@tomeuvizoso.net> - 0.79.2
- Misc. icon fixes.

* Thu Apr 03 2008 Simon Schampijer <simon@laptop.org> - 0.79.1
- Frame/Home redesign - Put corner stone

* Sat Feb  9 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.0-1
- Update to 0.79.0

* Fri Nov 02 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.33.20071102git0763fefc48
- #4610 Prevent a division by zero while making icons insensitive. (benzea)

* Fri Nov 02 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.32.20071102git9bc8be4d48
- #4568 Implement a better effect for insensitive icons [may need more tweaking] (benzea)
- Added tray-hide/show icons (eben)
- Added a zoom-original button for returning to actual size (eben)
- Updated the full media button set to the new design spec (eben)
- Added fullscreen (and return) buttons (eben)
- #4595 Fixed the "wiggle" in the busy cursor (eben)

* Fri Oct 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.31.20071019git811b41812a
- New snapshot

* Tue Oct  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.30.20071009git91d9239340
- New snapshot

* Sun Oct  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.29.20071007git9b93ff3a3f
- New snapshot

* Fri Sep 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.28.20070914git2aac89b4fe
- New snapshot

* Wed Sep 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.26.20070912gite4fd20770c
- New snapshot

* Sun Sep  9 2007 Dan Williams <dcbw@redhat.com> - 0.34-0.25.20070909git2e13ad392d
- New snapshot

* Thu Sep  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.24.20070906gitf89f6e00cc
- New snapshot

* Thu Aug 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.23.20070830gitd2120f79b7
- New snapshot

* Wed Aug 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.21.20070829git60139d01c3
- New snapshot

* Tue Aug 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.20.20070827git931d3dee31
- New snapshot

* Wed Aug 22 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.19.20070822git8de1d5be84
- New snapshot

* Mon Aug 20 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.18.20070820git81695a321f
- New snapshot

* Tue Aug 14 2007 John (J5) Palmieri <johnp@redhat.com> - 0.34-0.15.20070814gitb0228a578f
- New snapshot

* Fri Jul 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.15.20070727git359c47de2c
- New snapshot

* Wed Jul 25 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.14.20070725git37744886a7
- New snapshot

* Tue Jul 24 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.13.20070724git3368046fdc
- New snapshot

* Sat Jul 21 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.12.20070721gitb4d5062514
- New snapshot

* Thu Jul 19 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.11.20070719gitf662ad4507
- New snapshot

* Wed Jul 18 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.10.20070718giteb3ffd0171
- New snapshot

* Tue Jul 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.9.20070716gita0c7965b7b
- New snapshot

* Mon Jul 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.8.20070715git7724264dab
- New snapshot

* Fri Jul 13 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.7.20070713git454a63a3f0
- New snapshot

* Wed Jul 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.6.20070711git4d612c6644
- New snapshot

* Fri Jul  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.5.20070705gitaddbcacbc5
- Several new icons for network and journal

* Fri Jun 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.4.20070629git13fafab42e
- Minor tweaks to the controls style.

* Thu Jun 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.3.20070628git6c74e162ca
- New snapshot

* Tue Jun 26 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.34-0.2.20070626gitc788870202
- New snapshot

* Sat Jun 16 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.33-3.git5aef11739b
- Spec cleanups, patch by ivazqueznet@gmail.com
- Rename to sugar-artwork

* Thu Jun 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.33-3.git5640efb030
- Fix comboboxes on the toolbars

* Mon Jun  4 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.33-2.gitc3d3dce71b
- New snapshot

* Mon May 28 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.20.20070528git
- More work on the gtk theme

* Wed May 16 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.19.20070516git
- Add icon for call

* Mon May 14 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.17.20070514git
- More work on the theme

* Thu May 11 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.16.20070511git
- Fix cursors

* Thu May 11 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.15.20070511git
- Better gtk theme

* Thu May 10 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.14.20070510git
- New snapshot

* Thu Mar 29 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.12.20070329git
- Add an icon for the mesh device

* Thu Mar 22 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.11.20070322git
- Remove conflict with redhat-artwork

* Wed Mar 21 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.10.20070321git
- Fix italic icon

* Tue Mar 20 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.9.20070320git
- New icons for the write activity

* Mon Mar 19 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.8.20070319git
- More matchbox theme fixes

* Mon Mar 19 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.7.20070319git
- Fix matchbox font size

* Thu Mar 15 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.6.20070315git
- Fix font an icons size

* Wed Mar  7 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.5.20070307git
- Put back the gtk theme

* Fri Mar  2 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.4.20070302git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.3.20070228git
- Update snapshot

* Wed Feb 28 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.2.20070228git
- Update snapshot

* Sat Feb 24 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-2.1.20070224git
- Update to 2.1.20070224git

* Wed Feb  8 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.33-1
- Update to 0.33

* Wed Jan 31 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.32-1
- Update to 0.32

* Mon Jan 29 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.31-1
- Update to 0.31

* Tue Jan 16 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.30-1
- Update to 0.30

* Wed Jan 11 2007 Marco Pesenti Gritti <mpg@redhat.com> 0.29-1
- Update to 0.29

* Tue Dec 19 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.28-1
- Update to 0.28

* Tue Dec 19 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.27-1
- Update to 0.27

* Fri Nov 17 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.26-1
- Update 0.26

* Thu Nov  9 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.25-1
- Update to 0.25

* Wed Nov  8 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.24-1
- Update to 0.24

* Sat Nov  4 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.23-1
- Update to 0.23

* Fri Nov  3 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.22-1
- Update to 0.22 

* Mon Oct 30 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.21-1
- Update to 0.21

* Wed Oct 25 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.20-1
- Update to 0.20

* Tue Oct 24 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.19-1
- Update to 0.19

* Fri Oct 20 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.18-1
- Update to 0.18

* Thu Oct 19 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.17-1
- Update to 0.17

* Wed Oct 18 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.16-1
- Update to 0.16

* Tue Oct 17 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.15-1
- Update to 0.15

* Thu Oct 13 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.14-1
- Buld 0.14

* Thu Oct  5 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.13-1
- Build 0.13

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.12-1
- Build 0.12

* Fri Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.11-1
- Build 0.11

* Fri Jun  30 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.10-1
- Build 0.10 and add xorg-x11-apps

* Fri Jun  29 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.9-1
- Build 0.9

* Fri Jun  22 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.8-1
- Build 0.8

* Thu Jun  21 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.7-2
- Add some unpackaged files

* Thu Jun  7 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.7-1
- Build 0.7

* Thu Jun  7 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.6-1
- Build 0.6

* Thu Jun  7 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.5-1
- Build 0.5

* Thu Jun  7 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.4-2
- Add build require (perl xml parser)

* Thu Jun  7 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.4-1
- Build 0.4

* Thu May 23 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.3-1
- Build 0.3

* Thu May 22 2006 Marco Pesenti Gritti <mpg@redhat.com> 0.2-1
- Build 0.2
