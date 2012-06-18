#
# Regular cron jobs for the canaima-primeros-pasos package
#
0 4	* * *	root	[ -x /usr/bin/canaima-primeros-pasos_maintenance ] && /usr/bin/canaima-primeros-pasos_maintenance
