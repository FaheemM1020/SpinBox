import customtkinter as CTK
from typing import Callable

class FloatSpinbox(CTK.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size = 1,
                 add_command: Callable = None,
                 subract_command: Callable = None,
                 max_value: int = None,
                 min_value:int = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.stepsize = step_size
        self.add_command = add_command # Command to call when plus button is clicked
        self.subtract_command = subract_command  # Command to call minus button is clicked
        self.max_value = max_value
        self.min_value = min_value

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = CTK.CTkFrame(self, height=50)
        self.frame.grid(column=1, row=0, sticky='nsew')

        self.plus = CTK.CTkButton(self.frame, text='+', font=("roboto", 40), width=20, height=20, command=self.add)
        self.plus.pack(side='left',padx=2)

        self.entry = CTK.CTkEntry(self.frame, font=("roboto", 40), width=120, height=50)
        self.entry.pack(side='left',padx=2)
        self.entry.insert(CTK.END, 1.0 if self.min_value is None else float(self.min_value))

        self.minus = CTK.CTkButton(self.frame, text='-', font=("roboto", 40), width=40, height=20, command=self.subtract)
        self.minus.pack(side='left',padx=2)

    def add(self):
        if self.min_value is not None:
            if self.min_value > self.max_value:
                raise ValueError(f'min_value ({self.min_value}) greater than max_value ({self.max_value})')
            
        try:
            value = float(self.entry.get()) + self.stepsize
            
            if self.max_value is not None and value > self.max_value:
                print("Maximum Value Reached")
                return
            
            self.entry.delete(0, CTK.END)
            self.entry.insert(CTK.END, value)

            if self.add_command is not None:
                self.add_command()

        except ValueError as e:
            return

    def subtract(self):
        if self.min_value is not None:
            if self.min_value > self.max_value:
                raise ValueError(f'min_value ({self.min_value}) greater than max_value ({self.max_value})')
            
        try:
            value = float(self.entry.get()) - self.stepsize

            if self.min_value is not None and value < self.min_value:  # Change the condition here 
                return
            
            self.entry.delete(0, CTK.END)
            self.entry.insert(CTK.END, value)

            if self.subtract_command is not None:
                self.subtract_command()

        except ValueError:
            return

    def get(self):
        value = self.entry.get()
        return value

    def set(self, value: float):
        if self.min_value is not None and self.max_value is not None :
            if value > self.max_value :
                raise ValueError(f"Value ({value}) is greater than max_value {self.max_value}")
            elif value < self.min_value:
                raise ValueError(f"Value ({value}) is lesser than min_value {self.min_value}")

        self.entry.delete(0, CTK.END)
        self.entry.insert(CTK.END, float(value))
