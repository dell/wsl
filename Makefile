
include VERSION

myname=wsl
packagepath=..
rpmspecdir=pkg
standalonedir=dcim

all: help

help:
	@echo ""
	@echo "  distclean          - Remove files and directories created by make"
	@echo "  standalonepack     - Create a stand alone tar package"
	@echo "  rpmspec            - Create and prepare a directory for RPM packaging"
	@echo ""
	@false

distclean: rpmspecclean standalonepackclean
	-/bin/rm response*xml request*.xml log.txt >/dev/null 2>&1 || true

rpmspecclean:
	-/bin/rm -rf ${rpmspecdir} >/dev/null 2>&1
	
rpmspec: rpmspecclean
	-/bin/mkdir ${rpmspecdir}
	-/bin/cp ${myname}* wxm* LIC* READ* VER* ${rpmspecdir}/
	cat pkg-${myname}.spec | sed "s/Version:\s*1.0.0/Version:\t${version}/" > ${rpmspecdir}/${myname}.spec
	cat wsl-functions | sed "s/MYVERSION=\"0.1.5\"/MYVERSION=\"${version}\"/" > ${rpmspecdir}/wsl-functions
	for item in `ls -1 ${myname}* | grep -v 'wsl-'`; do cat $$item | sed "s/\$${0\%\/\*}\/wsl-functions/\/etc\/wsl\/wsl-functions/" >${rpmspecdir}/$$item ; chmod 755 ${rpmspecdir}/$$item ; done
	chmod go-w ${rpmspecdir}/*

standalonepackclean:
	-/bin/rm -rf ${standalonedir} >/dev/null 2>&1

standalonepack: standalonepackclean
	-/bin/mkdir ${standalonedir}
	-/bin/cp ${myname}* wxm* LIC* READ* VER* ${standalonedir}/
	cat wsl-functions | sed "s/MYVERSION=\"0.1.5\"/MYVERSION=\"${version}\"/" > ${standalonedir}/wsl-functions
	chmod go-w ${standalonedir}/* 
	tar -cvjf ${packagepath}/${myname}-${version}.tbz ${standalonedir}/* --exclude "Makefile"
	zip -u ${packagepath}/${myname}.zip ${packagepath}/${myname}-${version}.tbz 

