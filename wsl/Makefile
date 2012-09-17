
include VERSION

myname=wsl

all: packageit

clean:
	-/bin/rm response*xml request*.xml log.txt
	-/bin/rm -rf dcim

packageit: clean
	mkdir dcim 
	cp -fpv * dcim  || true 
	chmod a-w dcim/* 
	tar -cvjf ../${myname}-${version}.tbz dcim/* --exclude "Makefile"
	zip -u ../${myname}.zip ../${myname}-${version}.tbz 
	/bin/rm -rf dcim

