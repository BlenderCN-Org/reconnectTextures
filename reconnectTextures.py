"""
This script is meant to eaisly reconnect textures
by taking all materials on selected objects and
searching and trying to reconnect textures in 
another listed directory.

Needs to be given a UI and such

"""


import bpy
import os

def reconnectTextures(matList,directory):
	for mat in matList:
		for textureSlot in mat.texture_slots:
			if textureSlot == None: continue
			image = textureSlot.texture.image
			initial = bpy.path.basename(image.filepath)
			# do things to recover path
			newPath = os.path.join(bpy.path.abspath(directory),initial)
			if "//" in image.filepath:
				newPath = bpy.path.relpath(newPath)	
			image.filepath = 
			image.reload()
			bpy.ops.image.reload()
	for area in bpy.context.screen.areas:
		area.tag_redraw()
		#if area.type in ['IMAGE_EDITOR', 'VIEW_3D','PROPERTIES']:
		#	area.tag_redraw()

########
# gets all materials on input list of objects
def getObjectMaterials(objList):
	matList = []
	
	#loop over every object, adding each material if not alraedy added
	for obj in objList:
		#must be a mesh, e.g. lamps or cameras don't have 'materials'
		if obj.type != 'MESH': continue
		
		objectsMaterials = obj.material_slots
		for materialID in objectsMaterials:
			if materialID.material not in matList:
				matList.append(materialID.material)
	return matList

def main():
	
	directory = "/path/to/your/folder/"
	matList = getObjectMaterials(bpy.context.selected_objects)
	reconnectTextures(matList,directory)
	
	#currently need to reload blend file to work
main()

