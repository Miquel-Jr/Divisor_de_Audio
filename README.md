Divisor_de_Audios

Funcionalidad del archivo:

Separa los audios de tipo o extension ".wav" cada 30 segundos

Ejecución del proyecto "Divisor_de_Audios":

UPLOAD_FOLDER = os.getcwd();

EL programa comenzará a analizar la carperta donde se encuentre ubicada y buscará por defecto algún tipo de archivo wav para poder empezar la ejecución.

Al ejecutarse empezará a crear formatos wav con duracion de 30 segundos , adicionando a su nombre las cantidades de veces que se partio. 
Por ejemplo:

audio[1].wav;
audio[2].wav;
audio[3].wav;
.
.
.
audio[n].wav

El último audio no siempre tendrá los 30 segundos, ya que eso dependerá de la duracion de la canción, de que su duracion contenga un multiplo de 30, en caso no sea asi, el ultimo audio tendrá los segundos restantes.

Si no existe archivos en la carpeta de formato wav es recomendable poner alguno.

En caso tenga muchas archivos de formato wav y desee uno en específico deberá crear la variable "archivo" y asignar el nombre en específico del archivo wav para que pueda ejecutar solo ese

En otro caso, si desea analizar otra carpeta en donde se encuentren sus archivos solo deberá cambiar la ruta de la carpeta como por ejemplo:

UPLOAD_FOLDER= "/home/miqueel/Escritorio/ArchivosWav"




