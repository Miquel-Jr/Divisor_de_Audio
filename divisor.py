import os
import wave
import contextlib
import soundfile as sf
from pydub import AudioSegment
#Redirige a la carperta de ubicacion  del archivo python
UPLOAD_FOLDER=os.getcwd()

for archivo in os.listdir(UPLOAD_FOLDER):
		name_file=archivo.split('.')

		if(name_file[1]=='wav'): #Buscamos dentro de la carpeta donde está el archivo python, un archivo con extension ".wav"

			f=sf.SoundFile(archivo)
			time = 30000 
			j=1
			with contextlib.closing(wave.open(UPLOAD_FOLDER+ "/"+ archivo,'r')) as f:
	    			frames = f.getnframes()
	    			rate = f.getframerate()

	    			duration = int((frames / float(rate))*1000) #Duracion total del audio
				for i in range (0,duration,time): #rango de duracion del audio, tiempo que deseamos partir el audio (30seg) 
					newAudio = AudioSegment.from_wav(archivo)
					newAudio = newAudio[i:i+30000] #partimos el audio cada 30 segundos
					newAudio.export(name_file[0]+'_'+str(j)+".---wav")
					j=j+1 #repetimos la accion hasta terminar la duracion
