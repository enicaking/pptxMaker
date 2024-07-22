import tkinter as tk
from tkinter import ttk
from pptx_class import pptx


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x700')
        self.root.title('pptx Maker: Praise the Lord')
        self.mainframe = tk.Frame(self.root, background='pink')
        self.mainframe.pack(fill='both', expand=True)

        # Title text
        self.text = ttk.Label(self.mainframe, text='pptx Maker: Praise the Lord',
                              background='pink', font=("Brass Mono", 30))
        self.text.grid(row=0, column=0)

        # Intro Options
        options_intro = ['Dios está aquí', 'Ven a celebrar']
        self.set_intro_field = ttk.Combobox(self.mainframe, values=options_intro)
        self.set_intro_field.grid(row=1, column=0, sticky='NWES', pady=10)

        # Salmo Options
        self.set_salmo_field = ttk.Entry(self.mainframe)
        self.set_salmo_field.grid(row=2, column=0, pady=10, sticky='NWES')

        # PPTX Button
        generate_button = ttk.Button(self.mainframe, text='Take Me To Church', command=self.lyric2pptx)
        generate_button.grid(row=4, column=0, pady=10)

        self.root.mainloop()
        return

    def lyric2pptx(self):
        intro_song = self.set_intro_field.get()
        salmo_song = self.set_salmo_field.get()
        prs = pptx()
        prs.add_title_slide("Date Today", "Yahoo")
        prs.add_song_slide(str(intro_song))
        prs.add_song_slide(str(salmo_song))
        prs.save_presentation("test 8.pptx")


if __name__ == '__main__':
    App()
