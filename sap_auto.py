from lib import act 

sap = act.sap_launch()
act.sap_login(sap)
act.txn_vt02n(sap)