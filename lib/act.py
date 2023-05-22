import sys, win32com.client,time
import subprocess
from lib import utl

def sap_launch():
    
    path = r"C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe"
    subprocess.Popen(path)
    time.sleep(2)

    #   try:

    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return

    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return
        
    connection = application.OpenConnection("UACPL_DEV", True)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto  = None
        return

    session = connection.Children(0)
    if not type(session) == win32com.client.CDispatch:
        connection  = None
        application = None
        SapGuiAuto  = None
        return
    return session

def sap_login(sap):
    utl.fill_textbox(sap,"wnd[0]/usr/txtRSYST-BNAME","bs1_uacpl")
    utl.fill_textbox(sap,"wnd[0]/usr/pwdRSYST-BCODE","Zencon@2023")
    utl.fill_textbox(sap,"wnd[0]/usr/txtRSYST-LANGU","EN")
    utl.send_cntrkey(sap,"wnd[0]","0")
    utl.select_radio(sap,"wnd[1]/usr/radMULTI_LOGON_OPT2")
    utl.click_button(sap,"wnd[1]/tbar[0]/btn[0]")
    utl.click_button(sap,"wnd[1]/tbar[0]/btn[0]")

def txn_vt02n(sap):
    utl.fill_textbox(sap,"wnd[0]/tbar[0]/okcd","/nvt01n")
    utl.send_cntrkey(sap,"wnd[0]","0")
    utl.fill_textbox(sap,"wnd[0]/usr/ctxtVTTK-TPLST","1111")
    utl.select_cmkey(sap,"wnd[0]/usr/cmbVTTK-SHTYP","0002")
    utl.send_cntrkey(sap,"wnd[0]","0")
    utl.click_button(sap,"wnd[0]/tbar[0]/btn[11]")
    utl.click_button(sap,"wnd[1]/usr/btnSPOP-OPTION1")
    print(utl.read_textbox(sap,"wnd[0]/sbar/pane[0]"))

        