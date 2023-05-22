import sys, win32com.client,time
import subprocess

def sap_login():
    
    path = r"C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe"
    subprocess.Popen(path)
    time.sleep(2)

    #   try:

    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    #if not type(SapGuiAuto) == win32com.client.CDispatch:
    

    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        
    connection = application.OpenConnection("UACPL_DEV", True)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto  = None

    session = connection.Children(0)
    if not type(session) == win32com.client.CDispatch:
        connection  = None
        application = None
        SapGuiAuto  = None

    session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "bs1_uacpl"
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "Zencon@2023"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[1]/tbar[0]/btn[0]").press()