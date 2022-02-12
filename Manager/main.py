import sys
import monitorcontrol
import ctypes

OFFMODE = "off_soft"

if __name__ == "__main__":
    if len(sys.argv) > 0:
        monitors = monitorcontrol.get_monitors()
        if sys.argv[1] == "locko":
            ctypes.windll.user32.LockWorkStation()
            for monitor in monitors:
                with monitor:
                    monitor.set_power_mode(OFFMODE)
        elif sys.argv[1] == "screenson":
            for monitor in monitors:
                with monitor:
                    monitor.set_power_mode("on")
        elif sys.argv[1] == "screensoff":
            for monitor in monitors:
                with monitor:
                    monitor.set_power_mode(OFFMODE)
        elif sys.argv[1] == "animexd":
            # for with index var
            for i, monitor in enumerate(monitors):
                with monitor:
                    if i == 0:
                        monitor.set_contrast(0)
                        monitor.set_luminance(0)
                        monitor.set_power_mode("on")
                    else:
                        monitor.set_power_mode(OFFMODE)
        else:
            print("Error: Invalid argument")
            sys.exit(1)
    else:
        print("No argument")
        sys.exit(1)
