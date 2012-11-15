sugar-72.gtkrc: gtkrc.em
	$(srcdir)/em.py -p $$ -D scaling=\'72\' $(srcdir)/gtkrc.em > \
		$(top_builddir)/gtk/theme/sugar-72.gtkrc

sugar-100.gtkrc: gtkrc.em
	$(srcdir)/em.py -p $$ -D scaling=\'100\' $(srcdir)/gtkrc.em > \
		$(top_builddir)/gtk/theme/sugar-100.gtkrc

sugar-72-contrast.gtkrc: gtkrc-contrast.em
	$(srcdir)/em.py -p $$ -D scaling=\'72\' $(srcdir)/gtkrc-contrast.em > \
		$(top_builddir)/gtk/theme/sugar-72-contrast.gtkrc

sugar-100-contrast.gtkrc: gtkrc-contrast.em
	$(srcdir)/em.py -p $$ -D scaling=\'100\' $(srcdir)/gtkrc-contrast.em > \
		$(top_builddir)/gtk/theme/sugar-100-contrast.gtkrc

clean:
	$(RM) sugar-72.gtkrc
	$(RM) sugar-100.gtkrc
	$(RM) sugar-72-contrast.gtkrc
	$(RM) sugar-100-contrast.gtkrc

GTKRC_FILES =		\
	sugar-72.gtkrc	\
	sugar-100.gtkrc \
	sugar-100-contrast.gtkrc \
	sugar-72-contrast.gtkrc

install-data-local: $(GTKRC_FILES)
	$(mkinstalldirs) $(DESTDIR)$(datadir)/themes/sugar-72/gtk-2.0
	$(INSTALL_DATA) $(top_builddir)/gtk/theme/sugar-72.gtkrc \
		$(DESTDIR)$(datadir)/themes/sugar-72/gtk-2.0/gtkrc
	$(mkinstalldirs) $(DESTDIR)$(datadir)/themes/sugar-100/gtk-2.0
	$(INSTALL_DATA) $(top_builddir)/gtk/theme/sugar-100.gtkrc \
		$(DESTDIR)$(datadir)/themes/sugar-100/gtk-2.0/gtkrc
	$(mkinstalldirs) $(DESTDIR)$(datadir)/themes/sugar-72-contrast/gtk-2.0
	$(INSTALL_DATA) $(top_builddir)/gtk/theme/sugar-72-contrast.gtkrc \
		$(DESTDIR)$(datadir)/themes/sugar-72-contrast/gtk-2.0/gtkrc
	$(mkinstalldirs) $(DESTDIR)$(datadir)/themes/sugar-100-contrast/gtk-2.0
	$(INSTALL_DATA) $(top_builddir)/gtk/theme/sugar-100-contrast.gtkrc \
		$(DESTDIR)$(datadir)/themes/sugar-100-contrast/gtk-2.0/gtkrc

uninstall-local:
	rm -rf $(DESTDIR)$(datadir)/themes/sugar-72/gtk-2.0
	rm -rf $(DESTDIR)$(datadir)/themes/sugar-100/gtk-2.0
	rm -rf $(DESTDIR)$(datadir)/themes/sugar-100-contrast/gtk-2.0
	rm -rf $(DESTDIR)$(datadir)/themes/sugar-72-contrast/gtk-2.0

EXTRA_DIST = em.py gtkrc.em gtkrc-contrast.em
CLEANFILES = $(GTKRC_FILES)
