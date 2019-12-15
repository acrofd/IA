from Estaciones import Estacion

class Cordenadas:

    def __init__(self):
        self.cordenadas = {}
        self.rojo = ["Shinjuku", "Ochanomizu","Tokyo"]
        self.amarillo = ["Shinjuku", "Yoyogi", "Sendagoya", "Shinanomachi", "Yotsuya", "Iichigaya", "Iidabashi", "Suidobashi", "Ochanomizu", "Akihabara"]
        self.verde = ["Shinjuku", "Yoyogi", "Harajuku", "Shibuya","Ebisu", "Meguro", "Gotanda", "Osaki", "Shinagawa", "Tamachi", "Hamamatsucho", "Shimbashi", "Yurakucho", "Tokyo", "Kanda","Akihabara", "Okachimachi", "Ueno", "Uguisudani", "Nippori", "Nishi-Nippori", "Tabata", "Komagome", "Sugamo", "Otsuka", "Ikebukuro", "Mejiro","Takadanobaba", "Shin-Okubo"]
    
    def añadir(self):
        self.cordenadas["Shinjuku"] = Estacion("Shinjuku", ["Yoyogi", "Shin-Okubo", "Ochanomizu", "Sendagaya"],(35.689619, 139.700575))
        self.cordenadas["Yoyogi"] = Estacion("Yoyogi",["Shinjuku", "Sendagaya", "Harajuku"],(35.683042, 139.702082))
        self.cordenadas["Ochanomizu"] = Estacion("Ochanomizu", ["Tokyo", "Suidobashi", "Shinjuku"], (35.699406, 139.765246))
        self.cordenadas["Sendagaya"] = Estacion("Sendagaya", ["Yoyogi", "Shinanomachi", "Shinjuku"], (35.681200, 139.711285))
        self.cordenadas["Shinanomachi"] = Estacion("Shinanomachi", ["Sendagaya", "Yotsuya"], (35.680098, 139.720326))
        self.cordenadas["Yotsuya"] = Estacion("Yotsuya",  ["Shinanomachi", "Iichigaya"], (35.686164, 139.730222))
        self.cordenadas["Iichigaya"] = Estacion("Iichigaya", ["Yotsuya", "Iidabashi"], (35.691028, 139.735566))
        self.cordenadas["Iidabashi"] = Estacion("Iidabashi",["Iichigaya", "Suidobashi"] , (35.702090, 139.745022))
        self.cordenadas["Suidobashi"] = Estacion("Suidobashi", ["Iidabashi", "Akihabara", "Ochanomizu"], (35.702056, 139.753502))
        self.cordenadas["Akihabara"] = Estacion("Akihabara", ["Suidobashi", "Kanda", "Okachimachi"], (35.702056, 139.753502))
        self.cordenadas["Tokyo"] = Estacion("Tokyo", ["Ochanomizu", "Yurakucho", "Kanda"], (35.666396, 139.758345))
        self.cordenadas["Shin-Okubo"] = Estacion("Shin-Okubo", ["Shinjuku",  "Takadanobaba"], (35.701490, 139.700204))
        self.cordenadas["Takadanobaba"] = Estacion("Takadanobaba", ["Mejiro", "Shin-Okubo"], (35.712603, 139.703857))
        self.cordenadas["Mejiro"] = Estacion("Mejiro", ["Ikebukuro", "Takadanobaba"], (35.721186, 139.706558))
        self.cordenadas["Ikebukuro"] = Estacion("Ikebukuro", ["Mejiro", "Otsuka"], (35.729534, 139.710901))
        self.cordenadas["Otsuka"] = Estacion("Otsuka", ["Ikebukuro", "Sugamo"], (35.731836, 139.728110))
        self.cordenadas["Sugamo"] = Estacion("Sugamo", ["Otsuka", "Komagome"], (35.733448, 139.739285))
        self.cordenadas["Komagome"] = Estacion("Yoyogi",["Sugamo", "Tabata"] , (35.736578, 139.747008))
        self.cordenadas["Tabata"] = Estacion("Tabata", ["Komagome", "Nishi-Nippori"], (35.738168, 139.760815))
        self.cordenadas["Nishi-Nippori"] = Estacion("Nishi-Nippori", ["Tabata", "Nippori"], (35.732047, 139.766875))
        self.cordenadas["Nippori"] = Estacion("Nippori", ["Nishi-Nippori", "Uguisudani"], (35.728174, 139.770640))
        self.cordenadas["Uguisudani"] = Estacion("Uguisudani", ["Nippori", "Ueno"], (35.721463, 139.778011))
        self.cordenadas["Ueno"] = Estacion("Ueno",['Uguisudani', "Okachimachi"], (35.714180, 139.777410))
        self.cordenadas["Okachimachi"] = Estacion("Okachimachi",["Akihabara", "Ueno"], (35.707531, 139.774852))
        self.cordenadas["Kanda"] = Estacion("Kanda",["Akihabara", "Tokyo"], (35.691838, 139.770930))
        self.cordenadas["Yurakucho"] = Estacion("Yurakucho",["Tokyo", "Shimbashi"], (35.674942, 139.762820))
        self.cordenadas["Shimbashi"] = Estacion("Shimbashi",["Yurakucho", "Hamamatsucho"], (35.666396, 139.758345))
        self.cordenadas["Hamamatsucho"] = Estacion("Hamamatsucho", ["Shimbashi", "Tamachi"], (35.655389, 139.757139))
        self.cordenadas["Tamachi"] = Estacion("Tamachi",["Hamamatsucho", "Shinagawa"], (35.645744, 139.747560))
        self.cordenadas["Shinagawa"] = Estacion("Shinagawa",["Tamachi", "Osaki"], (35.628480, 139.738758))
        self.cordenadas["Osaki"] = Estacion("Osaki",["Shinagawa", "Gotanda"], (35.619861, 139.728189))
        self.cordenadas["Gotanda"] = Estacion("Gotanda",["Osaki", "Meguro"], (35.626171, 139.723601))
        self.cordenadas["Meguro"] = Estacion("Meguro",["Gotanda", "Ebisu"], (35.634116, 139.715830))
        self.cordenadas["Ebisu"] = Estacion("Ebisu",["Meguro", "Shibuya"], (35.646727, 139.710076))
        self.cordenadas["Shibuya"] = Estacion("Shibuya",["Ebisu", "Harajuku"], (35.658050, 139.701634))
        self.cordenadas["Harajuku"] = Estacion("Harajuku",["Yoyogi", "Shibuya"], (35.671612, 139.702930))

    def getLinea(self, estacion):
        lineas = []
        if(estacion in self.rojo):
            lineas.append("rojo")
        if(estacion in self.verde):
            lineas.append("verde")
        if(estacion in self.amarillo):
            lineas.append("amarillo")
        return lineas
        
    def getEstaciones(self):
        return self.cordenadas

    def getRojo(self):
        return self.rojo

    def getVerde(self):
        return self.verde

    def getAmarillo(self):
        return self.amarillo
