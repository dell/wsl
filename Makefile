
include VERSION

myname=wsl
packagepath=../..
rpmpkg=pkg

all: packageit

clean:
	-/bin/rm response*xml request*.xml log.txt wsl.spec >/dev/null 2>&1
	-/bin/rm -rf dcim >/dev/null 2>&1
	-/bin/rm -rf ${rpmpkg} >/dev/null 2>&1

rpmspec:
	-/bin/mkdir pkg
	-/bin/cp wl* wxm* LIC* READ* VER* ${rpmpkg}/
	cat pkg-wsl.spec | sed "s/Version:\s*1.0.0/Version:\t${version}/" > ${rpmpkg}/wsl.spec
	cat wsl-functions | sed "s/MYVERSION=\"0.1.5\"/MYVERSION=\"${version}\"/" > ${rpmpkg}/wsl-functions
	for item in `ls -1 wsl* | grep -v 'wsl-'`; do cat $item | sed "s/\${0\%\/\*}\/wsl-functions/\/etc\/wsl\/wsl-functions/" >pkg/$item ; done

packageit: clean
	mkdir dcim 
	cp -fpv * dcim  || true 
	chmod a-w dcim/* 
	tar -cvjf ${packagepath}/${myname}-${version}.tbz dcim/* --exclude "Makefile"
	zip -u ${packagepath}/${myname}.zip ${packagepath}/${myname}-${version}.tbz 
	/bin/rm -rf dcim

