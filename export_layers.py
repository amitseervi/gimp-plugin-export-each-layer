from gimpfu import *

def export_layers(image, outputFolder):
    spritesheet = pdb.gimp_image_duplicate(image)
    for i in range(len(image.layers)):
        if not image.layers[i].visible:
            continue
        layer_copy = pdb.gimp_layer_new_from_drawable(
            image.layers[i], spritesheet)
        try:
            for j in range(len(spritesheet.layers)):
                pdb.gimp_image_remove_layer(spritesheet, spritesheet.layers[j])
        except:
            pass
        pdb.gimp_image_insert_layer(
            spritesheet, layer_copy, None, 0)
        pdb.plug_in_autocrop(spritesheet, layer_copy)
        pdb.gimp_item_set_visible(layer_copy, True)
        layer_name = image.layers[i].name
        raw_file_name = outputFolder+"/"+layer_name+".png"
        pdb.file_png_save(spritesheet, spritesheet.layers[0], raw_file_name, raw_file_name, 0, 9, 0, 0, 0, 0, 0)
    pdb.gimp_image_delete(spritesheet)


register(
    "python-fu-export-layers",
    "Export layers as individual png files",
    "This script will help export each layer file as individual png image with layer name as file name",
    "Amit",
    "Seervi",
    "2023",
    "Export Layers",
    "",
    [
        (PF_IMAGE, "image", "Select Image", None),
        (PF_DIRNAME, "outputFolder", "Output directory", None),
    ],
    [],
    export_layers, menu="<Image>/Image")

main()
