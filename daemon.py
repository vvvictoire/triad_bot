import daemon

from triad_bot import main

with daemon.DaemonContext():
    main()
