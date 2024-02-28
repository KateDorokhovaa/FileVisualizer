import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class FileVisualizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Visualizer")
        
        # Створюємо кнопку для вибору файлу
        self.load_button = tk.Button(master, text="Вибрати файл", command=self.load_file)
        self.load_button.pack()
        
        # Ініціалізуємо змінні для зберігання шляху до файлу та розмірів графічної області
        self.file_path = ""
        self.canvas_width = 800
        self.canvas_height = 600
        
        # Створюємо графічну область для візуалізації
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

    def load_file(self):
        # Відкриваємо діалогове вікно для вибору файлу
        self.file_path = filedialog.askopenfilename()
        
        # Завантажуємо файл і відображаємо його в графічній області
        binary_array = self.load_binary_array(self.file_path)
        self.display_binary_array(binary_array)

    def load_binary_array(self, file_path):
        # Зчитуємо бінарний масив з файлу
        # Уявімо, що тут реалізований код для зчитування бінарного масиву з файлу
        # Одержуємо бінарний масив у вигляді NumPy масиву
        binary_array = np.random.randint(0, 2, size=(self.canvas_height, self.canvas_width // 8))  # Тимчасова імітація масиву
        
        return binary_array

    def display_binary_array(self, binary_array):
        # Перевіряємо, чи розмір масиву відповідає розміру графічної області
        if binary_array.shape[0] < self.canvas_height:
            # Якщо елементів масиву менше ніж кількість пікселів в графічній області,
            # то доповнюємо масив сірим кольором
            padding = self.canvas_height - binary_array.shape[0]
            binary_array = np.pad(binary_array, ((0, padding), (0, 0)), mode='constant', constant_values=0.5)
        
        # Обрізаємо масив, якщо кількість рядків більше, ніж кількість пікселів у графічній області
        binary_array = binary_array[:self.canvas_height, :self.canvas_width // 8]
        
        # Малюємо кожному елементу масиву відповідний піксель у графічній області
        for i in range(binary_array.shape[0]):
            for j in range(binary_array.shape[1]):
                pixel_color = "black" if binary_array[i, j] == 1 else "white" if binary_array[i, j] == 0 else "gray"
                self.canvas.create_rectangle(j * 8, i, (j + 1) * 8, i + 1, fill=pixel_color, outline="")

def main():
    root = tk.Tk()
    app = FileVisualizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
