import bpy
import bmesh
import os
import mathutils
import csv

# IMPORT TEXTFILE                  
directory = 'C:\\Users\\zesbaans\\Documents\\Moira\\blenderpython\\script blender\\libraryscripttest.blend\\Object\\' 

def load(characterName, name = "NewObject"):
	bpy.ops.wm.append(filename=characterName, directory=directory, autoselect=True)
	newObj = bpy.context.selected_objects[0]
	newObj.name = name
	return newObj


def loadAll(inputFile):
	f=open(inputFile)																	# open textfile
	list=[] 																			# make list 		
	currentPosition = 0																
	for line in f.readline():															# iterate over each character 
		objects = [line]																# open object with name [line] (characters in text) 
		for char in objects:																# iterate over objects															#
			obj = load(char, name=str(currentPosition))
			list.append(obj)
			currentPosition += 1
	return list



# DEF LOOPCUT
def loopCut( return_area = False ):                         # returns first 3d view, normally we get from context
    for area in bpy.context.window.screen.areas:                # area in windowsscreen areas
        if area.type == 'VIEW_3D':                              # if the area type is 3D view
            v3d = area.spaces[0]                                # v3d, 3d space
            rv3d = v3d.region_3d                                # rv3d, active region
            for region in area.regions:                         # for region in area regions
                if region.type == 'WINDOW':                     # if the region type is a window
                    if return_area: return region, rv3d, v3d, area # if return area is return region, rv3d, v4d or area
                    return region, rv3d, v3d                    # return region rvd, v3d
    return None, None                                           # return None for both regions

region, rv3d, v3d, area = loopCut(True)                     # when the view3d finds the region, rv3d, area it is true

override = {                                                    # override 
    'scene'  : bpy.context.scene,                               # scene, active scene
    'region' : region,                                          # region
    'area'   : area,                                            # area
    'space'  : v3d                                              # space
}


# DEF CYLINDER 
def cylinder(numberOfVertices, radius, depth, numberOfCuts):
    bpy.ops.mesh.primitive_cylinder_add(vertices=numberOfVertices, radius=radius, depth=depth, end_fill_type='NOTHING', view_align=False, enter_editmode=False, location=(0, 0, 0)) 
                                                                # create cylinder, radius and depth                                         
    #name = bpy.data.objects['Cylinder']                         # name it cylinder1
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)        # set to objectmode
    bpy.ops.object.modifier_add(type='SOLIDIFY')                # call solidify modifier
    bpy.context.object.modifiers["Solidify"].thickness = 0.2    # thickness of solidify 
    bpy.ops.object.editmode_toggle()                            # set to editmode 
    
    bpy.ops.mesh.loopcut_slide(         
        override, 
        MESH_OT_loopcut = {
            "number_cuts"           : numberOfCuts,              # number of cuts
            "smoothness"            : 1,                         # smoothness
            "falloff"               : 'SMOOTH',                  # was'INVERSE_SQUARE' that does not exist
            "edge_index"            : 1,                         # edge index? 
            "mesh_select_mode_init" : (True, False, False)       # ? 
    })
    bpy.ops.object.mode_set(mode='OBJECT')
    return bpy.context.object



# DEF FACEPOSITION
def getListOfFaces(obj):
    bpy.context.scene.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    mesh = bmesh.from_edit_mesh(obj.data)            
    mesh.faces.ensure_lookup_table()                                # call lookuptable
    
    rotList = []
    centerList = []
    
    z = mathutils.Vector((0,0,1))                               # call Vector y axis from mathutilis
    
    for face in mesh.faces:
        centerList.append(list(face.calc_center_median()))                # calculate center             
        rotList.append(list(z.rotation_difference( face.normal ).to_euler())) # list roation difference normal/euler
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return rotList, centerList

##########

textFile = 'C:\\Users\\zesbaans\\Documents\\Moira\\blenderpython\\text.txt'			# import text.csv 
verValue = 35
radValue = 1
depValue = 5
numValue = 15

# Load text file characters into 3D objects
characterObjects = loadAll(textFile)

# Make a cylinder, collect rotation and position of each face
c = cylinder(verValue, radValue, depValue, numValue)
rotations, centerPositions = getListOfFaces(c)

#TODO: verwerk alle characterObjects door ze op een positie+rotatie te zetten.
#for index, item in enumerate(rotations):
#    rotation = item
#    position = centerPositions[index]

def getPositionface     
    for rotation, position in zip(alist, blist):
        print a, b
        return ...  