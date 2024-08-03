import tkinter as tk
from tkinter import ttk
from pptx_class import pptx
import os

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x700')
        self.root.title('Praise the Lord')
        self.mainframe = tk.Frame(self.root, background='pink')
        self.mainframe.pack(fill='both', expand=True)

        # Title text
        self.text = ttk.Label(self.mainframe, text='Praise the Lord',
                              background='pink', font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        # Mode Dropdown
        options_mode = ['Adviento', 'Navidad', 'Cuaresma', 'Semana Santa', 'Pascua', 'Tiempo Ordinario']
        self.set_mode_field = ttk.Combobox(self.mainframe, values=options_mode)
        self.set_mode_field.grid(row=1, column=0, sticky='NWES', pady=10)
        mode_button = ttk.Button(self.mainframe, text='Época del Año', command=self.set_mode)
        mode_button.grid(row=1, column=1, pady=10)

        # Intro Options
        self.folder_path_intro = 'C:\\Users\\bucky\\Documents\\designMedia\\pptxMaker\\songs\\1_intro'
        options_intro = self.get_txt_files(self.folder_path_intro)
        self.set_intro_field = ttk.Combobox(self.mainframe, values=options_intro)
        self.set_intro_field.grid(row=2, column=0, sticky='NWES', pady=10)
        self.intro_text = ttk.Label(self.mainframe, text='Intro')
        self.intro_text.grid(row=2, column=1)

        # Salmo Options
        self.set_salmo_field = ttk.Entry(self.mainframe)
        self.set_salmo_field.grid(row=3, column=0, pady=10, sticky='NWES')
        self.salmo_text = ttk.Label(self.mainframe, text='New Salmo')
        self.salmo_text.grid(row=3, column=1)

        # Aleluya Options
        options_aleluya = ['Aleluya', 'Canta Aleluya']
        self.set_aleluya_field = ttk.Combobox(self.mainframe, values=options_aleluya)
        self.set_aleluya_field.set("Select an option")

        # PPTX Button
        generate_button = ttk.Button(self.mainframe, text='Take Me To Church', command=self.lyric2pptx)
        generate_button.grid(row=5, column=0, pady=10)

        self.root.mainloop()
        return

    def get_txt_files(self, folder_path):
        return [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    def set_mode(self):
        pass

    def lyric2pptx(self):
        salmo_song = self.set_salmo_field.get()
        aleluya_song = self.set_aleluya_field.get()
        prs = pptx()
        prs.add_title_slide("Mass Songs")
        selected_option = self.set_intro_field.get()
        if selected_option:
            with open(os.path.join(self.folder_path_intro, selected_option), 'rt', encoding='utf-8') as file:
                intro_song = file.read()
        prs.add_song_slide(str(intro_song))
        prs.add_song_slide(str(salmo_song))
        prs.save_presentation("test 9.pptx")


if __name__ == '__main__':
    App()
