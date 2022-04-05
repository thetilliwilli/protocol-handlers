from tkinter import *
from tkinter.ttk import *
from protocol_handler import ProtocolHandler


def render_gui(protocol_handlers: "list[ProtocolHandler]"):
    window = Tk()
    window.title("Protocol handler viewer")

    main_frame = Frame(window, padding="4 4 4 4")
    main_frame.grid()

    for index, protocol_handler in enumerate(protocol_handlers):
        if index > 10:
            break
        render_protocol_handler(main_frame, index, protocol_handler)

    window.mainloop()


def render_protocol_handler(parent, index, protocol_handler):
    frame = Frame(parent)
    frame.grid(row=index, column=0)

    Label(frame, text=str(index)).grid(row=0, column=0)

    text = Text(frame, height=1)
    text.insert("1.0", protocol_handler.protocol)
    text.grid(row=0, column=1)
    text.config(state="disabled")

    Button(frame, text="open").grid(row=0, column=2)
