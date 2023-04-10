ifeq ($(PREFIX),)
	PREFIX := /usr/local
endif


install:
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -m 644 main.py $(DESTDIR)$(PREFIX)/bin/intentview
	install -d $(DESTDIR)$(PREFIX)/share/applications/ 
	install -m 644 Intent.desktop $(DESTDIR)$(PREFIX)/share/applications/
