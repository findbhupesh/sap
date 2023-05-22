def fill_textbox(sap,xpath,value):
    try : 
        sap.findByID(xpath).text = value
    except:
        pass

def read_textbox(sap,xpath):

    try : 
        value = sap.findByID(xpath).text 
        return value
    except:
        pass

def click_button(sap,xpath):
    try : 
        sap.findByID(xpath).press()
    except:
        pass

def select_radio(sap,xpath):
    try:
        sap.findByID(xpath).select()
    except:
        pass

def send_cntrkey(sap,xpath,value):
    
    try:
        sap.findByID(xpath).sendVKey(value)
    except:
        pass

def select_cmkey(sap,xpath,value):
    try:
        sap.findByID(xpath).key = value
    except:
        pass