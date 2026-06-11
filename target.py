import os, time, threading, urllib.request, urllib.error

print("PID =", os.getpid(), flush=True)
time.sleep(8)

def fetch(label):
    try:
        urllib.request.urlopen(f"http://example.com/{label}", timeout=5)
        print(f"{label}: intercepted (HTTP 200)", flush=True)
    except urllib.error.HTTPError as exc:
        print(f"{label}: NOT intercepted (HTTP {exc.code})", flush=True)
    except Exception as exc:
        print(f"{label}: NOT intercepted ({type(exc).__name__})", flush=True)

fetch("MAIN")
worker = threading.Thread(target=fetch, args=["WORKER"])
worker.start()
worker.join()
