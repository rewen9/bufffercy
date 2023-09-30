import subprocess

class clipboardManager():
    def __init__(self) -> None:
        self.is_install_xclip = False
    def get_object_from_clipboard(self) -> str:
            """ Забрать данные исходя из ОС """
            import platform
            system = platform.system()
            if system == 'Linux':
                return self.get_last_copied_object_linux()
            elif system == 'Windows':
                return self.get_last_copied_object_windows()
            else:
                return None

    def get_last_copied_object_linux(self) -> str:
        if self.is_install_xclip:
            self.install_xclip()
            self.is_install_xclip = True
        command = ['xclip', '-selection', 'clipboard', '-o']
        try:
            process = subprocess.run(command, capture_output=True, text=True, timeout=1)  # capture_output=True,
        except subprocess.TimeoutExpired:
            # возможно буфер qt был задействовать
            from PyQt5 import QtWidgets
            clipboard = QtWidgets.QApplication.clipboard()
            text_data = clipboard.text()
            if text_data:
                return text_data
            return None
        return process.stdout.strip() if process.stdout else None

    def get_last_copied_object_windows(self) -> str:
        import win32clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()
        return data

    def install_xclip(self) -> None:
        try:
            # Try running the xclip command
            subprocess.run(['xclip', '-version'], check=True)
        except FileNotFoundError:
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'xclip'])

