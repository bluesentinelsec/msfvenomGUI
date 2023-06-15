import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk


class GUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title = "msfvenom-gui"

        self.parent_frame = ttk.Frame(self.main_window)
        self.parent_frame.pack(side="left", expand=1)

        self.widget_frame = ttk.Frame(self.parent_frame)
        self.widget_frame.pack(side="left", expand=1, pady=24, padx=24)

        # row 1: path to msfvenom
        self.label_msfvenom_exe = ttk.Label(master=self.widget_frame, text="Path to msfvenom:", justify="right")
        self.entry_msfvenom_exe = ttk.Entry(master=self.widget_frame)

        # row 2: payload
        self.label_payload = ttk.Label(master=self.widget_frame, text="Payload:", justify="right")
        self.combobox_payload = ttk.Combobox(master=self.widget_frame) # TODO: populate this

        # row 3: exe format
        self.label_exe_format = ttk.Label(master=self.widget_frame, text="Executable format:", justify="right")
        self.combobox_exe_format = ttk.Combobox(master=self.widget_frame)


        # row 4: transform format
        self.label_transform_format = ttk.Label(master=self.widget_frame, text="Transform format:", justify="right")
        self.combobox_transform_format = ttk.Combobox(master=self.widget_frame)

        # row 5: encoder
        self.label_encoder = ttk.Label(master=self.widget_frame, text="Encoding:", justify="right")
        self.combobox_encoder = ttk.Combobox(master=self.widget_frame)

        # row 6: LHOST and RHOST
        self.label_lhost = ttk.Label(master=self.widget_frame, text="LHOST:", justify="right")
        self.entry_lhost = ttk.Entry(master=self.widget_frame)
        self.label_rhost = ttk.Label(master=self.widget_frame, text="RHOST:", justify="right")
        self.entry_rhost = ttk.Entry(master=self.widget_frame)

        # row 7: LPORT and RPORT
        self.label_lport = ttk.Label(master=self.widget_frame, text="LPORT:", justify="right")
        self.entry_lport = ttk.Entry(master=self.widget_frame)
        self.label_rport = ttk.Label(master=self.widget_frame, text="RPORT:", justify="right")
        self.entry_rport = ttk.Entry(master=self.widget_frame)

        # row 8: output file
        self.label_out_file = ttk.Label(master=self.widget_frame, text="Output file:", justify="right")
        self.entry_out_file = ttk.Entry(master=self.widget_frame)
        # todo: implement fd.asksaveasfilename()

        # row 9: additional arguments
        self.label_opt_args = ttk.Label(master=self.widget_frame, text="Additional arguments:", justify="right")
        self.entry_opt_args = ttk.Entry(master=self.widget_frame)

        # row 10: generate payload button
        self.button_generate_payload = ttk.Button(master=self.widget_frame, text="Generate Payload")

        # row 11: generate msfvenom command
        self.label_command = ttk.Label(master=self.widget_frame, text="Msfvenom command:", justify="right")
        self.label_generated_command = ttk.Label(master=self.widget_frame)

        # row 12: output window
        self.label_console_output = ttk.Label(master=self.widget_frame)

        # place widgets on grid:
        self.label_msfvenom_exe.grid(row=0)
        self.entry_msfvenom_exe.grid(row=0, column=1)

        self.label_payload.grid(row=1)
        self.combobox_payload.grid(row=1, column=1)

        self.label_exe_format.grid(row=2)
        self.combobox_exe_format.grid(row=2, column=1)

        self.label_transform_format.grid(row=3)
        self.combobox_transform_format.grid(row=3, column=1)

        self.label_encoder.grid(row=4)
        self.combobox_encoder.grid(row=4, column=1)

        self.label_lhost.grid(row=5)
        self.entry_lhost.grid(row=5, column=1)
        self.label_rhost.grid(row=6)
        self.entry_rhost.grid(row=6, column=1)

        self.label_lport.grid(row=7)
        self.entry_lport.grid(row=7, column=1)
        self.label_rport.grid(row=8)
        self.entry_rport.grid(row=8, column=1)

        self.label_out_file.grid(row=9)
        self.entry_out_file.grid(row=9, column=1)

        self.label_opt_args.grid(row=10)
        self.entry_opt_args.grid(row=10, column=1)

        self.button_generate_payload.grid(row=11, columnspan=2)

        self.label_command.grid(row=12)
        self.label_generated_command.grid(row=13, column=1)
        self.label_console_output.grid(row=14)


        tk.mainloop()
