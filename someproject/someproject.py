"""Project"""
import dependency.depmodule
#import other_dependency.depmodule

def get_project_name():
    return "Someproject # %i" % dependency.depmodule.function()

#def get_other_project_name():
#    return "Someproject # %i" % other_dependency.depmodule.function()
