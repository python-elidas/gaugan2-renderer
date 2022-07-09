from gaugan2_renderer import Gaugan2Renderer
from tkinter import filedialog, Tk
import os 

def run():
    renderer = Gaugan2Renderer(waiting_time=10)
    more = 'y'
    styles = [
        'example0', 'example1', 
        'example2', 'example3', 
        'example4', 'example5', 
        'example6', 'example7', 
        'example8', 'example9', 'example10'
    ]
    while more == 'y':
        os.system('color a')
        os.system('cls')
        input(
        '''
        ######################################
        #   Welcome to the Gaugan2Renderer   #
        ######################################

        Presione cualquier tecla para continuar
        '''
        )
        root = Tk()
        in_folder = filedialog.askdirectory(title='Seleccione la carpeta de entrada')
        out_folder = filedialog.askdirectory(title='Seleccione la carpeta de salida')
        root.destroy()
        
        [print(f'{styles.index(i)}. {i}') for i in styles]
        try:
            ind = int(input('Seleccione el estilo:\n>>> '))
            renderer.run(in_folder, out_folder, styles[ind])
        except ValueError:
            ind = int(input('Seleccione el estilo:\n>>> '))
            renderer.run(in_folder, out_folder, styles[ind])
        
        vid_name = input('Ingrese el nombre del video:\n>>> ')
        try:
            if vid_name.splir('.')[-1] == 'mp4': pass
            else: '.'.join([vid_name, 'mp4'])
        except:
            vid_name = '.'.join([vid_name, 'mp4'])
        renderer.create_video(os.path.join(out_folder,vid_name))
        more = input('¿Desea continuar? (y/n)\n>>> ').lower()
        
if __name__ == '__main__':
    run()
