import speech_recognition as sr  # type: ignore
import tkinter as tk
from sound_util import speak
import tkinter.font as font

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Ứng dụng dịch vụ')

        # Set full screen
        self.root.attributes('-fullscreen', True)

        # Customize font
        self.custom_font = font.Font(family="Helvetica", size=16)

        # Create a frame for better organization
        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Label
        self.label = tk.Label(self.frame, text="Chọn chức năng bạn muốn:", font=self.custom_font, bg="#f0f0f0")
        self.label.pack(pady=20)

        # Buttons for services
        self.create_button("Tra cứu BHYT", "tra cứu bảo hiểm")
        self.create_button("Cấp lại bằng lái xe", "cấp lại bằng lái xe")
        self.create_button("Làm giấy tạm trú", "làm giấy tạm trú")

        # Frame for bottom buttons
        self.bottom_frame = tk.Frame(root, bg="#f0f0f0")
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Start Listening button
        self.mic_button = tk.Button(self.bottom_frame, text="Bắt đầu nghe", command=self.start_listening, font=self.custom_font, bg="#4CAF50", fg="white")
        self.mic_button.pack(side=tk.LEFT, padx=20, pady=10)

        # Exit button
        self.exit_button = tk.Button(self.bottom_frame, text="Thoát", command=self.exit_app, font=self.custom_font, bg="#f44336", fg="white")
        self.exit_button.pack(side=tk.RIGHT, padx=20, pady=10)

        self.speech = sr.Recognizer()

    def create_button(self, text, action):
        button = tk.Button(self.frame, text=text, command=lambda: self.perform_action(action), font=self.custom_font, bg="#2196F3", fg="white")
        button.pack(pady=10, padx=20, fill=tk.X)

    def start_listening(self):
        speak("Tôi đang nghe")
        with sr.Microphone() as source:
            self.label.config(text="Đang nghe...")
            self.root.update()  # Update the label immediately
            audio = self.speech.listen(source)

            try:
                text = self.speech.recognize_google(audio, language='vi-VN')
                self.label.config(text=f"Bạn nói: {text}")
                self.perform_action(text)
            except sr.UnknownValueError:
                self.label.config(text="Mời bạn chọn dịch vụ")
            except sr.RequestError as e:
                self.label.config(text="Lỗi kết nối. Vui lòng thử lại.")
                print(f"Request error: {e}")

    def perform_action(self, command):
        from cap_lai_bang_lai_xe import run  # Ensure this is the correct relative path
        command = command.lower()
        if "tra cứu bảo hiểm" in command:
            print("Tra cứu bảo hiểm y tế")
            # Implement your logic for checking health insurance here
        elif "cấp lại bằng lái xe" in command:
            speak("Mời bạn điền vào form sau!")
            run()  # Call the method from the imported module
        elif "làm giấy tạm trú" in command:
            print("Làm giấy tạm trú")
            # Implement your logic for temporary residency here

    def exit_app(self):
        speak("Rất vui được phục vụ bạn, hẹn gặp lại!")
        self.root.destroy()

def run_main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# if __name__ == "__main__":
#     run_main()