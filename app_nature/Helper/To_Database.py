import os
import docx


PATH_VYSOKE = r'C:\Users\King\Envs\djangoP\Tatry\nature\app_nature\static\app_nature\Tatry\Vysoke'
PATH_ZAPAD = r'C:\Users\King\Envs\djangoP\Tatry\nature\app_nature\static\app_nature\Tatry\Zapadne'
PATH_NIZKE = r'C:\Users\King\Envs\djangoP\Tatry\nature\app_nature\static\app_nature\Tatry\Nizke'

tatras = [PATH_NIZKE, PATH_ZAPAD, PATH_VYSOKE]


def to_database(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        file = docx.Document(dir + "\\" + fileName)
        text = []
        for paragraph in file.paragraphs:
            text.append(paragraph.text)
        fullText = '\n'.join(text)
        name = text[0]
        height_m = text[1]
        height = float(height_m)
        location = text[2]
        gps = text[3]
        q_description = text[4]
        list_p = list(q_description)
        len_p = len(list_p)
        if len_p > 94:
            del list_p[91:-1]
            del list_p[91]
            list_p.append("...")
            q_description = "".join(list_p)
        description = '\n'.join(text[4:])

        if dir == PATH_VYSOKE:
            heigh_tatras = mountain.objects.get(id=1)
            every_peak = peaks(name_of_mountain=heigh_tatras, name=name, height=height, location=location, gps=gps,
                                quick_description=q_description, text=description)
        elif dir == PATH_NIZKE:
            low_tatras = mountain.objects.get(id=2)
            every_peak = peaks(name_of_mountain=low_tatras, name=name, height=height, location=location, gps=gps,
                               quick_description=q_description, text=description)
        else:
            west_tatras = mountain.objects.get(id=3)
            every_peak = peaks(name_of_mountain=west_tatras, name=name, height=height, location=location, gps=gps,
                               quick_description=q_description, text=description)

        every_peak.save()
        elements_in_text = len(text)
        while elements_in_text != 0:
            del text[elements_in_text - 1]
            elements_in_text -= 1
