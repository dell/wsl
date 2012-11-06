
include VERSION

myname=wsl
packagedest=${HOME}
packagename=${myname}-${version}
packagesrc=pkg
rpmspecdir=${packagesrc}/${packagename}
standalonedir=dcim
standalonesrc=${packagesrc}/${standalonedir}

help:
	@echo ""
	@echo "  distclean          - Remove files and directories created by make"
	@echo "  standalonepack     - Create a stand alone tar package"
	@echo "  rpmspec            - Create RPM package"
	@echo "  all                - Calls standalonepack rpmspec"
	@echo ""
	@false

all: standalonepack rpmspec

distclean: rpmspecclean standalonepackclean
	-/bin/rm -rf ${packagesrc}
	-/bin/rm response*xml request*.xml log.txt >/dev/null 2>&1 || true

rpmspecclean:
	-/bin/rm -rf ${rpmspecdir} >/dev/null 2>&1
	
rpmspecprep: rpmspecclean
	-/bin/mkdir -p ${rpmspecdir}
	-/bin/cp -dv ${myname}* viwsl wxm* LIC* READ* VER* ${rpmspecdir}/
	cat pkg-${myname}.spec | sed "s/Version:\s*1.0.0/Version:\t${version}/" > ${rpmspecdir}/${myname}.spec
	cat wsl-functions | sed "s/MYVERSION=\"0.1.5\"/MYVERSION=\"${version}\"/" > ${rpmspecdir}/wsl-functions
	for item in `ls -1 *${myname}*` ; do [ ! -x "$$item" ] && continue ; echo "## updating $$item" ; cat $$item | sed "s/\$${0\%\/\*}\/wsl-functions/\/etc\/wsl\/wsl-functions/" >${rpmspecdir}/$$item ; chmod 755 ${rpmspecdir}/$$item ; done
	chmod go-w ${rpmspecdir}/*
	chmod -x ${rpmspecdir}/VERSION

rpmspec: rpmspecprep
	tar -C ${packagesrc} -cvzf ${packagedest}/${packagename}.tar.gz . --exclude "wsl.spec"
	/bin/cp ${rpmspecdir}/wsl.spec ${packagedest}
	@echo -e "\n## NOTICE: See spec and package files at ${packagedest}\n"

standalonepackclean:
	-/bin/rm -rf ${standalonesrc} >/dev/null 2>&1

standalonepack: standalonepackclean
	-/bin/mkdir -p ${standalonesrc}
	-/bin/cp -dv ${myname}* viwsl wxm* LIC* READ* VER* ${standalonesrc}/
	cat wsl-functions | sed "s/MYVERSION=\"0.1.5\"/MYVERSION=\"${version}\"/" > ${standalonesrc}/wsl-functions
	chmod go-w ${standalonesrc}/* 
	tar -C ${packagesrc} -cvjf ${packagedest}/${packagename}.tbz ${standalonedir}
	cd ${packagedest} && /bin/rm -f ${myname}.zip && zip ${myname}.zip ${packagename}.tbz

