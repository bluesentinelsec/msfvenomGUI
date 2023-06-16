import tkinter as tk
import tkinter.ttk as ttk

from command_builder import *
from subprocess import Popen, PIPE


class GUI:
    def __init__(self):
        self.cmd = CommandBuilder()

        self.main_window = tk.Tk()
        self.main_window.title("msfvenom-gui")

        self.parent_frame = ttk.Frame(self.main_window)
        self.parent_frame.pack(side="left", expand=1)

        self.widget_frame = ttk.Frame(self.parent_frame)
        self.widget_frame.pack(side="left", expand=1, pady=24, padx=24)

        # row 1: path to msfvenom
        self.label_msfvenom_exe = ttk.Label(master=self.widget_frame, text="Path to msfvenom:", justify="right")
        self.var_msfvenom_exe = tk.StringVar(value=self.cmd.msfvenom_path)
        self.entry_msfvenom_exe = ttk.Entry(master=self.widget_frame, textvariable=self.var_msfvenom_exe, width=25)

        # row 2: payload
        self.label_payload = ttk.Label(master=self.widget_frame, text="Payload:", justify="right")
        self.combobox_payload = ttk.Combobox(master=self.widget_frame,
                                             values=PAYLOADS, width=25)
        self.combobox_payload.current(1)

        # row 3: exe format
        self.label_exe_format = ttk.Label(master=self.widget_frame, text="Executable format:", justify="right")
        self.combobox_exe_format = ttk.Combobox(master=self.widget_frame, values=EXE_FORMAT, width=25)

        # row 4: transform format
        self.label_transform_format = ttk.Label(master=self.widget_frame, text="Transform format:", justify="right")
        self.combobox_transform_format = ttk.Combobox(master=self.widget_frame, values=TRANSFORM_FORMAT,
                                                      width=25)

        # row 5: encoder
        self.label_encoder = ttk.Label(master=self.widget_frame, text="Encoding:", justify="right")
        self.combobox_encoder = ttk.Combobox(master=self.widget_frame, values=ENCODING, width=25)

        # row 6: LHOST and RHOST
        self.label_lhost = ttk.Label(master=self.widget_frame, text="LHOST:", justify="right")
        self.var_lhost = tk.StringVar(value="127.0.0.1")
        self.entry_lhost = ttk.Entry(master=self.widget_frame, textvariable=self.var_lhost, width=25)

        self.label_lport = ttk.Label(master=self.widget_frame, text="LPORT:", justify="right")
        self.var_lport = tk.StringVar(value="4444")
        self.entry_lport = ttk.Entry(master=self.widget_frame, textvariable=self.var_lport, width=25)

        # row 7: LPORT and RPORT
        self.label_rhost = ttk.Label(master=self.widget_frame, text="RHOST:", justify="right")
        self.var_rhost = tk.StringVar(value="")
        self.entry_rhost = ttk.Entry(master=self.widget_frame, textvariable=self.var_rhost, width=25)
        self.label_rport = ttk.Label(master=self.widget_frame, text="RPORT:", justify="right")
        self.var_rport = tk.StringVar(value="")
        self.entry_rport = ttk.Entry(master=self.widget_frame, textvariable=self.var_rport, width=25)

        # row 8: output file
        self.label_out_file = ttk.Label(master=self.widget_frame, text="Output file:", justify="right")
        self.var_out_file = tk.StringVar(value="/tmp/payload")
        self.entry_out_file = ttk.Entry(master=self.widget_frame, textvariable=self.var_out_file, width=25)
        # todo: implement fd.asksaveasfilename()

        # row 9: additional arguments
        self.label_opt_args = ttk.Label(master=self.widget_frame, text="Additional arguments:", justify="right")
        self.var_args = tk.StringVar(value="")
        self.entry_opt_args = ttk.Entry(master=self.widget_frame, textvariable=self.var_args, width=25)

        # row 10: generate payload button
        self.button_generate_payload = ttk.Button(master=self.widget_frame, text="Generate Payload",
                                                  command=self.on_click_generate_payload)

        # row 11: generate msfvenom command
        self.label_command = ttk.Label(master=self.widget_frame, text="Msfvenom command:", justify="right")
        self.label_generated_command = ttk.Label(master=self.widget_frame, text="")

        # row 12: output window
        self.label_console_output = tk.Text(master=self.widget_frame)
        self.label_console_output.insert(tk.END, "")

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
        self.label_lport.grid(row=6)
        self.entry_lport.grid(row=6, column=1)

        self.label_rhost.grid(row=7)
        self.entry_rhost.grid(row=7, column=1)
        self.label_rport.grid(row=8)
        self.entry_rport.grid(row=8, column=1)

        self.label_out_file.grid(row=9)
        self.entry_out_file.grid(row=9, column=1)

        self.label_opt_args.grid(row=10)
        self.entry_opt_args.grid(row=10, column=1)

        self.button_generate_payload.grid(row=11, columnspan=2)

        self.label_command.grid(row=12)
        self.label_generated_command.grid(row=13, column=1)
        self.label_console_output.grid(row=14, columnspan=2)

        tk.mainloop()

    def on_click_generate_payload(self):
        self.label_console_output.delete('1.0', tk.END)

        self.cmd.msfvenom_path = self.var_msfvenom_exe.get()
        self.cmd.payload = self.combobox_payload.get()
        self.cmd.exe_format = self.combobox_exe_format.get()
        self.cmd.transform_format = self.combobox_transform_format.get()
        self.cmd.encoding = self.combobox_encoder.get()
        self.cmd.lhost = self.var_lhost.get()
        self.cmd.lport = self.var_lport.get()
        self.cmd.rhost = self.var_rhost.get()
        self.cmd.rport = self.var_rport.get()
        self.cmd.out_file = self.var_out_file.get()
        self.cmd.additional_args = self.var_args.get()

        self.generated_command_str = self.cmd.create_build_command()
        self.label_console_output.insert(tk.END, self.generated_command_str)

        cmd = f"/bin/sh -c '{self.generated_command_str}'"
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
        out = p.stdout.read()
        out += p.stderr.read()

        self.label_console_output.insert(tk.END, out)
