# Linux local mode doesn't capture worker-thread traffic (matches tid, not tgid)

Linux local capture (`--mode local:<pid>`) matches the socket-creating thread's id (tid), not the process id (tgid), so requests from worker threads bypass interception (macOS and Windows match by process).

- [Repro run](https://github.com/samatar26/mitmproxy-tid-repro/actions/runs/27317352471/job/80700765686#step:4:13): the main-thread request is intercepted (HTTP 200), the worker-thread one is missed and reaches the real server (HTTP 404).
- [Fixed run](https://github.com/samatar26/mitmproxy-tid-repro/actions/runs/27317352471/job/80700765679#step:5:13): with the one-line `ctx.pid()` → `ctx.tgid()` ([the whole fix](https://github.com/samatar26/mitmproxy-tid-repro/blob/main/.github/workflows/repro.yaml#L40)), both are intercepted (HTTP 200).
