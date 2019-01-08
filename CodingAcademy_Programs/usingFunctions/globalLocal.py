# returns True or False if the variable is either global or local

aGlobalariable = 1


def aFunction():
    aLocalVariable = -10
    print('The aLocalVariable inside aFunction:',
          'aLocalVariable' in locals())
    print('The aGlobalariable inside aFunction:',
          'aGlobalariable' in locals())


aFunction()
print('aLocalVariable in main:', 'aLocalVariable' in globals())
print('aGlobalariable in main:', 'aGlobalariable' in globals())
