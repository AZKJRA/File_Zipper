import shutil
import time
import glob

def start_infos():
    info = [
        "Programme De Compression Et De Decompression des Fichiers",
        "Ce Logiciel Permet de Compression Et De Decompression Des Fichiers Automatiquement",
        "Vous Devez Simplement Entrez le Nom de Fichiers a Compresser ou a Decompresser",
        "Attention !!!! le Programme doit Etre execute Dans Le meme repertoire que le Fichier a Compresser ou Decompresser",
        "A Note !!!! le Programme est compatible avec les formats format suivants:",
        " >>> zip ",
        " >>> tar "
    ]

    for fs in info:
        print(fs)
        print()
        time.sleep(1.9)

def get_file_name():
    name = input("Entrez le nom du Fichier: ")
    return name

def name_out():
    out_name = input("Entrez le nom du fichier en sortie: ")
    return out_name

def zipper_function():
    try:
        name = get_file_name()
        found = glob.glob("*")
        names = name.split(".")
        first_extension = names[0]
        if name:
            for fd in found:
                if fd == name:
                    out_name = name_out()
                    if fd.endswith(".zip"):
                        if out_name:
                            shutil.unpack_archive(f"{fd}", f"{out_name}_extraction_zip")
                        shutil.unpack_archive(f"{fd}", f"{first_extension}_extraction_zip")
                    elif fd.endswith(".tar"):
                        if out_name:
                            shutil.unpack_archive(f"{fd}", f"{out_name}_extraction_tar", "tar")
                        shutil.unpack_archive(f"{fd}", f"{first_extension}_extraction_tar", "tar")
                    else:
                        if out_name:
                            shutil.make_archive(f"{out_name}_zip", "zip", f"{fd}")
                        shutil.make_archive(f"{fd}_zip", "zip", f"{fd}")
                else:
                    print("Aucun Fichier Trouver !!!!!!!!!!!!!!!!")
        else:
            print("Fin du Processus .........././././././././././././././")
    except:
        print("Fin du Processus .........././././././././././././././")


start_infos()

zipper_function()

input()