# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

module = GetParams("module")

if module == "add_value":
    key_ = GetParams("key")
    value_ = GetParams("value")
    dict_ = GetParams("dict")
    res = GetParams("res")
    try:
        import json
        new_dict = json.loads(dict_)            
        new_element = {
            key_: value_
        }
        new_dict.update(new_element)
        SetVar(res, new_dict)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "delete_value":
    key_ = GetParams("key")
    dict_ = GetParams("dict")
    res = GetParams("res")
    try:
        import json
        new_dict = json.loads(dict_)            
        del new_dict[key_]
        SetVar(res, new_dict)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "find_element":
    dict_ = GetParams("dict")
    path_selector = GetParams("path_selector")
    res = GetParams("res")
    try:
        #xpath = "first/second/thrid?"
        import json
        dict_ = json.loads(dict_)
        path = path_selector.split("/")
        for p in path:
            dict_ = dict_[p]
        SetVar(res, dict_)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e    
    