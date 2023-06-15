PAYLOADS = ["",
            "linux/x86/meterpreter/reverse_tcp",
            "linux/x86/meterpreter/bind_tcp",
            "linux/x64/meterpreter_reverse_https",
            "linux/x64/meterpreter/bind_tcp",
            "osx/x64/meterpreter_reverse_https",
            "windows/meterpreter/reverse_https",
            "windows/meterpreter/bind_tcp",
            "windows/x64/meterpreter/bind_tcp",
            "windows/x64/meterpreter/reverse_https"]

EXE_FORMAT = ["",
              "dll",
              "exe",
              "psh",
              "vbs",
              "elf",
              "elf-so",
              "osx-app",
              "python-reflection"]

TRANSFORM_FORMAT = ["",
                    "base32",
                    "base64",
                    "bash",
                    "c",
                    "csharp",
                    "dw",
                    "dword",
                    "go",
                    "golang",
                    "hex",
                    "java",
                    "js_be",
                    "js_le",
                    "nim",
                    "nimlang",
                    "num",
                    "perl",
                    "pl",
                    "powershell",
                    "ps1",
                    "py",
                    "python",
                    "raw",
                    "rb",
                    "ruby",
                    "rust",
                    "rustlang",
                    "sh",
                    "vbapplication",
                    "vbscript"]

ENCODING = ["x64/xor",
            "x64/xor_context",
            "x64/xor_dynamic",
            "x64/zutto_dekiru",
            "x86/add_sub",
            "x86/alpha_mixed",
            "x86/alpha_upper",
            "x86/avoid_underscore_tolower",
            "x86/avoid_utf8_tolower",
            "x86/bloxor",
            "x86/bmp_polyglot",
            "x86/call4_dword_xor",
            "x86/context_cpuid",
            "x86/context_stat",
            "x86/context_time",
            "x86/countdown",
            "x86/fnstenv_mov",
            "x86/jmp_call_additive",
            "x86/nonalpha",
            "x86/nonupper",
            "x86/opt_sub",
            "x86/service",
            "x86/shikata_ga_nai",
            "x86/single_static_bit",
            "x86/unicode_mixed",
            "x86/unicode_upper",
            "x86/xor_dynamic",
            "x86/xor_poly"]

LORUM = "Lorem ipsum dolor sit amet"


class CommandBuilder:
    def __init__(self):
        self.msfvenom_path = ""
        self.payloads = ["one", "two", "three"]

    def get_payloads(self):
        return self.payloads
