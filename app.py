import winreg
from protocol_handler import ProtocolHandler
import html_creator
import gui

SOC_PATH = ['shell', 'open', 'command']


def get_all_custom_protocol_handlers() -> 'list[ProtocolHandler]':
    hkey_classes_root = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    key_names = get_all_keys(hkey_classes_root)
    socs = get_all_socs(hkey_classes_root, key_names)
    return socs


def get_all_keys(hkey):
    result = []
    i = 0
    while True:
        try:
            key_name = winreg.EnumKey(hkey, i)
            result.append(key_name)
            i += 1
        except:
            break
    return result


def get_all_socs(hkey, key_names):
    result = []
    for key_name in key_names:
        value = try_get_soc_value(hkey, key_name)
        if value != None:
            result.append(value)
    return result


def try_get_soc_value(hkey, key_name):
    key = None

    try:
        joined_soc_path = '\\'.join(SOC_PATH)
        soc_sub_key = f"{key_name}\{joined_soc_path}"
        key = winreg.OpenKey(hkey, soc_sub_key)
    except:
        return None # у данного ключа не нашлось shell/open/command

    i = 0
    while True:
        try:
            (value_name, value_data, data_type) = winreg.EnumValue(key, i)
            if value_name == '':
                return ProtocolHandler(key_name, soc_sub_key, value_data)
            i += 1
        except Exception as e:
            break  # не нашли заданного значения для ключа shell/open/command
        finally:
            winreg.CloseKey(key)

    return None


socs = get_all_custom_protocol_handlers()
# html_creator.write_files(socs)
gui.render_gui(socs)