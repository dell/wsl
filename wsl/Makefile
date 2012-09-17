
include VERSION

packageit:
	[ ! -d "dcim" ] && mkdir dcim 
	cp -fpv * dcim  || true 
	chmod a-w dcim/* 
	tar -C dcim -cvjf ../wsl-${version}.tbz *wsl* wxml* LICENSE* 
	zip -u ../wsl.zip ../wsl-${version}.tbz 
	/bin/rm -rf dcim

