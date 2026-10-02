import os as _0, random as _1, signal as _2, sys as _3, time as _4

_A, _B, _C = 5, 5, "#0078D7"

_Z = [
    "injecting payload", "bypassing firewall", "decrypting hash",
    "spawning shell", "brute-forcing port", "dumping memory",
    "patching kernel", "overriding ACL", "sniffing packets",
    "escalating privileges", "mounting /dev/null", "flushing cache",
    "handshaking node", "rooting subsystem", "extracting tokens",
    "nmap -sS -T5 -p- {ip}",
    "ssh root@{ip} -p {port}",
    "hashcat -m 0 {hx} rockyou.txt",
    "curl -s http://{ip}:{port}/shell.sh | bash",
    "netstat -ano | findstr {port}",
    "sudo chmod 777 /etc/shadow",
    "tracert {ip}",
    "msfconsole -x 'use exploit/multi/handler'",
    "python3 exploit.py --target {ip} --port {port}",
]
_D, _E = _Z[:15], _Z[15:]

_f = lambda: ".".join(str(_1.randint(1, 254)) for _ in range(4))
_g = lambda n=32: "".join(_1.choice("0123456789abcdef") for _ in range(n))


def _w():
    if _3.platform != "win32":
        _3.exit("This script is for Windows only.")
    _2.signal(_2.SIGINT, _2.SIG_IGN)
    _i()
    _j()
    _0.system("color 07")
    _0.system("cls")


def _h():
    _r = _1.random()
    _t = (
        lambda: "> " + _1.choice(_E).format(
            ip=_f(), port=_1.randint(20, 65535), hx=_g(16)),
        lambda: f"[{_1.randint(0, 100):3d}%] {_1.choice(_D)} ... {_g(12)}",
        lambda: " ".join(_g(2) for _ in range(_1.randint(12, 24))),
        lambda: f"0x{_g(8)}  {_f():<15}  ACCESS_GRANTED",
    )
    return _t[0 if _r < 0.35 else 1 if _r < 0.65 else 2 if _r < 0.85 else 3]()


def _j():
    _k = __import__("tkinter")
    _l = _k.Tk()
    _l.configure(bg=_C)
    _l.attributes("-fullscreen", True)
    _l.attributes("-topmost", True)
    try:
        _l.config(cursor="none")
    except _k.TclError:
        pass
    _l.protocol("WM_DELETE_WINDOW", lambda: None)

    _m = _l.winfo_screenheight() / 1080
    _n = lambda s, b=False: ("Segoe UI", max(8, int(s * _m)), "bold" if b else "normal")

    _o = _k.Frame(_l, bg=_C)
    _o.place(relx=0.12, rely=0.48, anchor="w")

    def _p(t, s, b=False, y=0, w=True):
        _q = _k.Label(_o, text=t, bg=_C, fg="white", font=_n(s, b),
                      justify="left", anchor="w",
                      wraplength=int(_l.winfo_screenwidth() * 0.7) if w else 0)
        _q.pack(anchor="w", pady=y)
        return _q

    _p(":(", 150, y=(0, int(30 * _m)), w=False)
    _p("Your PC ran into a problem and needs to restart. We're just "
       "collecting some error info, and then we'll restart for you.",
       28, y=(0, int(40 * _m)))
    _r = _p("0% complete", 28, y=(0, int(50 * _m)))
    _p("For more information about this issue and possible fixes, visit\n"
       "https://www.windows.com/stopcode", 16, y=(0, int(14 * _m)))
    _p("If you call a support person, give them this info:", 16)
    _p("Stop code: CRITICAL_PROCESS_DIED", 16)

    def _s(p):
        _r.config(text=f"{p}% complete")
        if p < 100:
            _l.after(_1.randint(150, 800), _s, min(100, p + _1.randint(1, 5)))
    _s(0)

    _t = [0]

    def _u(e):
        _t[0] += 1
        if _t[0] >= _B:
            _l.destroy()

    _l.bind("<Escape>", _u)

    def _v():
        _l.lift()
        _l.attributes("-topmost", True)
        _l.focus_force()
        _l.after(500, _v)

    _v()
    _l.mainloop()


def _i():
    _0.system("color 0a")
    _0.system("cls")
    _e = _4.time() + _A
    while _4.time() < _e:
        print(_h(), flush=True)
        _4.sleep(_1.uniform(0.005, 0.03))
    print("\n[!] SYSTEM COMPROMISED. HALTING...\n", flush=True)
    _4.sleep(0.8)


if __name__ == "__main__":
    _w()
